# Для русского языка
russian_letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
                   'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ',
                   'ы', 'ь', 'э', 'ю', 'я']

# Для английского языка
english_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                   'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt_ceaser(text, rot):
    to_change = list(text)
    for i in range(0, len(text)):
        if to_change[i] in english_letters and to_change[i].islower():
            to_change[i] = english_letters[(english_letters.index(to_change[i]) + rot) % len(english_letters)]

        if to_change[i].lower() in english_letters and to_change[i].isupper():
            low_char = to_change[i].lower()
            to_change[i] = english_letters[(english_letters.index(low_char) + rot) % len(english_letters)].upper()

        if to_change[i] in russian_letters and to_change[i].islower():
            to_change[i] = russian_letters[(russian_letters.index(to_change[i]) + rot) % len(russian_letters)]

        if to_change[i].lower() in russian_letters and to_change[i].isupper():
            low_char = to_change[i].lower()
            to_change[i] = russian_letters[(russian_letters.index(low_char) + rot) % len(russian_letters)].upper()

    text = ''.join(to_change)
    return text