#Alphabet
import string

#1.	Создайте класс Alphabet
class Alphabet:
    #2.	Создайте метод __init__(), внутри которого будут определены два динамических свойства:
    # 1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
    def __init__(self, En, letters_str):
        self.lang = En
        self.letters = list(letters_str)

    # 3.	Создайте метод print(), который выведет в консоль буквы алфавита
    def print(self):
        print(self.letters)

    # 4.	Создайте метод letters_num(), который вернет количество букв в алфавите
    def letters_num(self):
        len(self.letters)


# Английский алфавит
#1.	Создайте класс EngAlphabet путем наследования от класса Alphabet
class EngAlphabet(Alphabet):

    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    # Проверяем, относится ли буква к английскому алфавиту
    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        return False

    # Возвращаем количество букв в алфавите
    def letters_num(self):
        return EngAlphabet.__letters_num

    # Печатаем пример текста на английском языке
    @staticmethod
    def example():
        print("Hello World, \n are you fine?")


# Тесты
# 1.	Создайте объект класса EngAlphabet
# 2.	Напечатайте буквы алфавита для этого объекта
# 3.	Выведите количество букв в алфавите
# 4.	Проверьте, относится ли буква F к английскому алфавиту
# 5.	Проверьте, относится ли буква Щ к английскому алфавиту
# 6.	Выведите пример текста на английском языке

if __name__ == '__main__':
    eng_alphabet = EngAlphabet()
    eng_alphabet.print()
    print(eng_alphabet.letters_num())
    print(eng_alphabet.is_en_letter('F'))
    print(eng_alphabet.is_en_letter('Щ'))
    EngAlphabet.example()



