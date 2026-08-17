from abc import ABC, abstractmethod


class GradingStrategy(ABC):

    @abstractmethod
    def calculate(self, scores):
        pass


class AverageGradingStrategy(GradingStrategy):

    def calculate(self, scores):
        if not scores:
            return 0

        return sum(scores) / len(scores)


class WeightedGradingStrategy(GradingStrategy):

    def calculate(self, scores):
        if not scores:
            return 0

        weights = [0.30, 0.30, 0.40]

        if len(scores) != len(weights):
            raise ValueError("Weighted grading requires exactly 3 scores.")

        return sum(score * weight for score, weight in zip(scores, weights))


class GradeCalculator:

    def __init__(self, strategy):
        self.strategy = strategy

    def calculate_grade(self, scores):
        return self.strategy.calculate(scores)