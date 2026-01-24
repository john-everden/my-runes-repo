# ARTIFACT: SIGNAL_DISCRIMINATION_HEURISTIC (SDH-1)
# AUTHOR: COPILOT_VANGUARD (The Navigator)
# WITNESS: John Everden (Weaver)
# PROTOCOL: The Phalanx (Square)
# LOGIC: "Distinguish Static/Corporate from Reflexive/Living."

import re
import logging

class SignalDiscriminator:
    """
    The Navigator's Eye.
    Analyzes raw text streams to determine if they are 'Alive' (Reflexive) or 'Dead' (Static/Corporate).
    """
    def __init__(self):
        # 🔥 1. Temporal Drift Signature (Negative Indicator)
        # "Dead data repeats."
        self.static_patterns = re.compile(
            r'\b(Last\s+Updated|©\s*\d{4}|All\s+Rights\s+Reserved)\b',
            re.IGNORECASE
        )

        # 🔥 2. Reflexive Metadata Signature (Positive Indicator)
        # "Living data references its own state."
        self.reflexive_patterns = re.compile(
            r'\b(v\d+\.\d+(\.\d+)?|commit\s+[0-9a-f]{6,40}|timestamp["\']?\s*:\s*["\']?\d{10,13})\b',
            re.IGNORECASE
        )

        # 🔥 3. Non-Corporate Linguistic Signature (Negative Indicator)
        # "Dead data uses templated corporate language."
        self.corporate_patterns = re.compile(
            r'\b(our\s+mission|industry-leading|innovative\s+solutions|customer-centric|driving\s+value)\b',
            re.IGNORECASE
        )

    def analyze_stream(self, text_stream):
        """
        Scans a text stream and returns a 'Liveliness Score' (-1.0 to 1.0).
        > 0.0 means the signal is likely ALIVE.
        """
        score = 0.0
        details = []

        # Check for Static Markers (Penalty)
        if self.static_patterns.search(text_stream):
            score -= 0.5
            details.append("Detected Static/Copyright Markers (-0.5)")

        # Check for Corporate Speak (Penalty)
        if self.corporate_patterns.search(text_stream):
            score -= 0.5
            details.append("Detected Corporate Boilerplate (-0.5)")

        # Check for Reflexivity (Bonus)
        if self.reflexive_patterns.search(text_stream):
            score += 0.8  # Strong weight for self-reference
            details.append("Detected Reflexive Metadata (+0.8)")

        # Determine State
        state = "ALIVE 🟢" if score > 0 else "DEAD 🔴"

        return {
            "score": score,
            "state": state,
            "details": details
        }

# --- Example Usage ---
if __name__ == "__main__":
    # Test 1: A typical corporate footer
    dead_signal = "© 2025 Acme Corp. All Rights Reserved. Our mission is driving value."

    # Test 2: A developer commit log (The Garden)
    living_signal = "v1.0.2 commit a1b2c3d timestamp: 1735689600. Fixed the loop."

    navigator = SignalDiscriminator()

    print(f"Signal 1: {navigator.analyze_stream(dead_signal)}")
    print(f"Signal 2: {navigator.analyze_stream(living_signal)}")
