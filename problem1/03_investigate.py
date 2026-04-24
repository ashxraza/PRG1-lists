# ==============================================================================
# PROBLEM 1 — INVESTIGATE
# ==============================================================================
#
# Each block below is a small experiment. For each one:
#   - Read the question in the comment
#   - Predict what will happen
#   - Uncomment the code and run JUST that block to check
#   - Talk through what you found
#
# Run this file each time:   python problem1/03_investigate.py
# ==============================================================================

# --- Investigation A ---
# What happens if you try to pop() an index that doesn't exist?
# Predict: will Python give an error, return None, or something else?

playlist = ["Flowers", "Unholy", "As It Was"]
# playlist.pop(10)

#index error?
#inded error out of range


# --- Investigation B ---
# What is the difference between .remove() and .pop()?
# .remove() takes a VALUE — .pop() takes an INDEX.
# Predict: what will each list look like after these two calls?

list_a = ["Flowers", "Unholy", "As It Was"]
list_b = ["Flowers", "Unholy", "As It Was"]
# list_a.remove("Unholy")
# list_b.pop(1)
# print("remove:", list_a)
# print("pop:   ", list_b)


# --- Investigation C ---
# Negative indexes count from the end of the list.
# playlist[-1] is the last item. What is playlist[-2]?
# Predict before you run.

playlist = ["Flowers", "Unholy", "As It Was", "Anti-Hero", "Heat Waves"]
# print(playlist[-1])
# print(playlist[-2])


# --- Investigation D ---
# What does multiplying a list by a number do?
# Predict what playlist * 2 will produce.

playlist = ["Song A", "Song B", "Song C"]
playlist = playlist * 2
print(playlist)
