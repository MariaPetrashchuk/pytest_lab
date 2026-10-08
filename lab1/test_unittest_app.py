import unittest
from unittest.mock import patch
from unittest_app import check_number, count_vowels, get_number


class TestCheckNumber(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.figures = [
            ("Привіт", 2),
            ("Python", 1),
            ("Україна", 4)
        ]

    @classmethod
    def tearDownClass(cls):
        cls.figures = None

    def setUp(self):
        self.test_number = 5

    def tearDown(self):
        self.test_number = None

    def test_correct_number(self):
        self.assertTrue(check_number(self.test_number))

    def test_invalid_number(self):
        with self.assertRaises(AssertionError):
            check_number(0)

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Привіт"), 2)
        self.assertEqual(count_vowels("Python"), 1)
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("12345"), 0)
        self.assertEqual(count_vowels("Україна"), 4)

    def test_vowels_with_subtest(self):
        for text, expected in self.figures:
            with self.subTest(text=text):
                self.assertEqual(count_vowels(text), expected)

    @patch("builtins.input", return_value="5")
    def test_get_number(self, mock_input):
        self.assertEqual(get_number(), "5")
        mock_input.assert_called_once_with("Введіть число: ")


if __name__ == "__main__":
    unittest.main()