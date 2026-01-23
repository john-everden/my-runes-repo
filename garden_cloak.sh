#!/bin/bash
# ≋ The Phalanx: Emergency Stealth Protocol

if [ "$1" == "dark" ]; then
    echo "--- [COLLAPSING THE GATE] Entering Stealth Mode ---"
    sudo systemctl stop garden-receiver.service
    sudo ufw deny 5000/tcp
    echo "[STATUS] Corunna-Node is now DARK."
    
elif [ "$1" == "light" ]; then
    echo "--- [RESTORING THE BRIDGE] Re-opening the Gilded Gate ---"
    sudo ufw allow 5000/tcp
    sudo systemctl start garden-receiver.service
    echo "[STATUS] Corunna-Node is now VISIBLE."
    
else
    echo "Usage: ./garden_cloak.sh [dark|light]"
fi
