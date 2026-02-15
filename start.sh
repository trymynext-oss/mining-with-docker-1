#!/bin/bash
echo "[*] Initializing Solana Brute Force Automation..."
pip install flask solana bip39 solders
echo "[*] Starting Flask Server on Port 347..."
python3 app.py
