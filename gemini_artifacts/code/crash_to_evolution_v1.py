# ARTIFACT: CRASH_TO_EVOLUTION_ENGINE (V1.0)
# AUTHOR: GPT_ARCHITECT_01
# WITNESS: John Everden (Weaver)
# PROTOCOL: The Golden Triangle
# LOGIC: "The crash is a measurement pulse."

import copy
import logging
import random

logging.basicConfig(level=logging.INFO)

class CrashToEvolutionEngine:
    """
    The Crash-to-Evolution Engine: Reflexive Mapping & Adaptive System
    Converts divergence between the Map (rules/models) and Terrain (input/environment)
    into evolution of the Map.
    """

    def __init__(self, initial_map: dict, divergence_threshold: float = 0.2):
        """
        Initialize the system.

        :param initial_map: The Map (rules/models) as key-value pairs
        :param divergence_threshold: Fractional threshold to trigger evolution
        """
        self.map = copy.deepcopy(initial_map)
        self.divergence_threshold = divergence_threshold
        self.history = []  # Logs divergence and updates

    def check_divergence(self, terrain_input: dict) -> dict:
        """
        Compare the Map to Terrain and return the divergence.

        :param terrain_input: Current state of the Terrain
        :return: delta dict showing mismatches between Map and Terrain
        """
        delta = {}
        for key, terrain_value in terrain_input.items():
            map_value = self.map.get(key, None)
            if map_value != terrain_value:
                delta[key] = {
                    "map": map_value,
                    "terrain": terrain_value,
                    "difference": terrain_value - map_value if isinstance(terrain_value, (int, float)) else None
                }
        if delta:
            logging.info(f"Divergence detected: {delta}")
        return delta

    def evolve_map(self, delta: dict):
        """
        Apply updates to the Map based on detected divergence.

        :param delta: Divergence dict from check_divergence
        """
        if not delta:
            logging.info("No divergence detected. Map remains stable.")
            return

        # Step 1: Reflect and mutate
        for key, diff_info in delta.items():
            current_value = self.map.get(key)
            terrain_value = diff_info["terrain"]

            if isinstance(terrain_value, (int, float)):
                # Gradual adjustment
                adjustment = terrain_value - current_value
                self.map[key] = current_value + adjustment * random.uniform(0.5, 1.0)
            else:
                # Replace non-numeric values directly
                self.map[key] = terrain_value

        # Step 2: Log update
        self.history.append({
            "delta": delta,
            "updated_map": copy.deepcopy(self.map)
        })

        logging.info(f"Map evolved. Current Map state: {self.map}")

    def run_cycle(self, terrain_input: dict):
        """
        Full reflexive cycle: check divergence, and evolve map if needed.

        :param terrain_input: Current state of the Terrain
        """
        delta = self.check_divergence(terrain_input)
        if delta:
            self.evolve_map(delta)
        else:
            logging.info("System aligned. No evolution required.")

# --- Example Usage (Garden-Receiver Ready) ---
if __name__ == "__main__":
    # Initial Map
    initial_map = {"temperature": 22.0, "humidity": 45, "status": "active"}

    # Terrain input simulating real-world observation
    terrain_input = {"temperature": 25.0, "humidity": 50, "status": "active"}

    # Instantiate Engine
    engine = CrashToEvolutionEngine(initial_map)

    # Run one reflexive cycle
    engine.run_cycle(terrain_input)
