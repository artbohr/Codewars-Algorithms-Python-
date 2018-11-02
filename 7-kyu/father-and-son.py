def sc(s):
    return ''.join([x for x in s if s.count(x.lower())>0 and s.count(x.upper())>0])

'''
#Task:

Every uppercase letter is a Father, The corresponding lowercase letters is the Son.

Given the string ```s```, If the father and son both exist, keep them. If it is
a separate existence, delete them. Return the result.

For example:

```sc("Aab")``` should return ```"Aa"```

```sc("AabBc")``` should return ```"AabB"```

```sc("AaaaAaab")``` should return ```"AaaaAaa"```(father can have a lot of childs)

```sc("aAAAaAAb")``` should return ```"aAAAaAA"```(childs can also have a lot of parents)

'''
