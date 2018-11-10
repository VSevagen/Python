def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

print("Enter a word: ")
s = input()

print (s)
print(reverse(s))

if reverse(s) == s:
    print("s is a palindrome")
else:
    print("s is not a palindrome")