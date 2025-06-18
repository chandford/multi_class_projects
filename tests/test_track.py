from lib.track import Track

def test_track_sets_title_and_artist():
    track = Track("Track Title", "Artist Name")
    assert track.title == "Track Title"
    assert track.artist == "Artist Name"

def test_matches_returns_true_for_matching_keyword_title():
    track = Track("Track Title", "Artist Name")
    assert track.matches("Title") == True

def test_matches_returns_true_for_matching_keyword_artist():
    track = Track("Track Title", "Artist Name")
    assert track.matches("Name") == True

def test_matches_returns_false_for_no_matching_keyword():
    track = Track("Track Title", "Artist Name")
    assert track.matches("Song") == False
