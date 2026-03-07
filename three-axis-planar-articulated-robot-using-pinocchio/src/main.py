# Copyright (C) 2026 Joseph Morgridge
#
# Licensed under MIT License.
# See the LICENSE file in the project root for full license details.

"""
Main application entry point.

Initialises the program and starts the top level application control flow.
"""

import math
import numpy as np
import rrr_planar_robot

def main():
    """The main application entry point that starts the application."""

    #rrr_planar_robot.verify_pinocchio()

    # Robot link lengths (mm).
    link1_length_mm = 150.0
    link2_length_mm = 100.0

    # Robot configurations in radians (rad).
    # Zero position.
    q_zero_rad = np.array([0, 0, 0])
    # Soft home position.
    #                          [  60,         60,      0]    (deg).
    q_soft_home_rad = np.array([math.pi/3, -math.pi/3, 0]) # (rad).

    # The robots kinematic/dynamic model.
    robot = rrr_planar_robot.RRRPlanarRobot(link1_length_mm, link2_length_mm)

    print("\n...Three axis articulated robot...\n\n")

    # Display the robot joint placements.
    print("...Robot joint placements...\n")
    robot.print_joint_placements()

    # Display the robot pose/transformation matrix for the zero position.
    print("...End-effector transformation matrix in the zero position...")
    robot.print_end_effector_Tm_from_q(q_zero_rad)

    # Display the robot pose/transformation matrix for the soft home position.
    print("...End-effector transformation matrix in the home position...")
    robot.print_end_effector_Tm_from_q(q_soft_home_rad)

    # Now, we want the robot to be in a position given by cartesian coordinates (px, py).
    px = 180.0 # The desired x-coordinate in mm.
    py = 160.0 # The desired y-coordinate in mm.

    # Display the joint angles and robot pose/transformation matrix for the new robot position.
    # This uses inverse kinematics to calculate the required joint angles.
    print("...Joint angles and end-effector transformation matrix in the new position...")
    configuration = 1 # Shoulder up.
    robot.print_end_effector_Tm_from_p(px, py, configuration)

    print("\n...Robot analysis complete...\n\n")

if __name__ == "__main__":
    main()
