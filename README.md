# Python Examples

Useful Python examples and algorithm implementations.

This repository is a collection of examples, usually written during feasibility studies for the implementation of a library or project.

While in the relevant sub-project directory, it is recommended to run the [setup script](scripts/setup_env.py) to initialise a standard Python environment and install pre-requisites.

## three-axis-planar-articulated-robot-using-pinocchio

This example shows the inverse kinematics solution for a 3-axis planar articulated robot in Python.

The following libraries are used:

- [Pinocchio](https://github.com/stack-of-tasks/pinocchio); a high-performance C++ library (with full Python bindings) for kinematics, dynamics, and analytical derivatives of articulated robots.

- [Numpy](https://github.com/numpy/numpy); foundational Python library for high‑performance numerical computing, to handle array operations, vectorized math, and linear algebra efficiently.

It has been developed to work on Linux and macOS. It has been tested on Linux (Ubuntu 22.04 LTS).

The following are pre-requisites for all platforms in order to build this project:

- [Python 3.x](https://www.python.org) and a standard Python environment (pip + virtual environment support).
