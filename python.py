# Fibonacci sequence up to n terms

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Input from the user
num_terms = int(input("Enter the number of terms: "))

# Generate and display the Fibonacci sequence
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Fibonacci sequence up to {num_terms} terms:")
    print(fibonacci(num_terms))
