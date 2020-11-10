import unittest

from ex3 import intersection


class TestEx2(unittest.TestCase):

    def test_small(self):
        result = intersection([
            [1,2,3],
            [1,4,5],
            [1,6,7]
        ])
        self.assertTrue(result == [1])

        result = intersection([
            [1],
            [1],
        ])
        self.assertTrue(result == [1])

        result = intersection([
            [1,2],
            [1],
        ])
        self.assertTrue(result == [1])

        result = intersection([
            [1,2,3],
            [1,4,5,3],
            [1,6,7,3]
        ])
        result.sort()
        self.assertTrue(result == [1,3])

    def test_large(self):
        arrays = [
            list(range(10000, 20000)) + [1,2,3],
            list(range(20000, 30000)) + [1,2,3],
            list(range(30000, 40000)) + [1,2,3],
            list(range(40000, 50000)) + [1,2,3],
            list(range(50000, 60000)) + [1,2,3],
            list(range(60000, 70000)) + [1,2,3],
            list(range(70000, 80000)) + [1,2,3],
            list(range(80000, 90000)) + [1,2,3],
            list(range(90000, 100000)) + [1,2,3],
            list(range(100000, 110000)) + [1,2,3]
        ]

        result = intersection(arrays)
        result.sort()
        self.assertTrue(result == [1,2,3])

if __name__ == '__main__':
    unittest.main()
