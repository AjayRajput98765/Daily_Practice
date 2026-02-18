def is_palindrome(s):
    s = s.lower().replace(" ","")
    if s == s[::-1]:
        print("The string is a Palindrome")
    else:
        print("The string is not a palindrome")


string = input("Enter a string :")
is_palindrome(string)
