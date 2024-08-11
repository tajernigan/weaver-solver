import time
import random
import unittest
import json
from src.weaverSolverBDBFS import find_shortest_path
from src.files.graphcreation import one_letter_off

class TestWeaverSolver(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('src/files/words4.json', 'r') as infile:
            cls.graph = json.load(infile)
        with open('src/files/four_letter_words.txt') as infile:
            cls.words = [word.strip() for word in infile]
        cls.totalTime = 0.0

    def test_random_cases(self):
        num_cases = 1000
        for _ in range(num_cases):  # Running 50 different random tests within the same method
            start = random.choice(self.words)
            end = random.choice(self.words)
            t1 = time.time()
            solution = find_shortest_path(start, end, self.graph)
            t2 = time.time()
            self.totalTime += t2 - t1

            if solution is None:
                self.assertIsNone(solution)
            else:
                self.assertEqual(start, solution[0], f'Incorrect starting word for {start} to {end}')
                self.assertEqual(end, solution[-1], f'Incorrect ending word for {start} to {end}')
                for i in range(1, len(solution)):
                    self.assertTrue(one_letter_off(solution[i - 1], solution[i]), f'{solution[i - 1]} and {solution[i]} are not one letter apart')
            print(f"{start} -> {end}: {solution}")
        print(f'\nran {num_cases} cases in {self.totalTime:.5f} seconds\n')
        # You can add assertions here if you want to ensure the total time is below a certain threshold, for example:
        # self.assertLess(cls.totalTime, some_threshold, "Total time for all tests exceeded expected value")

class CustomTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return unittest.TextTestResult(self.stream, self.descriptions, self.verbosity)

if __name__ == '__main__':
    runner = CustomTestRunner(verbosity=0)  # Set verbosity to 0 to suppress output
    runner.run(unittest.defaultTestLoader.loadTestsFromTestCase(TestWeaverSolver))