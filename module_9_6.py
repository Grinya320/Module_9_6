def all_variants(text):
    a = len(text)
    for i in range(a):
        for y in range(i + 1, a + 1):
            yield text[i:y]


a = all_variants("abc")
for i in a:
    print(i)