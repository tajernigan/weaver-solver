import unittest
import json
from src.weaverSolverBDBFS import find_shortest_path

class TestWeaverSolver(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('src/files/words4.json', 'r') as infile:
            cls.graph = json.load(infile)

    def test_find_shortest_path(self):
        # Define the test cases and expected results
        test_cases = {
            ('abri', 'cart'): (None, True),  # expects None
            ('tilt', 'tilt'): (0, False),  # optimal = 0
            ('hilt', 'tilt'): (1, False),  # optimal = 1
            ('hill', 'tilt'): (2, False),  # optimal = 2
            ('hall', 'tilt'): (3, False),  # optimal = 3
            ('plat', 'form'): (4, False),  # optimal = 4
            ('left', 'turn'): (5, False),  # optimal = 5
            ('very', 'much'): (6, False),  # optimal = 6
            ('swan', 'lake'): (7, False),  # optimal = 7
            ('anta', 'unau'): (8, False),  # optimal = 8
            ('acta', 'unau'): (9, False),  # optimal = 9
            ('abas', 'unau'): (10, False), # optimal = 10
            ('aahs', 'odic'): (11, False), # optimal = 11
            ('aahs', 'unau'): (12, False), # optimal = 12
            ('plat', 'unau'): (13, False), # optimal = 13
            ('star', 'unau'): (14, False), # optimal = 14
            ('ahem', 'unau'): (15, False), # optimal = 15
            ('eddo', 'unau'): (16, False), # optimal = 16
            ('atap', 'unau'): (17, False), # optimal = 17

        }

        for (start, end), (expected_length, expect_none) in test_cases.items():
            with self.subTest(start=start, end=end):
                result = find_shortest_path(start, end, self.graph)
                
                if expect_none:
                    self.assertIsNone(result, f"Expected None for path from {start} to {end}, but got {result}")
                else:
                    path_length = len(result) - 1
                    self.assertEqual(path_length, expected_length, f"Expected length {expected_length} for path from {start} to {end}, but got {path_length}")
                print(f"Result for path from '{start}' to '{end}': {result}")

if __name__ == '__main__':
    unittest.main()
