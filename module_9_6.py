def all_variants(text):
    for n in range(len(text)):
        for j in range(n+1, len(text)+1):
            yield text[n:j]


gen = all_variants('abc')
for i in gen:
    print(i)
