def palindrome(word):
    for x in range(len(word)):
        if word[x]!=word[(len(word)-1)-x]:
            return False
        else:
            return True
word=input()
print(palindrome(word))