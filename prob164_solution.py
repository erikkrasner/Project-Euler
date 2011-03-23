memoized_counts = {}

def count_appropriate_digits(num_digits, starting_with):
    def digit_sum(two_digit_integer):
        return two_digit_integer / 10 + two_digit_integer % 10
    argument_pair = (num_digits, starting_with)
    if argument_pair in memoized_counts:
        return memoized_counts[argument_pair]
    if digit_sum(starting_with) > 9:
        return 0
    if num_digits <= 2:
        return 1
    first_digit, second_digit = starting_with / 10, starting_with % 10
    third_digits = range(10 - first_digit - second_digit)
    result = sum(map(lambda third_digit: count_appropriate_digits(num_digits - 1, 10 * second_digit + third_digit),third_digits))
    memoized_counts[argument_pair] = result
    return result

for num_digits in range(3,21):
    for starting_with in range(100):
        count_appropriate_digits(num_digits,starting_with)

twenty_digit_counts = filter(lambda x: x[0] == 20 and x[1] >= 10, memoized_counts)
print sum(map(lambda x: memoized_counts[x], twenty_digit_counts))
