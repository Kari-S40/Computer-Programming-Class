# Lesson 7 Assignment - Debugging and Testing Example

def calculate_product(numbers):
    print("[trace] entering calculate_product with:", numbers)
    product = 1
    for n in numbers:
        product = product * n
    print("[trace] exiting calculate_product with result =", product)
    return product

def main():
    try:
        print("Welcome to the Product Calculator Program!")
        count = int(input("How many numbers would you like to enter? "))

        numbers = []
        i = 0
        while i < count:
            value = float(input(f"Enter number {i + 1}: "))
            numbers.append(value)
            i = i + 1

        total_product = calculate_product(numbers)          # ✅ correct call
        last_number = numbers[len(numbers) - 1]             # ✅ index access

        print("Numbers entered:", numbers)
        print("Product of numbers:", total_product)
        print("Last number in the list (by index):", last_number)

        print("Completed by, Kari Shaddinger")

    except ValueError as e:
        print(f"Value Error: {e}")
    except IndexError as e:
        print(f"Run-time Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
