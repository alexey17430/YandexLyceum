class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.all_words = list()

    def add_word(self, word):
        if self.all_words and len(word) + len(self.all_words[-1]) < self.width:
            self.all_words[-1] += ' ' + word
        else:
            self.all_words.append(word)

    def end(self):
        for elem in self.all_words:
            print(elem)
        self.all_words = list()


class RightParagraph(LeftParagraph):
    def end(self):
        for elem in self.all_words:
            print(elem.rjust(self.width, ' '))
        self.all_words = list()
