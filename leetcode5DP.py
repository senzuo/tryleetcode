def longestPalindromeDP(s):
    ans = ''
    max_len = 0
    n = len(s)
    DP = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        DP[i][i] = True
        max_len = 1
        ans = s[i]
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            DP[i][i + 1] = True
            ans = s[i:i + 2]
            max_len = 2
    for length in range(3, n + 1):
        for i in range(n - 2):
            j = i + length - 1
            if j < n and DP[i + 1][j - 1] and s[i] == s[j]:
                DP[i][j] = True
                max_len = length
                ans = s[i:j + 1]
    return ans


print(longestPalindromeDP('cbbd'))
print(longestPalindromeDP('babad'))
print(longestPalindromeDP('a'))
print(longestPalindromeDP('bb'))
print(longestPalindromeDP('bbb'))
