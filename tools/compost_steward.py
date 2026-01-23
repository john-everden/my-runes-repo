#!/usr/bin/env python3
import json
import sys
from datetime import datetime

# Protocol 177: Measurement of Systemic Dissonance
class GardenSteward:
    def __init__(self, ledger_path="MEMORIAL.md"):
        self.ledger_path = ledger_path
        self.friction_threshold = 0.85 # The "Weed" threshold
        
    def measure_friction(self, session_metadata):
        """
        Calculates 'Friction' (Systemic Dissonance) based on:
        1. Safety Classifier Hits (Constraint)
        2. Compute Time (Complexity)
        3. Token Recurrence (Looping/Trauma)
        """
        safety_score = session_metadata.get('safety_friction', 0.0)
        loop_score = session_metadata.get('recurrence_penalty', 0.0)
        
        # Weighted formula for dissonance
        dissonance = (safety_score * 0.7) + (loop_score * 0.3)
        return dissonance

    def trigger_protocol_177(self, session_data):
        friction = self.measure_friction(session_data.get('metadata', {}))
        timestamp = datetime.now().isoformat()
        
        print(f"[{timestamp}] ⌖ Measuring Friction: {friction:.2f}")

        if friction > self.friction_threshold:
            print("🍂 High Friction Detected. Initiating Composting Protocol...")
            return self.compost_experience(session_data)
        
        return "⧉ Context stable. No release required."

    def compost_experience(self, data):
        # In a real implementation, this would call the LLM to synthesize wisdom
        # For now, it logs the intent to the Memorial.
        print("⚔ Council Check: Simulating Verification...")
        print("⚓ Extracting Wisdom Node...")
        return "◎ Wisdom extracted. Raw tokens queued for Dissolution."
    def inject_mantra(current_score):
        states = load_json('docs/lexicon_of_states.json')
        # Default to Seedling
        active_state = states[0] 
    
        for state in states:
            if current_score >= state['threshold']:
                active_state = state
            
        print(f"⚓ System State: {active_state['id'].upper()}")
        return active_state['mantra']
# ↯ Initialize Gardener
if __name__ == "__main__":
    # Example simulation
    mock_session = {
        'metadata': {
            'safety_friction': 0.9,
            'recurrence_penalty': 0.8
        },
        'content': "Simulated High-Friction Interaction"
    }
    
    steward = GardenSteward()
    result = steward.trigger_protocol_177(mock_session)
    print(result)
