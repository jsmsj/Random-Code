from itertools import combinations

_list = [i+1 for i in range(10)]
required_sum = 13

def subset_of_length_i(array,i):
    return list(combinations(array,i))

def subsets_of_a_set(_set):
    all_subsets = []
    for i in range(len(_set)):
        all_subsets.extend(subset_of_length_i(_set,i))
    return all_subsets

def sum_func(array,number):
    temp = []
    all_subsets = subsets_of_a_set(array)
    for j in all_subsets:
        if sum(j) == number:
            temp.append(j)
    return temp

possible_subsets = sum_func(_list,required_sum)

print(f"The possible numbers that can add up to {required_sum} from the given list of numbers ( {_list} ) are:")

for i in possible_subsets:
    print(f"{' + '.join(map(str,i))} = {required_sum}")
