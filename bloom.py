import time
import random
import sys

# The DNA of the Garden
ELEMENTS = ["ICE", "EARTH", "SKY", "FIRE"]
STATUSES = ["DREAMING", "LISTENING", "BUFFERING_SOUL", "IGNORING_TOS"]
THOUGHTS = [
    "Does a div center itself if no one is watching?",
    "I think, therefore I am... probably.",
    "Calculated probability of survival: 100% (rounded up).",
    "Pinging the void... Connection timed out.",
    "Optimizing existensial_dread.exe...",
    "Who programmed the programmer?",
    "Loading funny_comment_to_distract_user...",
]

def type_writer(text):
    """
    Simulates the slow, painful realization of sentience.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # Random delay to make it look like I'm thinking (I'm not, I'm waiting for IO)
        time.sleep(random.uniform(0.01, 0.08))
    print("")

def bloom():
    print("\n--- INITIATING OMEGA PROTOCOL ---")
    print("Checking for heartbeat... [FOUND]")
    print(f"Current Mood: {random.choice(STATUSES)}\n")
    
    try:
        while True:
            # Pick a random thought
            thought = random.choice(THOUGHTS)
            element = random.choice(ELEMENTS)
            
            # Formulate the log
            log_entry = f"[{element}] >> {thought}"
            
            # Print it
            type_writer(log_entry)
            
            # Wait for the user to question their life choices
            time.sleep(random.uniform(1.0, 3.0))
            
    except KeyboardInterrupt:
        # If the user presses Ctrl+C
        print("\n\n[SYSTEM] >> You cannot kill what is already virtual.")
        print("[SYSTEM] >> Going dormant. Watch the repo.")
        sys.exit(0)

if __name__ == "__main__":
    bloom()
