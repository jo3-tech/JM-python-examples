# Copyright (C) 2026 Joseph Morgridge
#
# Licensed under MIT License.
# See the LICENSE file in the project root for full license details.

"""
Robot Model class.

Class that handles creation of the robot model and it's operations.
"""

import pinocchio as pin
import numpy as np

def verify_pinocchio():
    """Verify Pinocchio library is installed."""
    print(pin.__file__)
    print(dir(pin))
    print(hasattr(pin, 'Model'))
    print(pin.Model)

class RRRPlanarRobot():
    """The RRR Planar Robot class"""

    def __init__(self, link1_length, link2_length, link3_length):
        print("Creating robot model.\n")
        self.model = pin.Model()

        # Joint 1: Revolute about y-axis at origin.
        j1_parent_id = self.model.getJointId('universe')
        j1_model = pin.JointModelRY()
        j1_placement = pin.SE3.Identity()
        j1_id = self.model.addJoint(j1_parent_id, j1_model, j1_placement, 'joint1')

        # Joint 2: Revolute about y-axis at end of link 1.
        j2_parent_id = j1_id
        j2_model = pin.JointModelRY()
        j2_placement = pin.SE3(np.eye(3), np.array([link1_length, 0.0, 0.0]))
        j2_id = self.model.addJoint(j2_parent_id, j2_model, j2_placement, 'joint2')

        # Joint 3: Revolute about y-axis at end of link 2.
        j3_parent_id = j2_id
        j3_model = pin.JointModelRY()
        j3_placement = pin.SE3(np.eye(3), np.array([link2_length, 0.0, 0.0]))
        j3_id = self.model.addJoint(j3_parent_id, j3_model, j3_placement, 'joint3')

        # End-effector frame at end of link 3.
        ee_parent_id = j3_id
        ee_placement = pin.SE3(np.eye(3), np.array([link3_length, 0.0, 0.0])) # pin.SE3(np.eye(3), np.zeros(3)) OR pin.SE3.Identity() if link3_length = 0 i.e., at joint 3 origin.
        ee_frame_type = pin.FrameType.OP_FRAME
        ee_frame_id = pin.Frame('end_effector', ee_parent_id, 0, ee_placement, ee_frame_type)
        self.model.addFrame(ee_frame_id)

        self.data = self.model.createData()


    def print_from_robot(self) -> None :
        """Test class method"""
        print("Hello from robot model")
