def solve(s):
    output = ''
    iter = 0
    q = s[::-1].replace(" ", "")

    for i in range(len(s)):
        if s[i] == ' ':
            output += ' '
        else:
            output += q[iter]
            iter += 1

    return output

'''
In this Kata, we are going to reverse a string while maintaining spaces.

For example:

solve("our code") = "edo cruo"
-- Normal reversal without spaces is "edocruo".
-- However, there is a space after the first three characters, hence "edo cruo"

solve("your code rocks") = "skco redo cruoy"
solve("codewars") = "srawedoc"

'''
