import random

MAX_NUMBER_OF_CAPITALIZED_CHARS_IN_A_ROW = 2
MAX_NUMBER_OF_UNCAPITALIZED_CHARS_IN_A_ROW = 3
CAPITALIZATION_PROBABILITY = 0.7

def capitalizator(str_input):
    capitalized_ch_counter =0
    uncapitalized_ch_counter = 0
    str_output = ""

    def should_capitalize():
        if capitalized_ch_counter == MAX_NUMBER_OF_CAPITALIZED_CHARS_IN_A_ROW:
            return False
        if uncapitalized_ch_counter == MAX_NUMBER_OF_UNCAPITALIZED_CHARS_IN_A_ROW:
            return True
        if random.random() < CAPITALIZATION_PROBABILITY:
            return True

    for s in str_input:
        if should_capitalize():
            str_output += s.capitalize()
            capitalized_ch_counter += 1
            uncapitalized_ch_counter = 0
        else:
            capitalized_ch_counter = 0
            uncapitalized_ch_counter += 1
            str_output += s

    return str_output

def main():
    str_input = input("Input:\n").lower()
    str_parsed = capitalizator(str_input)
    print(str_parsed)

if __name__ == "__main__":
    main()