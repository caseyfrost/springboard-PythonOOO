"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    """Reads a text file of lines with one word each into a python list and prints out the count of words.
    Contains a function to return a random word from the list of words."""

    def __init__(self, path):
        # creates the list attribute from the file using the crt_wrd_lst function below
        self._path = path
        self._wrd_lst = self.crt_wrd_lst()

    @property
    def path(self):
        return self._path

    @property
    def wrd_lst(self):
        return self._wrd_lst

    def crt_wrd_lst(self):
        # returns a list of words from a file where each line is one word
        with open(self._path, 'r') as file:
            lines = []
            while line := file.readline():
                lines.append(line.strip())
        return lines

    def random(self):
        # returns a random word from the wrd_lst attribute
        print(self._wrd_lst)
        return random.choice(self._wrd_lst)


if __name__ == '__main__':
    test = WordFinder('words_test.txt')
    print(test.random())
