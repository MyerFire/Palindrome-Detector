import argparse
import datetime
import humanfriendly


def is_palindrome(number):
    number = str(number) if not isinstance(number, str) else number  # converts the input to a str because this
    # only works with str
    number = list(number)  # this is weird because the .reverse() method on a list does not return a list
    _reversed = list(number)  # instead, it mutates the original list
    _reversed.reverse()  # so, i have to have two variables
    return True if number == _reversed else False


def test(test_range):
    for number in range(1, test_range + 1):
        if is_palindrome(number):
            yield number


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    parser = argparse.ArgumentParser(description="Tests if a number is a palindrome")
    parser.add_argument("--test", help="Triggers a test of 1 to N numbers")
    args = parser.parse_args()
    if args.test:
        palindromes = [str(number) for number in test(int(args.test))]
        print(f"The palindromes from 1 to {args.test} were {', '.join(palindromes)}")
        print(f"There were a total of {len(palindromes)}")
        print(f"Calculation took {humanfriendly.format_timespan(datetime.datetime.now() - start_time)}")
    else:
        print("Please enter a number to check whether it is a palindrome:", end=" ")
        number = input()
        print(f"The number {number} {'is a palindrome' if is_palindrome(number) else 'is not a palindrome'}")
        if len(number) == 1:
            print(f"Note that the number {number} is a single digit")
