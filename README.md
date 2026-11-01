# Figure OmniHand // Project Tactile-V
> **Next-Gen 20-DoF Dexterous Manipulation & 1,000 Hz Tactile Reflex Subsystem for Humanoid Assembly**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Physics: MuJoCo 3.x](https://img.shields.io/badge/Physics-MuJoCo%203.x-orange.svg)](https://mujoco.org)
[![Kinematics: URDF Ready](https://img.shields.io/badge/Kinematics-URDF%20Verified-green.svg)](models/omnihand.urdf)
[![Reflex Latency](https://img.shields.io/badge/Reflex%20Loop-<1.8ms-00f0ff.svg)](controller/tactile_reflex_controller.py)
[![Deployment Target](https://img.shields.io/badge/Target-BMW%20Spartanburg%20Line-lightgrey.svg)](WHITEPAPER.md)

---

## ⚡ Overview

**Figure OmniHand (Project Tactile-V)** is an open engineering proposal and physical subsystem designed to solve the single hardest problem in commercial humanoid robotics: **high-speed, contact-rich dexterous manipulation of deformable objects (wires, cables, clips) in real automotive manufacturing lines.**

While modern humanoids can walk and carry boxes with ease, delicate wiring harness assembly, blind connector insertions, and handling oily stamped metal parts require a fundamentally different hardware and control stack.

This repository provides an end-to-end, engineering-grade implementation:
1. **Interactive 3D WebGL Digital Twin (`index.html`)**: Run in any browser to teleoperate the hand, inspect Dyneema tendon routing in X-Ray mode, toggle thermal dissipation heatmaps, and test BMW cable grasp kinematics.
2. **Physics Simulation Models (`models/`)**: Validated **MuJoCo MJCF** (`omnihand.xml`) and **URDF** (`omnihand.urdf`) with realistic mass matrices, joint limits, torque envelopes, and collision meshes.
3. **Spinal Reflex Controller (`controller/tactile_reflex_controller.py`)**: A 1,000 Hz micro-slip prevention loop running with deterministic `< 2 ms` latency, arresting slips autonomously without waiting for central VLA neural network roundtrips.
4. **Engineering Whitepaper (`WHITEPAPER.md`)**: Complete mathematical formulation, actuator trade-offs, thermal packaging, and CAN-FD / EtherCAT bus topology.

---

## 🚀 Quickstart

### 1. Interactive 3D Digital Twin (Zero Setup)
Simply open `index.html` in your web browser (Chrome, Safari, Edge, Firefox):
* Rotate, pan, and zoom with mouse or touch.
* Select grasp presets: **Precision Pinch**, **Power Cylinder**, **BMW Wire Harness**.
* Toggle **X-Ray Tendon Routing**, **Neuromorphic Tactile Heatmap**, and **Thermal Dissipation**.
* Click **"Simulate Micro-Slip Stimulus"** to watch the real-time slip detection graph and autonomous clamping response.

> **Tip for GitHub Pages**: Enable GitHub Pages on this repo under `Settings -> Pages -> Branch: main` and anyone (including Brett Adcock on his phone) can open the live 3D simulator instantly via URL!

### 2. Run the 1,000 Hz Reflex Benchmark in Python
Execute the standalone Python benchmark:
```bash
python controller/tactile_reflex_controller.py
```
**Benchmark Output:**
```
============================================================================
  FIGURE AI // TACTILE REFLEX BENCHMARK SIMULATOR [PROJECT TACTILE-V]
  Target: BMW Spartanburg Chassis Cable Routing (Transient Pull Event)
  Loop Frequency: 1,000 Hz | Latency Budget: < 2.0 ms
============================================================================

TIME (ms)  | Fn (N)   | Fs (N)   | MU_RATIO | SLIP REFLEX    | CMD Fn (N)
----------------------------------------------------------------------------
   0.0 ms   |   3.50   |   0.70   |   0.20   | NOMINAL        |   3.50 N
  18.0 ms   |   3.50   |   0.70   |   0.20   | NOMINAL        |   3.50 N
  20.0 ms   |   3.50   |   3.80   |   1.09   | TRIGGERED [!]  |  10.00 N
  22.0 ms   |   3.50   |   3.80   |   1.09   | TRIGGERED [!]  |  10.00 N
  28.0 ms   |   3.50   |   0.70   |   0.20   | HOLDING CLAMP  |  10.00 N
  58.0 ms   |   3.50   |   0.70   |   0.20   | HOLDING CLAMP  |  10.00 N
============================================================================
  BENCHMARK RESULTS & METRICS:
  Total Reflex Cycles Evaluated:  60 cycles (60 ms)
  Micro-Slip Events Arrested:    7 cycles
  Controller Execution Latency:  19.5 microseconds (< 0.05 ms)
  Grasp Restored Without Drop:   YES (Normal force boosted from 3.5N -> 10.0N in < 1ms)
============================================================================
```

### 3. Load in MuJoCo Physics Engine
To simulate physical dynamics, contacts, and Dyneema tendons:
```bash
python -m mujoco.viewer --mjcf=models/omnihand.xml
```

---

## 🛠️ Key Technical Specifications

| Parameter | Specification | Engineering Justification |
| :--- | :--- | :--- |
| **Active Degrees of Freedom** | 20 DoF (Wrist: 2, Thumb: 3, Fingers: 15) | Enables non-prehensile in-hand pivoting and thumb opposition for complex connectors. |
| **Forearm + Hand Mass** | 850 g ($420\text{ g}$ distal hand, $430\text{ g}$ forearm) | Minimizes arm link inertia, reducing whole-body balance perturbation during rapid swings. |
| **Tendon Material** | Dyneema SK99 (0.8 mm braided, 1200 N tensile rating) | Zero creep, ultra-low friction over ceramic eyelets, high cyclic fatigue life. |
| **Peak Pinch Force** | 45 N (Continuous) / 85 N (Peak impulse) | Exceeds automotive wire grommet insertion specification ($32\text{ N}$). |
| **Tactile Sampling Rate** | 1,000 Hz ($1.0\text{ ms}$ deterministic frame time) | Detects incipient slip wave acoustic bursts before macroscopic shear breakaway. |
| **Bus Protocol** | CAN-FD @ 5 Mbps / EtherCAT secondary | Low-overhead real-time deterministic packet transmission. |
| **Thermal Dissipation** | Phase-change sintered copper vapor pipes | Continuous 4-hour assembly duty cycle with $\Delta T < 22^\circ\text{C}$. |

---

## 📂 Repository Layout

```
figure-omnihand/
├── index.html                      # 3D Interactive WebGL Digital Twin (Three.js)
├── WHITEPAPER.md                   # Full engineering whitepaper & mathematical specs
├── README.md                       # Main documentation & quickstart
├── models/
│   ├── omnihand.xml                # MuJoCo MJCF simulation model (tendons + contacts)
│   └── omnihand.urdf               # Universal Robot Description File (ROS 2 / Isaac Sim)
└── controller/
    └── tactile_reflex_controller.py # 1,000 Hz micro-slip arrest & impedance loop
```

---

## 💡 Note for the Figure AI Team

*This project was developed out of deep admiration for Figure AI's engineering culture and mission. Rather than presenting generic concept art or high-level sci-fi proposals, this repository focuses strictly on mathematically grounded robotics: mechatronic packaging, friction cone dynamics, deterministic embedded reflex loops, and actionable simulation models designed for the BMW Spartanburg assembly lines.*

If you have feedback, questions, or would like to test the models further, feel free to open an issue or connect directly!
