'''
Longest Palindrome

Find the length of the longest substring in the given string
's' that is the same in reverse.

As an example, if the input was “I like racecars that go fast”,
the substring (racecar) length would be 7.

If the length of the input string is 0, return value must be 0.

Example:
"a" -> 1
"aab" -> 2
"abcde" -> 1
"zzbaabcd" -> 4
'''

def longest_palindrome (s):
    s_rev = s[::-1]
    longest = 0

    for x in range(len(s)):
        for i in range(x,len(s)+1):
            if s_rev.find(s[x:i])>-1 and s[x:i]==s[x:i][::-1]:
                if longest < len(s[x:i]):
                    longest = len(s[x:i])
    return longest

longest_palindrome("baablkj12345432133d")
# Returns: 9
