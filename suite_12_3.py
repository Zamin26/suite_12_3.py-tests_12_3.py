import unittest
from runner import Runner  # Импортируем Runner
from runner_and_tournament import Runner, Tournament
import tests_12_3


test_suite = unittest.TestSuite()  # Новый объект
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))



runner = unittest.TextTestRunner(verbosity=2)  #  объект класса TextTestRunner, с аргументом verbosity=2.
runner.run(test_suite)  # Запуск теста



