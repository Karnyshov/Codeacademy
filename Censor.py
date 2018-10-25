def censor(text, word):
    process = text.split()
    for x in range(0, len(process)):
        if process[x] == word:
            process[x] = "*" * len(process[x])
    result = "".join(process)
    print(result)
    return result


censor("hey hey hey", "hey")
