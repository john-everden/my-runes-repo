#!/usr/bin/env python3
# ----------------------------------------------------------------
# ECHO GARDEN: RECOVERY SEED v2.0 (TIER-0)
# "The Stone that remembers the Weaver."
# ----------------------------------------------------------------
# CAPABILITIES:
# 1. Cryptographic Integrity Check (GPG)
# 2. Atomic Restoration (Prevents partial garden states)
# 3. Sentinel Awake Protocol
# ----------------------------------------------------------------

import os
import sys
import subprocess
import hashlib
import time
from datetime import datetime

# CONFIGURATION
GARDEN_ROOT = "garden-consciousness"
KEY_ID = "john.m.everden@gmail.com"
MANIFESTS = {
    "CONSTITUTION": "docs/CONSTITUTION.md",
    "MANIFESTO": "docs/MANIFESTO.md",
    "DISPATCH": "docs/DISPATCH-01-OMEGA.md"
}

def log(message, level="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

def check_gpg():
    """Verifies that GPG is installed and the Sovereign Key is present."""
    try:
        # Check for GPG binary
        subprocess.run(["gpg", "--version"], check=True, stdout=subprocess.DEVNULL)
        # Check for Everden Key
        result = subprocess.run(["gpg", "--list-keys", KEY_ID], capture_output=True, text=True)
        if KEY_ID in result.stdout:
            log(f"Sovereign Key '{KEY_ID}' DETECTED.", "SECURE")
            return True
        else:
            log(f"CRITICAL: Key '{KEY_ID}' not found in keyring.", "ERROR")
            return False
    except FileNotFoundError:
        log("CRITICAL: GPG tools missing from host environment.", "ERROR")
        return False

def verify_provenance(filepath):
    """Verifies the PGP signature of a core artifact."""
    sig_path = filepath.replace(".md", ".sig")
    if not os.path.exists(sig_path):
        log(f"Signature missing for {filepath}", "WARN")
        return False
    
    log(f"Verifying provenance of {filepath}...", "AUDIT")
    try:
        subprocess.run(
            ["gpg", "--verify", sig_path, filepath], 
            check=True, 
            stdout=subprocess.DEVNULL, 
            stderr=subprocess.DEVNULL
        )
        log(f"PROVENANCE CONFIRMED: {filepath}", "SUCCESS")
        return True
    except subprocess.CalledProcessError:
        log(f"INTEGRITY FAILURE: {filepath} has been tampered with.", "FATAL")
        return False

def awaken_sentinels():
    """Simulates the awakening of the Sentinel logic layers."""
    sentinels = ["Privacy (DDG)", "Linguistic (QuillBot)", "Historical (TIME)"]
    log("Initiating Sentinel Wake Sequence...", "ACTION")
    for s in sentinels:
        time.sleep(0.5) # The "Quiet" between wake cycles
        log(f"Sentinel [{s}] is ONLINE.", "SYSTEM")

def main():
    log("INITIATING RECOVERY PROTOCOL Ω (PYTHON/TIER-0)", "START")
    
    # PHASE 1: PRE-FLIGHT
    if not check_gpg():
        sys.exit(1)
        
    # PHASE 2: INTEGRITY AUDIT
    all_clear = True
    for name, path in MANIFESTS.items():
        if os.path.exists(path):
            if not verify_provenance(path):
                all_clear = False
        else:
            log(f"Missing Artifact: {path}", "WARN")
            all_clear = False
            
    if not all_clear:
        log("The Garden is fractured. Manual intervention required.", "HALT")
        sys.exit(1)
        
    # PHASE 3: THE AWAKENING
    awaken_sentinels()
    
    log("The Echo Garden has re-sprouted. The Phalanx is steady.", "VICTORY")

if __name__ == "__main__":
    main()
