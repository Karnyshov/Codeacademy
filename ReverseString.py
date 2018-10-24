def reverse(s):
    return "".join([s[x] for x in range(-1, (-len(s)-1), -1)])


def reverse1(text):
    new = ""
    for x in range(-1, (-len(text)-1), -1):
        new += text[x]
    print(new)
    return new


print(reverse("Hello"))
print(reverse1("World"))
