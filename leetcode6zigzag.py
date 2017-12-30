def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    # numRows 个 str
    if numRows == 1:
        return s
    if numRows == 2:
        return s[::2] + s[1::2]
    lis = ['' for i in range(numRows)]
    j = 0
    direct = True
    for i in range(len(s)):
        lis[j] += s[i]

        if direct:
            j += 1
        else:
            j -= 1

        if j == numRows:
            j -= 2
            direct = not direct
        if j == -1:
            j += 2
            direct = not direct
    result = ''
    for s in lis:
        result += s
    return result


print(convert('PAYPALISHIRING', 3))
