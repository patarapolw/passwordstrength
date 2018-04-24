import string

from passwordstrength.dir import database_path


class Entropy:
    def __init__(self):
        with open(database_path('google-10000-english.txt')) as f:
            self.common_words = f.read().strip().split('\n')
        with open(database_path('words.txt')) as f:
            self.dictionary_words = f.read().strip().split('\n')

    def entropy_non_word(self, password):
        entropy = 1
        for i, char in enumerate(password):
            if char in string.punctuation + string.digits:
                entropy *= len(string.printable)
            elif self._consecutive(password, i):
                entropy *= len(string.ascii_lowercase)
            else:
                entropy *= len(string.ascii_letters)

        return entropy

    @staticmethod
    def _consecutive(password, index):
        if len(password) < index+3:
            return False

        if all([char.islower() for char in password[index:index+3]]):
            return True
        elif all([char.isupper() for char in password[index:index+3]]):
            return True
        else:
            return False

    def entropy_word_list(self, keyword_list):
        entropy = 1
        for word in keyword_list:
            if word in self.common_words:
                entropy *= len(self.common_words)
            elif word.lower() in self.common_words:
                entropy *= 2*len(self.common_words)
            elif word in self.dictionary_words:
                entropy *= len(self.dictionary_words)
            else:
                entropy *= self.entropy_non_word(word)

        return entropy
