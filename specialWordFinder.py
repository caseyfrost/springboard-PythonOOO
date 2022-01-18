from wordfinder import WordFinder


class SpecialWordFinder(WordFinder):
    """Subclass of WordFinder
    Unlike WordFinder it removes blank lines and lines that begin with #"""

    def crt_wrd_lst(self):
        """returns a list of words from a file where each line is one word but removes blank lines and lines that
        start with the # character"""
        with open(self._path, 'r') as file:
            lines = []
            while line := file.readline():
                line = line.rstrip()
                if line != '':
                    if line[0] != '#':
                        lines.append(line)
        return lines


if __name__ == '__main__':
    test = SpecialWordFinder('words_test.txt')
    print(test.random())
