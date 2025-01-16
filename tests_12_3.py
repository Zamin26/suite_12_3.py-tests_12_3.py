import unittest

from runner import Runner  # Импортируем Runner
from runner_and_tournament import Runner, Tournament

def skip_if_frozen(test_method):                        # Пропуск теста, если is_frozen равно True
    def wrapper(self):
        if getattr(self, 'is_frozen', False):           # Дополнение атрибутом is_frozen
            raise unittest.SkipTest('Тесты в этом кейсе заморожены') # Если is_frozen равно True,пропускаем тест и выводим сообщение
        return test_method(self)            # В случае is_frozen = False, тест выполняется
    return wrapper

class RunnerTest(unittest.TestCase):    # Декораторы для класса RunnerTest
    is_frozen = False  #  Атрибут is_frozen = False

    @skip_if_frozen                 # Применение декоратора
    def test_challenge(self):
        self.assertEqual(2 + 2, 4)  # Проверка на сложение

    @skip_if_frozen                 # Применение декоратора
    def test_run(self):
        self.assertTrue(True)       # Проверка на условие True


    @skip_if_frozen                 # Применение декоратора
    def test_walk(self):
        self.assertFalse(False)     # Проверка на условие False




class TournamentTest(unittest.TestCase):        # Дополнение класса TournamentTest декораторами
    is_frozen = True  # Условие is_frozen = True

    @skip_if_frozen  # Применение декоратора
    def test_first_tournament(self):
        self.assertEqual(3 * 2, 6)  # Проверка на умножение

    @skip_if_frozen  # Применение декоратора
    def test_second_tournament(self):
        self.assertTrue(False)  # Проверка на выражение False

    @skip_if_frozen  # Применение декоратора
    def test_third_tournament(self):
        self.assertIn(3, [2, 3, 4])  # Проверка на наличие числа в списке






