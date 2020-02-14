a = str(input("Enter a string "))

a=a.casefold()

r = reversed(a)

if list(r)==list(a):
    print("the string is palindrome")
else:
    print("the is not a palindrome")

