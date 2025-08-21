# first Version
def music_album():
    track_number = 1
    misc_album_list = {}
    while track_number <= 10:
        print("Please enter your track name and artist: ")
        print("(Press 'q' anytime to leave)")
        track_name = input("Enter the Track name: ")
        if track_name == 'q':
            break
        artist_name = input("Enter the Artist name: ")
        if artist_name == 'q':
            break
        if track_name:
            misc_album_list[f"{track_name}"] = f"{artist_name}"
            print(misc_album_list)
            print(track_number)
        track_number += 1
print(music_album())

