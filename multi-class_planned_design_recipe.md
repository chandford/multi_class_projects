# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can RECORD my experiences
I want to keep a regular DIARY

As a user
So that I can reflect on my experiences
I want to READ my PAST diary ENTRIES

As a user
So that I can reflect on my experiences in my busy day
I want to SELECT diary ENTRIES to read BASED ON how much TIME I have and my READING SPEED

As a user
So that I can KEEP TRACK of my tasks
I want to keep a TODO LIST along with my diary

As a user
So that I can KEEP TRACK of my CONTACTS
I want to see a LIST of all of the MOBILE phone NUMBERS IN all my DIARY ENTRIES

## 2. Design the Class System

                             ┌───────────────────────┐       ┌─────────────────────┐  
                             │                       │       │                     │  
                             │  Diary                │       │   TodoList          │  
                             │                       │       │                     │  
                             │  - entry_list         │       │  - todo_list        │  
                             │                       │       │                     │  
                             │  - add()              │       │ - add()             │  
 Takes contacts from entries │  - all()              │       │ - show_outstanding()│  
 ┌───────────────────────┐   │  - count_words()      │       │ - show_completed()  │  
 │                       │   │  - reading_time()     │       │ - reset_list()      │  
 │   ContactManager      │   │  - find_best_entry()  │       │                     │  
 │                       │   │                       │       │                     │  
 │   - contact_list      │   │                       │       │                     │  
 │                       │   └──┬───────┬────────────┘       └───────────┬─────────┘  
 │   - add()             │      │       │                                │            
 │   - all()             │      │       │    stores                      │  stores    
 │                       │   ┌──┘       │  instances                     │ instances  
 │                       │   │        ─ │     of...                      │   of...    
 │                       ├───┘          │                                │            
 │                       │   ┌──────────┴────────────┐       ┌───────────┴─────────┐  
 │                       │   │                       │       │                     │  
 └───────────────────────┘   │    DiaryEntry(contents)       │   ToDo(task)        │  
                            ─┤                       │       │                     │  
                             │  - entry_num          │       │  - task             │  
                             │  - contents           │       │  - complete         │  
                             │  - date               │       │                     │  
                             │  - word_count         │       │                     │  
                             │                       │       │  - mark_complete()  │  
                             │  - count_words()      │       │                     │  
                             │  - reading_time()     │       │                     │  
                             │  - reading_chunk()    │       │                     │  
                             │                       │       │                     │  
                             └───────────────────────┘       └─────────────────────┘  
                                                                                      
                                                                                      
                                                                                      
                                                                                    
                                                                                     

```python
class DiaryEntry:

    # User-facing properties:
    #   entry_num: an integer
    #   contents: a string
    #   date: a datetime object
    #   word_count: an integer (?)

    def __init__(self, contents):
        # Side-effects:
        #   Sets the entry_num property
        #   Sets the contents property
        #   Sets the date property

        pass

    def count_words(self):
        # Side-effects:
        #   Sets the word_count property
        # Returns:
        #   An integer representing the number of words in the contents
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: integer representing the num of words the user can read
        #        per minute
        # Returns:
        #   Integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        pass


class Diary:

    def __init__(self):
        # Properties:
        #   entry_list: a list of DiaryEntry instances
        #   entry_count: an integer (protect?)
        pass 

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Side-effects:
        #   Adds the entry to the entries list
        pass

    def all(self):
        # Parameters:
        #   None
        # Returns:
        #   A list of instances of DiaryEntry
        pass

    def count_words(self):
        # Parameters:
        #   None
        # Returns:
        #   Integer representing the number of words in all diary entries
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        pass
    

    def find_best_entry(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass


class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        pass

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass

class TodoList:
    def __init__(self):
    # Properties:
        #   todo_list: a list of Todo instances
        pass

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        pass

    def show_outstanding(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        pass

    def show_completed(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass


    def reset_list(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass


class Contact:
    def __init__(self, name, number):
        # Parameters:
        #   name: a name representing the contact's name
        #   number: a string(?) representing the contact's phone number
        # Side-effects:
        #   Sets the name property
        #   Sets the number property
        pass

class ContactManager: 
    def __init__(self):
        # Properties:
        #   contact_list: a list of Contact instances
        pass 


    def add(self, contact):
        # Parameters:
        #   contact: an instance of Contact
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the Contact to the list of contacts
        pass

    def all(self):
        # Parameters:
        #   None
        # Returns:
        #   A list of dictionaries of contacts(?)
        pass

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
