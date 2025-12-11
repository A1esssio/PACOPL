#include <math.h>   // For math functions, specifically sqrt (square root)
#include <stdio.h>  // For input/output functions like printf and scanf
#include <stdlib.h> // For string to number conversion (atof)

// Function to prompt the user for a coefficient
// &coeff is a "pointer", it allows the function to modify the variable in main
void prompt_input_coefficient(const char *name, double *coeff) {
  printf("Enter coefficient %s: ", name);
  // Infinite loop until a valid number is entered
  while (scanf("%lf", coeff) != 1) {
    printf("Error: Invalid input. Please try again: ");
    // Clear the input buffer to prevent the program from getting stuck on
    // invalid input
    while (getchar() != '\n')
      ;
  }
}

int main(int argc, char *argv[]) {
  double a, b, c;

  if (argc == 4) {
    printf("Coefficients taken from command-line arguments.\n");
    a = atof(argv[1]);
    b = atof(argv[2]);
    c = atof(argv[3]);
  } else {
    printf("No coefficients were passed, please enter them manually.\n");
    prompt_input_coefficient("A", &a);
    prompt_input_coefficient("B", &b);
    prompt_input_coefficient("C", &c);
  }

  printf("\nSolving equation: %.2fx^4 + %.2fx^2 + %.2f = 0\n", a, b, c);

  // --- Solving Logic ---
  double discriminant = b * b - 4 * a * c;
  if (discriminant < 0) {
    printf("No real roots because the discriminant is negative.\n");
    return 0;
  }

  double yFirst = (-b + sqrt(discriminant)) / (2 * a);
  double ySecond = (-b - sqrt(discriminant)) / (2 * a);

  double roots[4];
  int count = 0;

  if (yFirst >= 0) {
    double xFirst = sqrt(yFirst);
    if (xFirst == 0) {
      roots[count++] = 0;
    } else {
      roots[count++] = xFirst;
      roots[count++] = -xFirst;
    }
  }

  if (ySecond >= 0) {
    double xSecond = sqrt(ySecond);
    if (yFirst != ySecond) {
      if (xSecond == 0) {
        if (yFirst != 0) {
          roots[count++] = 0;
        }
      } else {
        roots[count++] = xSecond;
        roots[count++] = -xSecond;
      }
    }
  }
  // --- Solving Logic ---

  // --- Output Result ---
  if (count == 0) {
    printf("No real roots found.\n");
  } else {
    printf("Found real roots:\n");
    for (int i = 0; i < count; i++) {
      printf("%.2f ", roots[i]);
    }
    printf("\n");
  }
  // --- Output Result ---

  return 0;
}
