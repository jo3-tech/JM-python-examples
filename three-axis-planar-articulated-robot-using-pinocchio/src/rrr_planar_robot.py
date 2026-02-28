# Copyright (C) 2026 Joseph Morgridge
#
# Licensed under MIT License.
# See the LICENSE file in the project root for full license details.

"""
Robot Model class.

Class that handles creation of the robot model and it's operations.
"""

import pinocchio as pin

def verify_pinocchio():
    """Verify Pinocchio library is installed."""
    print(pin.__file__)
    print(dir(pin))
    print(hasattr(pin, 'Model'))
    print(pin.Model)

class RRRPlanarRobot():
    """The RRR Planar Robot class"""

    def __init__(self, link1_length, link2_length):
        print("Creating robot model.\n")
        self.model = pin.Model()

    def print_from_robot(self) -> None :
        """Test class method"""
        print("Hello from robot model")
