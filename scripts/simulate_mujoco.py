#!/usr/bin/env python3
"""
===============================================================================
FIGURE OMNIHAND // MUJOCO 3.x PHYSICS SIMULATION LAUNCHER
===============================================================================
Launches the native MuJoCo interactive viewer for kinematics & contact dynamics.
"""

import os
import sys

def main():
    try:
        import mujoco
        import mujoco.viewer
    except ImportError:
        print("[!] MuJoCo is not installed in your current Python environment.")
        print("    Install it via: pip install mujoco")
        sys.exit(1)

    model_dir = os.path.join(os.path.dirname(__file__), "..", "models")
    xml_path = os.path.abspath(os.path.join(model_dir, "omnihand.xml"))

    if not os.path.exists(xml_path):
        print(f"[!] Model file not found: {xml_path}")
        sys.exit(1)

    print("=" * 70)
    print("  FIGURE AI // PROJECT TACTILE-V : MUJOCO SIMULATION")
    print(f"  Loading: {xml_path}")
    print("=" * 70)

    model = mujoco.MjModel.from_xml_path(xml_path)
    data = mujoco.MjData(model)

    print(f"  Model Loaded Successfully:")
    print(f"  - Generalized Coordinates (nq): {model.nq}")
    print(f"  - Degrees of Freedom (nv):       {model.nv}")
    print(f"  - Active Actuators (nu):         {model.nu}")
    print(f"  - Rigid Bodies:                  {model.nbody}")
    print("=" * 70)
    print("  Launching interactive 3D physics viewer...")

    mujoco.viewer.launch(model, data)

if __name__ == "__main__":
    main()
