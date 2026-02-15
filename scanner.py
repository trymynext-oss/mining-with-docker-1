import bip39
from solana.rpc.api import Client
from solders.keypair import Keypair
import threading
import json
import time

# Configuration
RPC_URL = "https://api.mainnet-beta.solana.com"
client = Client(RPC_URL)
stats = {"checked": 0, "found": 0, "last_address": ""}

def brute_force():
    global stats
    while True:
        mnemonic = bip39.generate_mnemonic(12)
        seed = bip39.mnemonic_to_seed(mnemonic)
        # Standard Solana path derivation
        kp = Keypair.from_seed(seed[:32]) 
        pubkey = str(kp.pubkey())
        
        try:
            balance = client.get_balance(kp.pubkey()).value
            stats["checked"] += 1
            stats["last_address"] = pubkey
            
            if balance > 0:
                stats["found"] += 1
                with open("found.txt", "a") as f:
                    f.write(f"Mnemonic: {mnemonic} | Addr: {pubkey} | Bal: {balance}\n")
        except:
            time.sleep(1) # Anti-rate limit

def start_threads(count=4):
    for _ in range(count):
        threading.Thread(target=brute_force, daemon=True).start()
