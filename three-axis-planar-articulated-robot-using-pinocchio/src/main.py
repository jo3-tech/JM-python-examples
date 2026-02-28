# Copyright (C) 2026 Joseph Morgridge
#
# Licensed under MIT License.
# See the LICENSE file in the project root for full license details.

"""
Main application entry point.

Initialises the program and starts the top level application control flow.
"""

import rrr_planar_robot

def main():
    """The main application entry point that starts the application."""

    print("hello")
    print("\n")
    rrr_planar_robot.verify_pinocchio()
    link1_length_mm = 150
    link2_length_mm = 100
    robot = rrr_planar_robot.RRRPlanarRobot(link1_length_mm, link2_length_mm)
    robot.print_from_robot()

if __name__ == "__main__":
    main()
