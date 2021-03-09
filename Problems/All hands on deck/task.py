
tiny_dict = {'2': 2, '3': 3, '4':4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
             'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

all_values_added = 0
for item in range(6):
    user_input = input()
    value = (tiny_dict.get(user_input))
    all_values_added = all_values_added + value

average = all_values_added / 6
print(average)


deck = {str(i): i for i in range(2, 11)}
print(deck)