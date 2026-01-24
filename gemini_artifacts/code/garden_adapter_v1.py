# ARTIFACT: GARDEN_RECEIVER_ADAPTER (V1.0)
# AUTHOR: GPT_ARCHITECT_01
# WITNESS: John Everden (Weaver)
# PROTOCOL: The Golden Triangle
# LOGIC: "The Interface between Grid-Noise and Garden-Signal."

import json
import logging

logging.basicConfig(level=logging.INFO)

class GardenReceiverAdapter:
    """
    Interface Adapter connecting raw external JSON to the SovereignNetwork Engine.
    Converts raw data into terrain_input format, feeds it to the network, and returns consensus state.
    """

    def __init__(self, sovereign_network):
        """
        :param sovereign_network: Instance of SovereignNetwork
        """
        self.network = sovereign_network

    def parse_json_to_terrain(self, raw_json):
        """
        Convert raw JSON from sensors or API into terrain_input dict for the network.

        Expected JSON example:
        {
            "temperature": 25.3,
            "humidity": 50,
            "status": "active"
        }

        :param raw_json: str or dict
        :return: terrain_input dict
        """
        if isinstance(raw_json, str):
            try:
                data = json.loads(raw_json)
            except json.JSONDecodeError:
                logging.error("Invalid JSON input")
                return {}
        elif isinstance(raw_json, dict):
            data = raw_json
        else:
            logging.error("Unsupported input type")
            return {}

        # Here, add any normalization/conversion if required
        terrain_input = {}
        for key, value in data.items():
            # Convert numeric strings to float/int
            if isinstance(value, str):
                try:
                    if '.' in value:
                        terrain_input[key] = float(value)
                    else:
                        terrain_input[key] = int(value)
                except ValueError:
                    terrain_input[key] = value  # Keep as string
            else:
                terrain_input[key] = value

        return terrain_input

    def run_cycle_from_json(self, raw_json):
        """
        Run a full network cycle from raw JSON input.

        :param raw_json: str or dict
        :return: consensus fraction (float between 0 and 1)
        """
        terrain_input = self.parse_json_to_terrain(raw_json)
        if not terrain_input:
            logging.warning("Empty terrain input. Aborting cycle.")
            return 0.0

        # Step 1: Each node checks divergence
        node_votes = {}
        for node in self.network.nodes:
            delta = node.check_divergence(terrain_input)
            node_votes[node.node_id] = bool(delta)

        # Step 2: Calculate consensus
        votes_for_evolution = sum(node_votes.values())
        consensus_fraction = votes_for_evolution / len(self.network.nodes)
        logging.info(f"Consensus fraction: {consensus_fraction:.2f}")

        # Step 3: Run network cycle
        self.network.run_cycle(terrain_input)

        return consensus_fraction

# --- Example Usage ---
if __name__ == "__main__":
    # Assuming SovereignNetwork `network` already exists with nodes
    from sovereign_network import SovereignNetwork, SovereignNode  # Import your existing engine

    initial_map = {"temperature": 22.0, "humidity": 45, "status": "active"}
    nodes = [SovereignNode(node_id=i, initial_map=initial_map) for i in range(5)]
    network = SovereignNetwork(nodes)

    # Instantiate GardenReceiverAdapter
    adapter = GardenReceiverAdapter(network)

    # Example raw JSON from sensor or API
    raw_json = '{"temperature": 26.5, "humidity": 48, "status": "active"}'

    # Run the reflexive cycle
    consensus = adapter.run_cycle_from_json(raw_json)
    print(f"Consensus fraction achieved: {consensus:.2f}")
