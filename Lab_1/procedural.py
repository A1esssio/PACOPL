import sys
import math


def get_input_coefficient(args, index):
    try:
        return float(args[index])
    except (IndexError, ValueError):
        return None


def prompt_coefficient(name):
    while True:
        try:
            value = float(input(f"write coefficient {name}: "))
            return value
        except ValueError:
            print("error: coefficient must be float")


def solve_biquadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return []

    roots = set()
    y_first = (-b + math.sqrt(discriminant)) / (2 * a)
    y_second = (-b - math.sqrt(discriminant)) / (2 * a)

    if y_first >= 0:
        x_first = math.sqrt(y_first)
        roots.add(x_first)
        roots.add(-x_first)

    if y_second >= 0:
        x_second = math.sqrt(y_second)
        roots.add(x_second)
        roots.add(-x_second)

    return sorted(list(roots))


def main():
    args = sys.argv[1:]

    a = get_input_coefficient(args, 0)
    if a is None:
        a = prompt_coefficient('A')

    b = get_input_coefficient(args, 1)
    if b is None:
        b = prompt_coefficient('B')

    c = get_input_coefficient(args, 2)
    if c is None:
        c = prompt_coefficient('C')

    print(f"equation: {a}x^4 + {b}x^2 + {c} = 0")

    roots_real = solve_biquadratic(a, b, c)

    if not roots_real:
        print("no real roots")
    else:
        print(f"real roots: {roots_real}")


if __name__ == "__main__":
    main()
