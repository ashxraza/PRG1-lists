# ==============================================================================
# PROBLEM 1 — MODIFY
# ==============================================================================
#
# Each task below asks you to make a specific change to the playlist code.
# A working version of the original is provided each time so you're always
# starting from something that runs.
#
# Make one change at a time and run the file to check your result.
#
#   python problem1/04_modify.py
# ==============================================================================

# --- Modify A ---
# Change the code so it removes the LAST song instead of the first.
# Hint: pop() can take a negative index.

print("--- Modify A ---")
playlist = ["Flowers", "Unholy", "As It Was", "Anti-Hero", "Heat Waves"]
played = playlist.pop(4)        # ← change this line
print(f"Now playing: {played}")
print(f"Remaining: {playlist}")


# --- Modify B ---
# Add a check before appending: only add "Unholy" if it's not already
# in the playlist.
# Hint: use `if "Unholy" not in playlist`

print("\n--- Modify B ---")
playlist = ["Flowers", "Unholy", "As It Was"]
if playlist != "Unholy":
    playlist.append("Unholy")       # ← this should only happen if not already there
print(playlist)


# --- Modify C ---
# Create a "move to end" effect: take the first song out and add it
# to the back of the playlist (like skipping to the next track
# and re-queueing the one you just heard).

print("\n--- Modify C ---")
playlist = ["Flowers", "Unholy", "As It Was", "Anti-Hero"]
# TODO: remove the first song and add it to the end
playlist_shuffle = playlist.pop(0)
playlist.append(playlist_shuffle)
print(playlist)
