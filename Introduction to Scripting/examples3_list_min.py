"""
Example of program that use a loop to compute the minimum number in a list
"""


def list_minimum(numbers):
    """
    Compute the minimum of a list of numbers
    """

    min_num = float("inf")
    for num in numbers:
        if num < min_num:
            min_num = num  # Set "Run to cursor" on this line
    return min_num

def run_example():
    """
    Run an example using list_minimum
    """
    example_list = [4.6, 5.9, 2.1, 5.7, 1.1, 8.3]
    print("An example list is", example_list)
    print()
    minimum_number = list_minimum(example_list)
    print("The minimum of this example list is", minimum_number)

run_example()
