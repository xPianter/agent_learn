import unittest

from valid_parentheses import is_valid


class TestIsValid(unittest.TestCase):
    def test_valid_cases(self):
        cases = ["()", "()[]{}", "{[]}"]

        for s in cases:
            with self.subTest(s=s):
                self.assertTrue(is_valid(s))

    def test_invalid_cases(self):
        cases = ["(]", "([)]", "(", "]"]

        for s in cases:
            with self.subTest(s=s):
                self.assertFalse(is_valid(s))


if __name__ == "__main__":
    unittest.main()