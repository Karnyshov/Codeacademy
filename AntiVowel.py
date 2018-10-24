def anti_vowel(text):
    text_new = text
    for x in text:
        if x in "aeiouAEIOU":
            text_new = text_new.replace(x, "")
    print(text_new)
    return text_new


def anti_vowel1(text):
    final = ""
    vowel = "aeiouAEIOU"
    for x in text:
        if x not in vowel:
            final += x
    print(final)
    return final


anti_vowel("Hey look Words!")
anti_vowel1("Books!")
