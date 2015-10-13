class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for verse in self.lyrics:
            print(verse)
        print('-' * 30)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right here"])

bop_lyrics = ["They rally around the family",
             "With pockes full of shells"]

bulls_on_parade = Song(bop_lyrics)

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
