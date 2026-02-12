def is_even(number):
    if type(number) == int:
        if number %2 == 0:
            print("Even Number")
        else:
            print("Odd Number")
    else:
        print("Enter a integer")

# To run
is_even(2)
is_even(3)