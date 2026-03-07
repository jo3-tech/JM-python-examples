# Copyright (C) 2026 Joseph Morgridge
#
# Licensed under MIT License.
# See the LICENSE file in the project root for full license details.

"""
Robot Model class.

Class that handles creation of the robot model and it's operations.
"""

import math
import pinocchio as pin
import numpy as np
from numpy.typing import NDArray
from typing import Annotated

def verify_pinocchio():
    """Verify Pinocchio library is installed."""
    print(pin.__file__)
    print(dir(pin))
    print(hasattr(pin, 'Model'))
    print(pin.Model)

class RRRPlanarRobot():
    """The RRR Planar Robot class"""

    def __init__(self, link1_length: float, link2_length: float):
        print("Creating robot model.\n")

        # Model.

        self.model = pin.Model()

        # Joint 1: Revolute about y-axis at origin.
        j1_parent_id = self.model.getJointId('universe')
        j1_model = pin.JointModelRZ()
        j1_placement = pin.SE3(np.eye(3), np.zeros(3)) # pin.SE3.Identity()
        self.j1_id = self.model.addJoint(j1_parent_id, j1_model, j1_placement, 'joint1')

        # Joint 2: Revolute about y-axis at end of link 1.
        j2_parent_id = self.j1_id
        j2_model = pin.JointModelRZ()
        j2_placement = pin.SE3(np.eye(3), np.array([link1_length, 0.0, 0.0]))
        self.j2_id = self.model.addJoint(j2_parent_id, j2_model, j2_placement, 'joint2')

        # Joint 3: Revolute about y-axis at end of link 2.
        j3_parent_id = self.j2_id
        j3_model = pin.JointModelRZ()
        j3_placement = pin.SE3(np.eye(3), np.array([link2_length, 0.0, 0.0]))
        self.j3_id = self.model.addJoint(j3_parent_id, j3_model, j3_placement, 'joint3')

        # End-effector frame at joint 3.
        ee_parent_id = self.j3_id
        ee_placement = pin.SE3(np.eye(3), np.zeros(3)) # pin.SE3.Identity()
        ee_frame_type = pin.FrameType.OP_FRAME
        ee_frame = pin.Frame('end_effector', ee_parent_id, 0, ee_placement, ee_frame_type)
        self.ee_frame_id = self.model.addFrame(ee_frame)

        # Data.

        self.data = self.model.createData()

    def print_joint_placements(self) -> None:
        """Print each joint placement in the chain/series."""
        print(f"\nNo. of joints = {self.model.nq}\n")
        for j_id in [self.j1_id, self.j2_id, self.j3_id]:
            print("\nJoint ", j_id, ":\n", self.model.jointPlacements[j_id])
        print("\n")

    def print_end_effector_Tm_from_q(self, q: Annotated[NDArray[np.float64], (3,)]) -> None:
        """Print robot pose/end-effector transformation matrix for a given joint configuration."""
        pin.forwardKinematics(self.model, self.data, q)
        pin.updateFramePlacements(self.model, self.data)
        print("\nEnd-effector Tm:\n", self.data.oMf[self.ee_frame_id])
        print("\n")

    def print_end_effector_Tm_from_p(self, px: float, py: float, configuration: int) -> None:
        """Print robot pose/end-effector transformation matrix for a given e-e position (px, py)."""
        q = self.inverse_kine(px, py, configuration)
        print("\nq = ", q)
        self.print_end_effector_Tm_from_q(q)

    def inverse_kine(self, px: float, py: float, configuration: int) -> Annotated[NDArray[np.float64], (3,)]:
        """Inverse kinematics solution for the three axis planar articulated robot.

        Inputs are the end-effector x- and y-coordinates (position),
        and the configuration number (1 = Shoulder up, 2 = Shoulder down). 
        Output is the array of angles in radians.
        Equations 3-7-2, 3-7-4, 3-7-7 and 3-7-8 obtained from:
        Schilling, R.J. (1990) Fundamentals of Robotics Analysis and Control.
        Englewood Cliffs: Prentice-Hall, Inc.
        """

        # Convenience array access indexes.
        i1 = 0
        i3 = 2

        # Get robot parameters.

        # Robot link lengths (mm).
        a1 = self.model.jointPlacements[self.j2_id].translation[i1]
        a2 = self.model.jointPlacements[self.j3_id].translation[i1]

        # Get transform elements.

        # Equation 3-7-2 extract. Context given in section 3-7-4.
        w1 = px
        w2 = py
        w6 = self.data.oMf[self.ee_frame_id].rotation[i3, i3] # R33

        # Calculate q1, q2, q3

        # Equation 3-7-4.
        q2 = math.acos((math.pow(w1, 2) + math.pow(w2, 2) - math.pow(a1, 2) - math.pow(a2, 2)) / (2 * a1 * a2)) # (rad).

        #if configuration is 1:
            # q2 unchanged # Shoulder up.
        if configuration == 2:
            q2 = - q2 # Shoulder down.

        C2 = math.cos(q2)
        S2 = math.sin(q2)

        # Equation 3-7-7.
        q1 = math.atan2(((a1 + (a2 * C2)) * w2) - (a2 * S2 * w1), ((a1 + (a2 * C2)) * w1) + (a2 * S2 * w2)) # (rad).

        # Equation 3-7-8.
        q3 = math.pi * math.log(w6) # (rad).

        q_output = np.array([q1, q2, q3])

        return q_output
