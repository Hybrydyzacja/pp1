class Music():
    def __init__(self, artist, track_tittle, album, year):
        self.artist = artist
        self.track_tittle = track_tittle
        self.album = album
        self.year = year

    def __str__(self):
        return "Performer: " + self.artist + "\n" + "Song: " + self.track_tittle + "\n"+"Album: " + self.album + "\n"+"Year: " + self.year

my_music = Music("Iron Maiden", "Run to the hills", "The number of the beast", "1984")
my_music2 = Music("Led Zeppelin", "Stairway to heaven", "IV" ,"1971")
print(my_music)
print()
print(my_music2)