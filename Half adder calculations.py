# Half Adder Calculator
# Digital Circuits / Electrical Engineering
#
# Half Adder:
# Sum   = A XOR B
# Carry = A AND B


def half_adder(a, b):
    """Calculate Sum and Carry of a half adder."""

    if a not in [0, 1] or b not in [0, 1]:
        raise ValueError("Inputs must be 0 or 1.")

    sum_bit = a ^ b
    carry = a & b

    return sum_bit, carry


def calculate_half_adder():
    print("\n========== HALF ADDER CALCULATOR ==========")

    try:
        a = int(input("Enter input A (0 or 1): "))
        b = int(input("Enter input B (0 or 1): "))

        sum_bit, carry = half_adder(a, b)

        print("\nResults:")
        print(f"A     = {a}")
        print(f"B     = {b}")
        print(f"Sum   = {sum_bit}")
        print(f"Carry = {carry}")

    except ValueError as error:
        print(f"\nError: {error}")


def display_truth_table():
    print("\n========== HALF ADDER TRUTH TABLE ==========")

    print("\nA\tB\tSUM\tCARRY")
    print("---------------------------")

    for a in [0, 1]:
        for b in [0, 1]:
            sum_bit, carry = half_adder(a, b)
            print(f"{a}\t{b}\t{sum_bit}\t{carry}")


def gate_calculation():
    print("\n========== LOGIC GATE CALCULATION ==========")

    a = int(input("Enter A (0 or 1): "))
    b = int(input("Enter B (0 or 1): "))

    if a not in [0, 1] or b not in [0, 1]:
        print("Error: Inputs must be 0 or 1.")
        return

    xor_output = a ^ b
    and_output = a & b

    print("\nGate Outputs:")
    print(f"XOR Gate Output (SUM)   = {xor_output}")
    print(f"AND Gate Output (CARRY) = {and_output}")


def binary_addition():
    print("\n========== ONE-BIT BINARY ADDITION ==========")

    a = int(input("Enter first bit (0 or 1): "))
    b = int(input("Enter second bit (0 or 1): "))

    if a not in [0, 1] or b not in [0, 1]:
        print("Error: Enter only 0 or 1.")
        return

    sum_bit, carry = half_adder(a, b)

    print(f"\n{a} + {b}")

    if carry == 1:
        print(f"Result = {carry}{sum_bit}")
    else:
        print(f"Result = {sum_bit}")

    print(f"SUM   = {sum_bit}")
    print(f"CARRY = {carry}")


def main():

    while True:

        print("\n==============================================")
        print("          HALF ADDER CALCULATOR")
        print("          Digital Circuits")
        print("          Electrical Engineering")
        print("==============================================")

        print("1. Half Adder Calculation")
        print("2. Display Truth Table")
        print("3. Logic Gate Calculation")
        print("4. One-Bit Binary Addition")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        try:

            if choice == "1":
                calculate_half_adder()

            elif choice == "2":
                display_truth_table()

            elif choice == "3":
                gate_calculation()

            elif choice == "4":
                binary_addition()

            elif choice == "5":
                print("\nThank you for using Half Adder Calculator!")
                break

            else:
                print("\nInvalid choice. Please select 1-5.")

        except ValueError:
            print("\nPlease enter valid binary inputs (0 or 1).")


if __name__ == "__main__":
    main()
