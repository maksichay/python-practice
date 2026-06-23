
def is_palindrome(word):
    clean_word = word.lower()
    return clean_word == clean_word[::-1]
user_word = input("Введите слово для проверки: ")
word_clean = user_word.replace(" ", "")
result = is_palindrome(word_clean)
print(result)