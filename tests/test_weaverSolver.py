import time
import random
import unittest
from src.weaverSolver import WeaverSolver
from src.graphcreation import words_list

class TestWeaverSolver(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.words = words_list(4)
        cls.solver = WeaverSolver(word_length=4)
        cls.totalTime = 0.0

    def one_letter_off(self, word_one, word_two):
        if len(word_one) != len(word_two):
            return False
        difference_count = 0
        for i in range(len(word_one)):
            if word_one[i] != word_two[i]:
                difference_count += 1
            if difference_count > 1:
                return False
        return difference_count == 1

    def test_random_cases(self):
        num_cases = 10000
        for _ in range(num_cases):  # Running 50 different random tests within the same method
            start = random.choice(self.words)
            end = random.choice(self.words)
            t1 = time.time()
            solution = self.solver.find_shortest_path(start, end)
            t2 = time.time()
            self.totalTime += t2 - t1

            if solution is None:
                self.assertIsNone(solution)
            else:
                self.assertEqual(start, solution[0], f'Incorrect starting word for {start} to {end}')
                self.assertEqual(end, solution[-1], f'Incorrect ending word for {start} to {end}')
                for i in range(1, len(solution)):
                    self.assertTrue(self.one_letter_off(solution[i - 1], solution[i]), f'{solution[i - 1]} and {solution[i]} are not one letter apart')
        # You can add assertions here if you want to ensure the total time is below a certain threshold, for example:
        # self.assertLess(cls.totalTime, some_threshold, "Total time for all tests exceeded expected value")

    def test_manual_cases(self):
        cases = [
            ("tilt", "tilt"),
            ("hilt", "tilt"),
            ("hill", "tilt"),
            ("hall", "tilt"),
            ("plat", "form"),
            ("left", "turn"),
            ("very", "much"),
            ("swan", "lake"),
            ("anta", "unau"),
            ("acta", "unau"),
            ("abas", "unau"),
            ("aahs", "odic"),
            ("aahs", "unau"),
            ("plat", "unau"),
            ("star", "unau"),
            ("ahem", "unau"),
            ("eddo", "unau"),
            ("atap", "unau"),
            ("chef", "cook"),
        ]

        for start, end in cases:
            solution = self.solver.find_shortest_path(start, end)
            if solution is not None:
                self.assertEqual(solution[0], start)
                self.assertEqual(solution[-1], end)
                for i in range(1, len(solution)):
                    self.assertTrue(self.one_letter_off(solution[i - 1], solution[i]))

class CustomTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return unittest.TextTestResult(self.stream, self.descriptions, self.verbosity)

if __name__ == '__main__':
    runner = CustomTestRunner(verbosity=0)  # Set verbosity to 0 to suppress output
    runner.run(unittest.defaultTestLoader.loadTestsFromTestCase(TestWeaverSolver))