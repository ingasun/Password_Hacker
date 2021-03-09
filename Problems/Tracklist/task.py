tracks = {"Woodkid": {"The Golden Age": "Run Boy Run",
                      "On the Other Side": "Samara"},
          "Cure": {"Disintegration": "Lovesong",
                   "Wish": "Friday I'm in love",
                   "Seventeen Seconds": "A Forest"}}


def tracklist(**tracks):
    for artist, albums in tracks.items():
        print(artist)
        for album in albums.items():
            print("ALBUM:"," TRACK: ".join(album))


# tracklist(Woodkid={"The Golden Age": "Run Boy Run",
#                    "On the Other Side": "Samara"},
#           Cure={"Disintegration": "Lovesong",
#                 "Wish": "Friday I'm in love",
#                 "Seventeen Seconds": "A Forest"})