#Suppose we have a string S. We have to find the longest palindromic substring in S
#Assume the length of string S is 1000. If string "BABAC" - "BAB"
#for exe: google -> goog
#equal string


# b a b a bad : odd palidromes, center starts with letter
# bab
# c b b d: even palindromes, center starts with space / no letter
#O(n^2) and O(1)


'''
Define one matrix of order same as length of string and fill it with false
Major diagonal element as true, so DP[i,i] = True

for l in range 2 to length of S + 1
    for i in range 0 to length of S – l + 1
        end := i + l
        if l = 2, then
            if S[i] = S[end - 1], then
                DP[i, end - 1] = True, max_len := l, and start := i
        otherwise
            if S[i] = S[end - 1] and DP[i + 1, end - 2], then
                DP[i, end - 1] = True, max_len := l, and start := i
    return a substring of from index start to start + max_len
'''
class Solution(object):
   def longestPalindrome(self, s):
      dp = [[False for i in range(len(s))] for i in range(len(s))]
      for i in range(len(s)):
         dp[i][i] = True
      max_length = 1
      start = 0
      for l in range(2,len(s)+1):
         for i in range(len(s)-l+1):
            end = i+l
            if l==2:
               if s[i] == s[end-1]:
                  dp[i][end-1]=True
                  max_length = l
                  start = i
            else:
               if s[i] == s[end-1] and dp[i+1][end-2]:
                  dp[i][end-1]=True
                  max_length = l
                  start = i
      return s[start:start+max_length]
ob1 = Solution()
print(ob1.longestPalindrome("ABBABBC"))
