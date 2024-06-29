# 5. Longest Palindromic Substring
#    - Write a program to find the longest palindromic substring within a given string.
#    - Expected output: If the input string is "babad", the output should be "bab" or "aba". If the input string is "cbbd", the output should be "bb".

def longest_palindromic_substring(s):
    if len(s) < 2:
        return s

    start, max_length = 0, 1
    for i in range(1, len(s)):
        odd = s[i - max_length - 1:i + 1]
        even = s[i - max_length:i + 1]
        if i - max_length - 1 >= 0 and odd == odd[::-1]:
            start = i - max_length - 1
            max_length += 2
        elif even == even[::-1]:
            start = i - max_length
            max_length += 1

    return s[start:start + max_length]

input_str = "babad"
result = longest_palindromic_substring(input_str)
print(result)
