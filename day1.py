'''The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
'''

digit_counter = 0
total_sum = 0
single_digit = None
combined_digit = None

with open ('01_puzzle_input.txt', 'r') as file:

    for text_row in file:



        for char in text_row:
            if char.isdigit():
                digit_counter += 1

        if digit_counter > 1:
            for char in text_row:
                if char.isdigit():
                    first_digit = char
                    break

            for char in reversed(text_row):
                if char.isdigit():
                    second_digit = char
                    break

            combined_digit = int(str(first_digit) + str(second_digit))


        elif digit_counter <= 1:
            for char in text_row:
                if char.isdigit():
                    single_digit = int(char)

        if combined_digit is not None:
            total_sum += combined_digit
        if single_digit is not None:
            total_sum += single_digit

print(total_sum)







