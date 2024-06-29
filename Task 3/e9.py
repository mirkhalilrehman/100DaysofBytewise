
# 9. Minimum Edit Distance
#    - Write a program to calculate the minimum number of operations (insertions, deletions, or substitutions) required to transform one string into another.
#    - Expected output: If the two input strings are "kitten" and "sitting", the output should be `3`.

def min_edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    return dp[m][n]

str1 = "kitten"
str2 = "sitting"
result = min_edit_distance(str1, str2)
print(result)
