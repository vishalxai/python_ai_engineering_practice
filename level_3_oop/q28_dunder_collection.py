# Q28 — OOP: Dunder Methods for Collections
# Create a Playlist class:
#   - __init__(self, name)  → stores name and an empty list of songs
#   - add_song(song)        → appends to the list
#   - __len__               → returns number of songs (enables len(playlist))
#   - __contains__          → enables "Song Title" in playlist
#   - __str__               → returns "Playlist: {name} ({n} songs)"
#
# Test:
#   p = Playlist("Chill")
#   p.add_song("Blinding Lights")
#   print(len(p))                        → 1
#   print("Blinding Lights" in p)        → True
