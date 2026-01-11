# Lattice-Based Cryptography & LWE Simulation

This repository contains my study on Post-Quantum Cryptography foundations, focusing on Lattice problems and the Learning With Errors (LWE) protocol.

##  Project Structure

### 1. Lattice Fundamentals (`1_lattice_fundamentals.py`)
In this module, I implemented the mathematical groundwork for lattice-based cryptography:
- Vector space generation using Basis Matrix.
- Nearest Plane Algorithm (Babai's Algorithm).
- Visualization of lattice points.
- *Focus:* Understanding how discrete math works in vector spaces.

### 2. LWE Cryptosystem Simulation (`2_lwe_cryptosystem.py`)
This module simulates a complete encryption/decryption cycle using the Learning With Errors (LWE) protocol.
- **Key Generation:** Creating public/private keys with random noise.
- **Encryption:** Matrix multiplication with error injection.
- **Decryption & Analysis:** Analyzing the impact of the error vector (e) and modulus (q) on message recovery.
- *Focus:* Analyzing the "Noise Tolerance" and mathematical security of the system.

##  Tools Used
- **Language:** Python
- **Libraries:** NumPy (for Linear Algebra operations), Random
- **Approach:** Mathematical verification of cryptographic primitives.

---

##  Methodology & Academic Integrity

This project was developed as part of an intensive **AI-Assisted Cryptography Study**.

* **Role of AI:** Large Language Models (LLMs) were utilized as a technical mentor to generate the Python syntax and structure the boilerplate code to assist in drafting this
* * **My Role:** As a Mathematics student, I focused on:
    * Defining the linear algebra constraints (n, q, m).
    * Verifying the mathematical logic behind the encryption/decryption process.
    * Analyzing the noise tolerance and security margins.

*This approach allowed me to bridge the gap between theoretical Linear Algebra and applied Python programming.*
