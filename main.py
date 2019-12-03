# Ruben Navarro
# 12/03/2019
# main.py
# CTCI - URLify
# Inserts a string into another string when there is a single space.

# checks if a string is empty
def check_if_empty(s):
    if not s:
        return False
    else:
        return True

# checks if string is of length 1
def check_single_char(s):
    if len(s) == 1:
        return False;
    else:
        return True;

# constructs string and returns finalized results
def construct_string(s):
    str2 = ""
    i = 0

    for c in s:
        if c == ' ' and i != len(s):
            if s[i + 1] != ' ':
                i += 1
                str2 += "%20"
        else:
            str2 += c
            i += 1
    return str2

# Main function
str = "Mr John Smith    "

if not check_if_empty(str):
    print("String is empty")
    exit()

if not check_single_char(str):
    print("String must be of length 2 or greater")
    exit()

final_string = construct_string(str)

print("Final String: {0}".format(final_string))

