def check_palindrome(word):
    word = word.lower()
    if word == word[::-1]:
        return True
    else:
        return False
    
print(check_palindrome("HeLLo"))

print(check_palindrome("abBA"))

print(check_palindrome("PALinDROmemORDnilap"))






#https://www.reddit.com/r/FreeCodeCamp/comments/18m1749/challenge_beginner_the_pythonic_palindrome_checker/
#This is where I learned word == word[::-1]:

