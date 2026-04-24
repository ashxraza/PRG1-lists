# ==============================================================================
# PROBLEM 1 — MAKE
# ==============================================================================
#
# Write this program from scratch. A starter structure is provided but the
# logic is all yours to fill in.
#
# The program should:
#   1. Start with an empty playlist
#   2. Ask the user to enter 5 songs (one at a time)
#   3. If a song is already in the playlist, don't add it — tell the user
#   4. Print the final playlist in reverse order
#
# Run your solution with:   python problem1/05_make.py
#
# Example output:
#   Enter song 1: Flowers
#   Enter song 2: Unholy
#   Enter song 3: Flowers
#   "Flowers" is already in your playlist — skipping
#   Enter song 4: As It Was
#   Enter song 5: Anti-Hero
#
#   Your playlist (reversed):
#   Anti-Hero
#   As It Was
#   Unholy
#   Flowers
# ==============================================================================

playlist = []

# TODO: loop 5 times and ask the user for a song each time
# TODO: only add the song if it isn't already in the playlist
# TODO: print the playlist in reverse order

# for x in range (5):
#     user_input = input(f"Enter song {x+1}")
#     if user_input not in playlist:
#         playlist.append(user_input)
#         print(f"{user_input} has been added to the playlist")
#     else:
#         print(f"{user_input} has been added to the playlist")
#     for x in range(len(playlist)-1,-1,-1):
#         print(f"your playlist is {playlist[x]}")

i = 0
while i < 5:
    user_input = input(f"Enter song {i+1}")
    if user_input not in playlist:
        playlist.append(user_input)
        i +=1
        print(f"{user_input} has been added to the playlist")
    else:
        print(f"{user_input} is already in the plalist, please enter a different song")
    for i in range(len(playlist)-1,-1,-1):
        print(f"your playlist is {playlist[i]}")
    

