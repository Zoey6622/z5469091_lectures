def process_string(s):
    L = s.split()
    for i, word in enumerate(L):
        if i % 2 == 0:
            L[i] = word.lower()
        else:
            L[i] = word.upper()
    return L

def process_string(s):
    L = []
    for i, word in enumerate(s.split()):
        if i % 2 == 0:
            L.append(word.lower())
        else:
            L.append(word.upper())
    return L

# Testing
s = 'This is my test String'
process_string(s)

