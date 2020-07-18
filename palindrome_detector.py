import argparse


def is_palindrome(number):
    number = str(number) if not isinstance(number, str) else number  # converts the input to a str because this
    # only works with str
    number = list(number)  # this is weird because the .reverse() method on a list does not return a list
    _reversed = list(number)  # instead, it mutates the original list
    _reversed.reverse()  # so, i have to have two variables
    return True if number == _reversed else False


def test(test_range):
    data = []
    for number in range(1, test_range + 1):
        data.append({
            "number": number,
            "is_palindrome": is_palindrome(number)
        })
    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tests if a number is a palindrome")
    parser.add_argument("--test", help="Triggers a test of 1 to N numbers")
    args = parser.parse_args()
    if args.test:
        data = test(int(args.test))
        string, palindromes, non_palindromes = [], [], []
        for _set in data:
            string.append(f"{_set['number']}: {_set['is_palindrome']}")
            if _set["is_palindrome"]:
                palindromes.append(_set["number"])
            else:
                non_palindromes.append(_set["number"])
        print("\n".join(string))
        print(f"In the range of 1 to {args.test}, {len(palindromes)} palindrome(s) were found, and {len(non_palindromes)} non-palindrome(s) were found")
    else:
        print("Please enter a number to check whether it is a palindrome:", end=" ")
        number = input()
        print(f"The number {number} {'is a palindrome' if is_palindrome(number) else 'is not a palindrome'}")
        if len(number) == 1:
            print(f"Note that the number {number} is a single digit")
