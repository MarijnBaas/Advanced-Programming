def mutation_finder(source_list, target_list):
    mutation = []
    for i in range(len(source_list)):
        if source_list[i] != target_list[i]:
            mutation.append(source_list[i])
    return mutation
#--------------------------------------------------------------------------------------------------------
def fastest_invert(mutation, source):
    inversion_list = []
    for i in range(len(mutation)):
        target_index = mutation[i]-1
        current_index = source_list.index(mutation[i]) 
        min_list = min(current_index, target_index)
        max_list = max(current_index, target_index)+1
        invert_list = list(range(min_list, max_list))
        inversion_list.append(invert_list)
    return inversion_list
#--------------------------------------------------------------------------------------------------------
def inversion_dict(inversion_list):
    inv_dict = {}
    for sublist in inversion_list:
        sublist_tuple = tuple(sublist)
        if sublist_tuple in inv_dict:
            inv_dict[sublist_tuple] += 1
        else:
            inv_dict[sublist_tuple] = 1
    return inv_dict
#--------------------------------------------------------------------------------------------------------
#dictionary = {(0, 1, 2, 3): 2, (0, 1, 2): 2, (4, 5, 6, 7): 2, (5, 6): 2, (7, 8, 9): 1}

def combine_overlapping_keys(dictionary):
    key_list = list(dictionary.keys())
    class_list = []
    new_dict = dictionary.copy()
    for i in range(len(key_list)):  
        for j in range(len(key_list)):  
            if i != j and len(set(key_list[i]).intersection(set(key_list[j]))) == len(set(key_list[j])):
                del new_dict[key_list[j]]
    return new_dict
#--------------------------------------------------------------------------------------------------------
#new_dict = {(0, 1, 2, 3): 2, (4, 5, 6, 7): 2, (7, 8, 9): 1}

def check_overlaps(new_dict):
    key_list = list(new_dict.keys())
    overlapping_list = []
    non_overlapping = []
    overlapping = []
    for i in range(len(key_list)):
        overlapping_count = 0
        for j in range(len(key_list)):
            if i != j:
                overlapping_count += len(set(key_list[i]).intersection(set(key_list[j])))
        overlapping_list.append(overlapping_count)
    for i in range(len(key_list)):
        if overlapping_list[i] == 0:
            non_overlapping.append(key_list[i])
        else:
            overlapping.append(key_list[i])
    return non_overlapping, overlapping
#--------------------------------------------------------------------------------------------------------
def invert_sequence(source_list, inversion_key): 
    start_index = min(inversion_key)  
    end_index = max(inversion_key) + 1  
    inverted_sublist = source_list[start_index:end_index][::-1]
    source_list[start_index:end_index] = inverted_sublist
    print(source_list)
    return source_list
#--------------------------------------------------------------------------------------------------------
source_list = [1, 2, 6, 5, 4, 3, 7, 8, 9]
target_list =[1,2,3,4,5,6,7,8,9]
source = '1 2 6 5 4 3 7 8 9'

# def inversion_loop(source_list, target_list, source):
#     mutation = mutation_finder(source_list, target_list)
#     inversion_list = fastest_invert(mutation, source)
#     inv_dict = inversion_dict(inversion_list)
#     new_dict = combine_overlapping_keys(inv_dict)
#     non_overlapping, overlapping = check_overlaps(new_dict)
#     return non_overlapping, overlapping

# non_overlapping, overlapping = inversion_loop(source_list, target_list, source)

def inversion_mutations(source_list, target_list):
    print(source_list)
    mutation =[0]
    while len(mutation) != 0:
        mutation = mutation_finder(source_list, target_list)
        inversion_list = fastest_invert(mutation, source)
        inv_dict = inversion_dict(inversion_list)
        new_dict = combine_overlapping_keys(inv_dict)
        non_overlapping, overlapping = check_overlaps(new_dict)
        for i in range(len(non_overlapping)):
            invert_sequence(source_list, non_overlapping[i])

inversion_mutations(source_list, target_list)
#plan is to put a part of inversion mutation into a combined function and than calling that again on a
#sublist of the new sequences made by the overlapping mutation sequences.

