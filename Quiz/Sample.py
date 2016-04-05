'''
Created on Sep 15, 2014

@author: John
'''


def palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and palindrome(s[1:-1])

'''
def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return palindrome(s[1:-1])
'''

if __name__ == '__main__':
    
    import sys
    s = sys.stdin.readline().strip()
    print(palindrome(s))