from itertools import product

pword = 'inga'

new_bla = list(map(''.join, product(*zip(pword.lower(), pword.upper()))))
print(new_bla)
for item in new_bla:
    print(item)


def allperm(password):
    return list(map(''.join, product(*zip(password.lower(), password.upper()))))


print(allperm(pword))