def tokenize(expression):
    parts = expression.split()
    print(parts)
    for i in parts:
        if keywords.__contains__(i):
            keywords[i] += 1
        elif operators.__contains__(i):
            operators[i] += 1
        elif booleans.__contains__(i):
            booleans[i] += 1
        elif i.isnumeric():
            if numbers.__contains__(i):
                numbers[i] += 1
            else:
                numbers[i] = 1
        else:
            if identifiers.__contains__(i):
                identifiers[i] += 1
            else:
                identifiers[i] = 1


identifiers = dict()
keywords = dict([
    ("si", 0), # if
    ("otro", 0), # else
    ("cuando", 0), # while
    ("para", 0), # for
    ("cambia", 0) # switch
    ])
numbers = dict()
booleans = dict([
    ("cierto", 0), # true
    ("falso", 0) # false
    ])
operators = dict([
    ("+", 0),
    ("-", 0),
    ("*", 0),
    ("/", 0),
    ("%", 0),
    ("=", 0),
    ("==", 0)])

token = ""
tokenize(token)