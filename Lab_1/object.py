import sys
import math


class BiquadraticEquationInRealSolution:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.roots = []

    def solve(self):
        discriminant = self.b ** 2 - 4 * self.a * self.c
        if discriminant < 0:
            return

        temp_roots = set()
        y1 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)
        y2 = (-self.b - math.sqrt(discriminant)) / (2 * self.a)

        if y1 >= 0:
            x1 = math.sqrt(y1)
            temp_roots.add(x1)
            temp_roots.add(-x1)

        if y2 >= 0:
            x2 = math.sqrt(y2)
            temp_roots.add(x2)
            temp_roots.add(-x2)

        self.roots = sorted(list(temp_roots))

    def display_results(self):
        print(
            f"equation: {self.a}x^4 + {self.b}x^2 + {self.c} = 0")
        if not self.roots:
            print("no real roots")
        else:
            print(f"real roots: {self.roots}")


def get_input_coefficient(args, index):
    try:
        return float(args[index])
    except (IndexError, ValueError):
        return None


def prompt_coefficient(name):
    while True:
        try:
            return float(input(f"write coefficient {name}: "))
        except ValueError:
            print("error: coefficient must be float")


def main():
    args = sys.argv[1:]

    a = get_input_coefficient(args, 0) or prompt_coefficient('A')
    b = get_input_coefficient(args, 1) or prompt_coefficient('B')
    c = get_input_coefficient(args, 2) or prompt_coefficient('C')

    equation = BiquadraticEquationInRealSolution(a, b, c)
    equation.solve()
    equation.display_results()


if __name__ == "__main__":
    main()
