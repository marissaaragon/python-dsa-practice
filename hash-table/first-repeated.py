def first_repeated(str):
    seen = {}

    for c in str:
        if c in seen:
            return c
        else:
            seen[c] = 1
    return None

string = "a green apple"
print(first_repeated(string))