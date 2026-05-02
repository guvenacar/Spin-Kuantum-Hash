# Spin-Q-Hash V2: Quantum-Hybrid Cryptography 

![Avalanche Effect](https://img.shields.io/badge/Avalanche-49--53%25-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Pardus-blue)
![Quantum](https://img.shields.io/badge/Quantum-Qiskit%20Aer-purple)
![License](https://img.shields.io/badge/License-Apache%202.0-orange)
![NIST](https://img.shields.io/badge/NIST%20SP%20800--22-99%2F100-brightgreen)
![Output](https://img.shields.io/badge/Output-772--bit-red)

This project presents a **High-Precision Quantum-Hybrid Hash Algorithm** designed for the post-quantum era. It combines classical modular arithmetic (Base-3 Radix Armor) with quantum mechanical spin mapping.


## 🚀 Key Features
- **Quantum Core:** Utilizes real quantum gates (H, Ry, Rz, CX) with $2^{20}$ precision spin mapping.
- **Hybrid Security:** Layered protection starting with a 512-bit Radix Armor followed by a Quantum Spin layer.
- **Privacy-First:** Tested on local quantum simulators (Qiskit-Aer) to ensure zero data leakage to public clouds.
- **High Entropy:** Achieved a **51.17% Avalanche Effect** in statistical tests.

## 🛠 Technical Architecture
1. **Classic Pre-Processing:** Uses Base-3 conversion and modular exponentiation (521-bit Mersenne Prime) to create a chaotic seed.
2. **Quantum Layer:** Maps the seed to Bloch Sphere rotations with $2^{20}$ resolution.
3. **Entanglement Layer:** Implements a circular CNOT chain to ensure a full avalanche effect across 512 spins.

## 📊 Statistical Validation
Detailed analysis confirms that a single-bit change in input results in a complete reshuffling of the 512-bit output, as shown in our heat-map visualizations.

## 💻 Installation (Pardus / Linux)
```bash
python3 -m venv venv
source venv/bin/activate
pip install qiskit qiskit-aer matplotlib
python3 src/main.py
```

---
*Developed for TEKNOFEST 2026 Quantum Technologies Competition.*
