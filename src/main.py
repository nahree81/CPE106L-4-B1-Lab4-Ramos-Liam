from grade_calculator import GradeCalculator
from grade_calculator import AverageGradingStrategy
from grade_calculator import WeightedGradingStrategy


def main():
    print("=== Grade Calculator ===")
    print("1. Average Grading")
    print("2. Weighted Grading")

    choice = input("Choose a grading method: ")

    if choice == "1":
        scores = [float(x) for x in input(
            "Enter scores separated by spaces: "
        ).split()]

        calculator = GradeCalculator(AverageGradingStrategy())
        grade = calculator.calculate_grade(scores)

    elif choice == "2":
        print("Weights: 30% + 30% + 40%")

        scores = [float(x) for x in input(
            "Enter 3 scores separated by spaces: "
        ).split()]

        calculator = GradeCalculator(WeightedGradingStrategy())
        grade = calculator.calculate_grade(scores)

    else:
        print("Invalid choice.")
        return

    print(f"Final Grade: {grade:.2f}")


if __name__ == "__main__":
    main()