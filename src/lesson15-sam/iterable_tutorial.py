import csv
from functools import total_ordering

@total_ordering
class Word(object):
    '''A simple object that represents a single word. We are overriding the 
    ordering functions so that words are sorted by their length, instead of
    alphabetical order. '''

    def __init__(self, text):
        assert ' ' not in text, "Words cannot have spaces in them."
        self.text = self.remove_nonalphanumeric_chars(text.lower())

    def __repr__(self):
        return '<Word: %s>' % (self.text,)

    def remove_nonalphanumeric_chars(self, text):
        return ''.join(c for c in text if c.isalpha())

    def __len__(self):
        return len(self.text)

    def __eq__(self, other):
        return len(self) == len(other)

    def __gt__(self, other):
        return len(self) > len(other) 

class FileReader(object):
    '''A simple object that takes a filename as input'''

    def __init__(self, filename):
        self.infile = open(filename)
            
    def __iter__(self):
        return self

    def next(self):        
        whisper_id, text = self.infile.next().split(',', 1)
        trimmed = text.strip()[1:-1]
        return [Word(w) for w in trimmed.split()]

    def __del__(self):
        self.infile.close()
             
    
def file_reader_generator(filename):
    with open(filename) as infile:
        for line in infile:
            whisper_id, text = infile.next().split(',', 1)
            trimmed = text.strip()[1:-1]
            yield [Word(w) for w in trimmed.split()]

