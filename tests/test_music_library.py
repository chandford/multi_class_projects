from lib.music_library import MusicLibrary
from unittest.mock import Mock

def test_musiclibrary_has_store_for_track_instances():
    library = MusicLibrary()
    assert library.tracks == []

def test_add_adds_single_track_instance():
    library = MusicLibrary()
    track_1 = Mock()
    library.add(track_1)
    assert library.tracks == [track_1]

def test_add_adds_multiple_track_instances():
    library = MusicLibrary()
    track_1 = Mock()
    track_2 = Mock()
    library.add(track_1)
    library.add(track_2)
    assert library.tracks == [track_1, track_2]
    track_3 = Mock()
    library.add(track_3)
    assert library.tracks == [track_1, track_2, track_3]


def test_search_returns_track_instance_for_matching_keyword_title():
    library = MusicLibrary()
    track_1 = Mock()
    track_1.title = "Track Title"
    track_1.artist = "Artist Name"
    library.add(track_1)
    assert type(library.search("Track")) == list
    assert library.search("Track") == [track_1]

def test_search_returns_track_instance_for_matching_keyword_artist():
    library = MusicLibrary()
    track_1 = Mock()
    track_1.title = "Track Title"
    track_1.artist = "Artist Name"
    library.add(track_1)
    assert library.search("Artist") == [track_1]

def test_search_returns_track_instances_for_multiple_matching_keywords():
    library = MusicLibrary()
    track_1 = Mock()
    track_1.title = "Track Title"
    track_1.artist = "Artist Name"
    track_2 = Mock()
    track_2.title = "Track Title 2"
    track_2.artist = "Artist Name 2"
    library.add(track_1)
    library.add(track_2)
    assert library.search("Name") == [track_1, track_2]
