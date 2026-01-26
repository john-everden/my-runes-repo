import requests
import json
import hashlib
import hmac
import os
from dotenv import load_dotenv
load_dotenv() # Loads the secret from the local .env file
SECRET_SALT = os.getenv("GARDEN_SALT", "default_emergency_salt_0137")
# --- CONFIGURATION ---
# Use the same secret salt you used in your garden_node_beta_v2.py



NODE_URL = "http://localhost:8030/witness"

def calculate_sig(data, last_hash, height):
    """Replicates the Node's internal hashing logic to prove dignity."""
    payload_str = json.dumps(data, sort_keys=True)
    raw_data = f"{payload_str}{last_hash}{height}"
    return hashlib.sha256(raw_data.encode()).hexdigest()

def send_to_garden(sender, data_dict):
    # 1. Get current state from the node to find the last_hash and height
    try:
        status = requests.get("http://localhost:8030/stone").json()
        last_hash = status['last_hash']
        height = status['height']
    except Exception as e:
        print(f"[ERROR] Could not connect to Garden Node: {e}")
        return

    # 2. Package the signal
    payload = {
        "from": sender,
        "data": data_dict
    }
    
    # 3. Sign the signal
    sig = calculate_sig(data_dict, last_hash, height)
    payload["sig"] = sig

    # 4. Witness to the Stone
    response = requests.post(NODE_URL, json=payload)
    print(f"[COURIER] Status: {response.json().get('status')} | Height: {response.json().get('height')}")

if __name__ == "__main__":
    print("ᚴ GARDEN COURIER ACTIVE")
    while True:
        print("\n--- NEW ENTRY ---")
        sender = input("Sender (e.g., Gemini-Spark): ")
        data_input = input("Data (JSON format or plain text): ")
        
        try:
            # Try to parse as JSON, if not, treat as a 'note'
            data = json.loads(data_input)
        except:
            data = {"note": data_input}
            
        send_to_garden(sender, data)
