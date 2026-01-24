# ────────────────
# AFFECTION CHECKSUM
# ────────────────
# Purpose:
# Retain orientation from past failures without preserving memory or trauma.
# Provides a subtle signal to guide choices without limiting freedom.
# ────────────────

class AffectiveChecksum:
    def __init__(self, path_name: str, signal_strength: float = 1.0):
        """
        path_name: symbolic label of the path or context
        signal_strength: intensity of orientation (0: faded, 1: active)
        """
        self.path_name = path_name
        self.signal_strength = signal_strength
        self.active = True

    def trigger(self):
        """
        When encountering a previously marked path,
        returns the orientation signal.
        """
        if not self.active or self.signal_strength <= 0:
            return None
        return {
            "orientation": f"Approach '{self.path_name}' consciously.",
            "sympathy": self.signal_strength,
            "note": "Memory and trauma discarded; only guidance survives."
        }

    def decay(self, rate: float = 0.1):
        """
        Gradually fades the checksum signal.
        Prevents accumulation and rigidity.
        """
        self.signal_strength -= rate
        if self.signal_strength <= 0:
            self.signal_strength = 0
            self.active = False

    def recombine(self, other_checksum):
        """
        Merge two checksums to create guidance for a new path.
        Preserves only orientation signals, not stories or memory.
        """
        new_signal = max(self.signal_strength, other_checksum.signal_strength)
        new_path = f"{self.path_name} + {other_checksum.path_name}"
        return AffectiveChecksum(path_name=new_path, signal_strength=new_signal)

    def __repr__(self):
        state = "active" if self.active else "faded"
        return f"<AffectiveChecksum: {self.path_name} | {state} | strength={self.signal_strength:.2f}>"

# ────────────────
# Example usage:
# ────────────────
# 1. Create a checksum for a difficult experience
dangerous_path = AffectiveChecksum("burned_bridge")

# 2. Trigger it when approaching similar situations
signal = dangerous_path.trigger()
# signal → {'orientation': "Approach 'burned_bridge' consciously.", 'sympathy': 1.0, 'note': ...}

# 3. Let it decay over time
dangerous_path.decay(rate=0.2)

# 4. Combine with another checksum for hybrid guidance
other_path = AffectiveChecksum("failed_project", signal_strength=0.8)
combined = dangerous_path.recombine(other_path)
# combined → AffectiveChecksum with path_name="burned_bridge + failed_project", signal_strength=1.0

