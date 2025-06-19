from lib.diary_entry import DiaryEntry

class Diary:
    def __init__(self):
        self.entry_list = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self.entry_list.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.entry_list

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        total_word_count = 0
        for entry in self.entry_list:
            total_word_count += entry.count_words()
        return total_word_count

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        word_count = self.count_words()
        reading_time = word_count / wpm
        return int(reading_time)
    

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
            chunk_length = wpm * minutes
            suitable_list = [entry for entry in self.entry_list if entry.count_words() <= chunk_length]
            sorted_suitable_entries = sorted(suitable_list, key= lambda l: l.count_words())
            return sorted_suitable_entries[-1]