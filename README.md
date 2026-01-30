# Experimental Study of AES Block Cipher Modes
## Overview

This project presents a case study of AES encryption in different modes of operation, specifically ECB and CBC, using Python. By comparing the insecure ECB mode and the secure CBC mode, it aims to 
demonstrate how patterns in plaintext can leak in ECB but stay hidden in other modes.

## Installation (Windows)

1. Open Command Prompt in the project directory.
2. Create and activate virtual environment:
```bash
python -m venv .venv.\.venv\Scripts\activate
```
3. Install dependencies in the environment:
```bash
pip install -r requirements.txt
```

## Run Experiments

To encrypt the pattern using ECB and CBC thus showing ECB information leakage in practice, run: 
```bash
python src\ecb_demo.py
```
To check if ECB and CBC encrypt and decrypt functions are implemented correctly, run:
```bash
python src\experiments.py
```
