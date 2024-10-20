def swap_variables(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    # Swap the values
    a, b = b, a
    print(f"After swapping: a = {a}, b = {b}")

def main():
    # Example values
    x = 5
    y = 10
    swap_variables(x, y)

if __name__ == "__main__":
    main()
