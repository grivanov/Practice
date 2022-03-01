def pairs_sum_to_target(list1, list2, target):
    # Write your code here.
    result_list = list()

    for idx, elem in enumerate(list1):
        for index, sub_el in enumerate(list2):
            if elem + sub_el == target:
                result_list.append([idx, index])
    
    return(result_list)


list1 = [1, -2, 4, 5, 9]
list2 = [4, 2, -4, -4, 0]
target = 5

pairs_sum_to_target(list1, list2, target)
