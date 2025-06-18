from lib.track import Track
from lib.music_library import MusicLibrary

def test_add_adds_single_track_instance():
    library = MusicLibrary()
    track_1 = Track("Track Title", "Artist Name")
    library.add(track_1)
    assert library.tracks == [track_1]

def test_add_adds_multiple_track_instances():
    library = MusicLibrary()
    track_1 = Track("Track Title", "Artist Name")
    track_2 = Track("Track Title 2", "Artist Name 2")
    library.add(track_1)
    library.add(track_2)
    assert library.tracks == [track_1, track_2]


def test_search_returns_track_instance_for_matching_title():
    library = MusicLibrary()
    track_1 = Track("Track Title", "Artist Name")
    track_2 = Track("Title 2", "Artist Name 2")
    library.add(track_1)
    library.add(track_2)
    assert type(library.search("Track")) == list
    assert library.search("Track") == [track_1]

def test_search_returns_track_instance_for_matching_artist():
    library = MusicLibrary()
    track_1 = Track("Track Title", "Artist Name")
    track_2 = Track("Title 2", "Artist Name 2")
    library.add(track_1)
    library.add(track_2)
    assert library.search("Name") == [track_1, track_2]
    assert library.search("Name")[-1].title == "Title 2"