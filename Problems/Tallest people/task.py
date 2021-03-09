
from collections import OrderedDict
# persons = {"Laura": 170, "Robin": 190, "Paul": 190}
# max_value_list = [(k) for (k), v in persons.items() if v == max(persons.values())]
# print(sorted(max_value_list))
# new_dict = {}
# for name, height in persons.items():
#     if name in max_value_list:
#         new_dict.update({name: height})
#         print(f'{name} : {height}')
# last_try = (OrderedDict(sorted(new_dict.items())))
# print(last_try)
# for name, height in last_try.items():
#     print(f'{name} : {height}')



def tallest_people(**persons):
    max_value_list = [(k) for (k), v in persons.items() if v == max(persons.values())]
    # print(sorted(max_value_list))
    # new_dict = {}
    for name, height in sorted(persons.items()):
        if name in max_value_list:
            # new_dict.update({name: height})
            print(f'{name} : {height}')
    # last_try = (OrderedDict(sorted(new_dict.items())))
    # # print(last_try)
    # for name, height in last_try.items():
    #     print(f'{name} : {height}')


# # Name : height
# def say_bye(**names):
#     for name in names:
#         print("Au revoir,", name)
#         print("See you on", names[name]["next appointment"])
#         print()
#
#
# humans = {"Laura": {"next appointment": "Tuesday"},
#           "Robin": {"next appointment": "Friday"}}
#
# say_bye(**humans)

# Au revoir, Laura
# See you on Tuesday
#
# Au revoir, Robin
# See you on Friday