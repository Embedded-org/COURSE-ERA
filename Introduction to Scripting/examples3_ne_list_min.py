"""
Example of program that use a loop to compute the minimum number in a non-empty list
"""


def ne_list_minimum(numbers):
    """
    Compute the minimum of a non-empty list of numbers - contains an error
    """

    min_num = numbers[0]
    for num in numbers[1 :]:
        if num > min_num:
            min_num = num  # Set "Run to cursor" on this line
    return min_num

def run_tests():
    """
    Run an example using list_minimum
    """
    print(ne_list_minimum([1.0]))
    print(ne_list_minimum([-1.0, -2.0, 3.3]))
    print(ne_list_minimum([4.6, 5.9, 2.1, 5.7, 1.1, 8.3]))

run_tests()
