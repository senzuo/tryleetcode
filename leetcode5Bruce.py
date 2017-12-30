# 自己写的暴力求解

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    imax = len(s)
    longest = s[0]
    for k in range(imax - 1):
        # 两种情况考虑  1. xxxaaxxx 2.xxaxx
        # 但是 xxxaaaxxx GG
        # 只能乖乖都执行了……
        if s[k] == s[k + 1]:
            i, j = k, k + 1
            # while i > 0 and j < imax - 1 and s[i - 1] == s[j + 1]:
            #     i -= 1
            #     j += 1
            # if j - i + 1 > len(longest):
            #     longest = s[i: j + 1]
        else:
            i, j = k, k
        while i > 0 and j < imax - 1 and s[i - 1] == s[j + 1]:
            i -= 1
            j += 1
        if j - i + 1 > len(longest):
            longest = s[i: j + 1]

    return longest


# print(longestPalindrome('cbbd'))
# print(longestPalindrome('babad'))
# print(longestPalindrome('a'))
# print(longestPalindrome('bbb'))
# print('Wrong!')


# 人家的暴力求解
def longestPalindromeBruteForce(s):
    """
    :type s: str
    :rtype: str
    """
    ans, pal_str = 0, ''
    for i in range(len(s)):
        for j in range(i, len(s)):
            print(s[i:j + 1])
            if s[i:j + 1] == s[i:j + 1][::-1]:
                length = j - i + 1
                if length > ans:
                    ans = length
                    pal_str = s[i:j + 1]
    return pal_str


# print(longestPalindromeBruteForce('cbbd'))
print(longestPalindromeBruteForce('babad'))
# print(longestPalindromeBruteForce('a'))
# print(longestPalindromeBruteForce('bb'))


### 对比
# 出发点不同，自己的函数从每个点向两边拓展，别人的是检查每个字串是否是回文
# 自己函数效率稍微高一些，别人的函数代码简洁一些

