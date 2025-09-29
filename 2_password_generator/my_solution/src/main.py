import random
import string
from abc import ABC , abstractmethod
import nltk

if nltk.corpus.words.words() is None :
    nltk.download('words')


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass



class PinGenerator(PasswordGenerator):
    def __init__(self,length):
        self.length = length

    def generate(self): 
        return ''.join([random.choice(string.digits) for _ in range(self.length)])
    
# pin_gen = PinGenerator(8)
# pin_gen.generate()


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self,length: int = 8, include_sambols: bool = False, include_numbers: bool = False):
        self.length = length
        self.char = string.ascii_letters
        if include_sambols:
            self.char += string.punctuation
        if include_numbers:
            self.char += string.digits

    def generate(self): 
        return ''.join([random.choice(self.char) for _ in range(self.length)])
    
# pass_gen = RandomPasswordGenerator(8,True,True)
# pass_gen.generate()


class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(
        self,num_of_words: int = 4,
        separator: str = '-',
        caplitalization: bool = False,
        vocabulary: list = None
    ):
        if vocabulary is None:
            self.vocabulary = nltk.corpus.words.words()
        vocabulary = vocabulary
        self.num_of_words = num_of_words
        self.separator = separator
        self.caplitalization = caplitalization

    def generate(self): 
        password_words = [random.choice(self.vocabulary) for _ in range(self.num_of_words)]
        if self.caplitalization:
              return self.separator.join(
                [word.upper() if random.choice([False,True]) else word.lower() for word in password_words])
        return self.separator.join(password_words)

# memorable_pass_gen = MemorablePasswordGenerator(8,' ',True)
# memorable_pass_gen.generate()

if __name__ == '__main__':
    p_obg = MemorablePasswordGenerator()
    print(p_obg.generate())