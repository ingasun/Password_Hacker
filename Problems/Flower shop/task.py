import itertools
# flower_names = ['rose', 'tulip', 'sunflower', 'bla']
#
# my_iter1 = itertools.combinations(flower_names, 1)
# my_iter2 = itertools.combinations(flower_names, 2)
# my_iter3 = itertools.combinations(flower_names, 3)
#
# print(next(my_iter2))
# for i in range(len(flower_names)):
#     print(next(my_iter1))
#
# for i in range(len(flower_names)):
#     print(next(my_iter2))
#
# print(next(my_iter3))


def r_subset(liste, r):
    # return list of all subsets of length r
    # to deal with duplicate subsets use
    # set(list(combinations(arr, r)))
    return list(itertools.combinations(liste, r))


# Driver Function
if __name__ == "__main__":
    iter_list1 = (r_subset(flower_names, 1))
    iter_list2 = (r_subset(flower_names, 2))
    iter_list3 = (r_subset(flower_names, 3))
    for i in range(len(iter_list1)):
        print(iter_list1[i])
    for i in range(len(iter_list2)):
        print(iter_list2[i])
    for i in range(len(iter_list3)):
        print(iter_list3[i])