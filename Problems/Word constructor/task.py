sone = input()
stwo = input()

empty_str = ''
for a, b in zip(sone, stwo):
    new_str_elem = (a, b)
    empty_str += ''.join(new_str_elem)

print(empty_str)

# password = ('nigc', (5, 4, 9, 6))
#
# password[0] + ''.join([str(x) for x in password[1]])