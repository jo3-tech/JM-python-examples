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
    link3_length_mm = 0.0

    # Robot configurations in radians (rad).
    # Zero position.
    zero_q_rad = np.array([0, 0, 0])
    # Soft home position.
    #                                 [  60,         60,      0]    (deg).
    soft_home_q_rad = np.array([math.pi/3, -math.pi/3, 0]) # (rad).

    # The robots kinematic/dynamic model.
    robot = rrr_planar_robot.RRRPlanarRobot(link1_length_mm, link2_length_mm, link3_length_mm)

    print("\n...Three axis articulated robot...\n\n")

    # Display the robot joint placements.
    print("...Robot joint placements...\n")
    robot.print_joint_placements()

    # Display the robot pose/transformation matrix for the zero position.
    print("...End-effector transformation matrix in the zero position...")
    robot.print_end_effector_Tm(zero_q_rad)

if __name__ == "__main__":
    main()
