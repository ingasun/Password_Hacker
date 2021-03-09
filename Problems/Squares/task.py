n = int(input())


def squares(zahl):
    for x in range(1, zahl + 1):
        yield x**2


squares1 = squares(n)
for x in squares1:
    print(x)

# Don't forget to print out the first n numbers one by one heren = int(input())
#
#
# squares1 = (x**2 for x in range(1, n+1))
#
# for x in squares1:
#     print(x)
#
# # Don't forget to print out the first n numbers one by one here