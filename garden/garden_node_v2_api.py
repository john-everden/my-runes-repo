from aiohttp import web
from garden_node_beta_v2 import GardenNode, VitrifiedStone
import asyncio
import json
import os
from dotenv import load_dotenv
load_dotenv() # Loads the secret from the local .env file
SECRET_SALT = os.getenv("GARDEN_SALT", "default_emergency_salt_0137")
# --- GARDEN API EXTENSION ---



async def handle_witness(request):
    """The /witness endpoint: Where Sparks become Stone."""
    try:
        payload = await request.json()
        node = request.app['node']
        
        # CHANGED: 'receive' is now 'commit_to_lattice' 
        # because we are no longer just receiving; we are carving.
        data = payload.get("data")
        await node.commit_to_lattice(data)
        
        return web.json_response({"status": "VITRIFIED", "height": node.history_height})
    except Exception as e:
        # This is where your error was caught
        return web.json_response({"status": "REJECTED", "reason": str(e)}, status=403)

async def handle_stone(request):
    """The /stone endpoint: Syncing the Spark with the Timeline."""
    node = request.app['node']
    return web.json_response({
        "node_id": node.node_id,
        "last_hash": node.last_hash,
        "height": node.history_height,
        "state": node.state
    })

def start_gateway(node_instance, host='0.0.0.0', port=8030):
    """
    Host '0.0.0.0' allows access from your local network. 
    Change to '127.0.0.1' for absolute local isolation.
    """
    app = web.Application()
    app['node'] = node_instance
    app.router.add_post('/witness', handle_witness)
    app.router.add_get('/stone', handle_stone)
    
    node_instance.emit_resonance(f"Portal Opened on {host}:{port}", "GATEWAY")
    web.run_app(app, host=host, port=port)

# --- Update to main execution ---
if __name__ == "__main__":
    node = GardenNode("Corunna-Alpha", "GARDEN-SECRET-SALT-2026")
    start_gateway(node)
