import unittest

from src.grade_calculator import GradeCalculator
from src.grade_calculator import AverageGradingStrategy
from src.grade_calculator import WeightedGradingStrategy


class TestGradeCalculator(unittest.TestCase):

    def test_average_grading(self):
        calculator = GradeCalculator(AverageGradingStrategy())

        result = calculator.calculate_grade([80, 90, 100])

        self.assertEqual(result, 90)

    def test_weighted_grading(self):
        calculator = GradeCalculator(WeightedGradingStrategy())

        result = calculator.calculate_grade([80, 90, 100])

        self.assertEqual(result, 91)

    def test_empty_scores(self):
        calculator = GradeCalculator(AverageGradingStrategy())

        result = calculator.calculate_grade([])

        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()