# Assignment 5
import re

def check_string(s):
    pattern = "^[A-Za-z0-9] + $"  # ^=start, $=end, +=one or more
    return bool(re.match(pattern, s))


# Example Usage
s1 = "Hello123"
s2 = "Hello_123"  # Contains Underscore

print (check_string(s1))
print(check_string(s2))