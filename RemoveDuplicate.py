def remove_duplicates(sequence):
    print(sequence)
    unique = []
    for x in sequence:
        if x not in unique:
            unique.append(x)
    print(unique)
    return unique
