
class MusicLibrary:

    def __init__(self):
        self.tracks = []

    def add(self, track):
        self.tracks.append(track)

    def search(self, keyword):
        result_list = [ track for track in self.tracks
                        if keyword in track.title or keyword in track.artist
                        ]
        return result_list
