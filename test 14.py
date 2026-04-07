def is_palindrome(text):
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("Hello"))
print(is_palindrome("A man a plan a canal Panama"))