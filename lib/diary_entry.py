class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.title = title
        self.contents = contents
        self.position = 0

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
            words_list = self.contents.split()
            return len(words_list)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
            word_count = self.count_words()
            reading_time = word_count / wpm
            return int(reading_time)

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        chunk_length = wpm * minutes
        contents_list = self.contents.split()

        if self.position >= len(contents_list):
            self.position = 0

        chunk = " ".join(contents_list[self.position: self.position+chunk_length])
        self.position += chunk_length

        return chunk