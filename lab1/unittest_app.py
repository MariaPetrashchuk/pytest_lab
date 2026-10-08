def check_number(number):
    assert number > 0, "Число має бути більшим за нуль!"
    return True


def count_vowels(text):
    vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯaeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def get_number():
    number = input("Введіть число: ")
    return number