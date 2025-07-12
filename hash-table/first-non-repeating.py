# Find first non-repeating character

def first_non_repeating(str):
    str = str.lower()
    count = {}

    #find counts
    for c in str:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

    for c in str:
        if count[c] == 1:
            return c
    return None


string = "a Green apple"
print("first non repeating character:", first_non_repeating(string))


