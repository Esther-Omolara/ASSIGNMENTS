import math

# quadratic equation
def solve_quadratic(a: int | float, b: int | float, c: int | float) -> str:
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check if the discriminant is positive, negative, or zero
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Roots are real and distinct: {root1}, {root2}"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"Root is real and equal: {root}"
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        return f"Roots are complex: {real_part} + {imaginary_part}i, {real_part} - {imaginary_part}i"

# accept input for coefficients a, b, and c
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Call the solve_quadratic function and print the result
result = solve_quadratic(a, b, c)
print(result)