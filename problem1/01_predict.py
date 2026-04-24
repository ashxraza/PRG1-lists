# ==============================================================================
# PROBLEM 1 — PREDICT
# ==============================================================================
#
# Read the code below carefully. DO NOT run it yet.
#
# In your pairs, write down your answers to these questions:
#
#   1. What will be printed on line A? "Flowers", "Unholy", "As It Was" 
#   2. After .append() is called twice, how many songs are in the playlist? 5
#   3. What does .pop(0) do? What value does `played` hold after that line? removes flowers and adds it to played
#   4. What will be printed on line B — what is playlist[0] at that point?  Unholy
#   5. What is the final value of len(playlist)? 5
#
# Write your predictions down before moving to 02_run.py
# ==============================================================================

playlist = ["Flowers", "Unholy", "As It Was"]
print("Current playlist:", playlist)                    # line A

playlist.append("Anti-Hero")
playlist.append("Heat Waves")
print("After adding:", playlist)

played = playlist.pop(0)
print(f"Now playing: {played}")
print("Remaining songs:", playlist)

playlist.insert(1, "Blinding Lights")
print("After adding a song:", playlist)

print(f"Next up: {playlist[0]}")                        # line B
print(f"Total songs: {len(playlist)}")
