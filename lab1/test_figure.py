import unittest
from figure_app import Figure


class TestFigure(unittest.TestCase):

    def test_figure_type(self):
        square = Figure("квадрат", 5)
        self.assertEqual(square.get_figure_type(), "квадрат")

    def test_figure_length(self):
        square = Figure("квадрат", 5)
        self.assertEqual(square.get_figure_length(), 5)

    def test_angles(self):
        figures = [
            ("квадрат", 4),
            ("прямокутник", 4),
            ("трикутник", 3)
        ]

        for figure_type, expected_angles in figures:
            with self.subTest(figure_type=figure_type):
                figure = Figure(figure_type, 5)
                self.assertEqual(figure.get_angles(), expected_angles)

    def test_zero_length(self):
        with self.assertRaises(AssertionError):
            Figure("квадрат", 0)

    def test_negative_length(self):
        with self.assertRaises(AssertionError):
            Figure("квадрат", -5)

    def test_unknown_type(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 5)


if __name__ == "__main__":
    unittest.main()