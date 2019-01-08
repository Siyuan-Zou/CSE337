import re

#Part 1
def noSpecialChar(s):
    i = 0
    while i < len(s):
        if not s[i].isalpha() and not s[i].isdigit():
            return False
        i += 1
    return True

def repeatedSubstring_len3(s):
    i = 0
    while i<len(s)-3:
        if s[i:i+3] in s[i+1:]:
            return True
        i+=1
    return False

def palindrome(s):
    i = 0
    while i < len(s)/2 + 1:
        if s[i] != s[-i-1]:
            return False
        i+=1
    return True

def notEnoughUniqueChar(s):
    c = list()
    i = 0
    while i < len(s):
        if s[i] not in c:
            c.append(s[i])
        i+=1
    if len(c) < len(s)/2:
        return True
    return False

def password_check(username, password):
    if len(password)>20 or len(password)<6:
        return False
    elif re.search('[0-9]', password) is None:
        return False
    elif re.search('[A-Z]', password) is None:
        return False
    elif noSpecialChar(password):
        return False
    elif repeatedSubstring_len3(password):
        return False
    elif palindrome(password):
        return False
    elif notEnoughUniqueChar(password):
        return False
    elif username in password or username[::-1] in password:
        return False
    return True

#Part2
username = input("Enter Your Username: ")
password = input("Enter Your Password: ")
while password_check(username, password) is False:
    password = input("Please Enter a Stronger Password: ")
print("Success")