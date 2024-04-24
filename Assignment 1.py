#source = '3 2 1 4 8 7 6 5 9'
#source = '3 2 1 8 4 7 6 5 9'
source = '1 2 5 4 6 3 7 8 9'
target = '1 2 3 4 5 6 7 8 9'

source_list = source.split()
for i in range(len(source_list)):
    source_list[i] = int(source_list[i])

target_list = target.split()
for i in range(len(target_list)):
    target_list[i] = int(target_list[i])

def mutation_finder(source_list, target_list):
    mutation = []
    for i in range(len(source_list)):
        if source_list[i] != target_list[i]:
            mutation.append(source_list[i])
    return mutation

def fastest_invert(mutation, source):
    inversion_list = []
    for i in range(len(mutation)):
        target_index = mutation[i]-1
        current_index = int(source.index(str(mutation[i]))/2)
        min_list = min(current_index, target_index)
        max_list = max(current_index, target_index)+1
        invert_list = list(range(min_list, max_list))
        inversion_list.append(invert_list)
    return inversion_list

def inversion_dict(inversion_list):
    inv_dict = {}
    for sublist in inversion_list:
        sublist_tuple = tuple(sublist)
        if sublist_tuple in inv_dict:
            inv_dict[sublist_tuple] += 1
        else:
            inv_dict[sublist_tuple] = 1
    return inv_dict

def check_overlapping_keys(dictionary):
    overlapping_list = []
    keys = list(dictionary.keys())
    for i in range(len(keys)):
        overlapping = False
        for j in range(len(keys)):
            if i != j and len(set(keys[i]).intersection(set(keys[j]))) > 0:
                overlapping = True
                break
        overlapping_list.append(overlapping)
    return overlapping_list

def invert_sequence(source_list, inversion_key): 
    start_index = min(inversion_key)  
    end_index = max(inversion_key) + 1  
    inverted_sublist = source_list[start_index:end_index][::-1]
    source_list[start_index:end_index] = inverted_sublist
    return source_list

def inversion_mutations(source_list, target_list):
    mutation =[0]
    while len(mutation) != 0:
        print(source_list)
        mutation = mutation_finder(source_list, target_list)
        inversion_list = fastest_invert(mutation, source)
        inv_dict = inversion_dict(inversion_list)
        overlapping_list = check_overlapping_keys(inv_dict)
        for i in range(len(overlapping_list)):
            if overlapping_list[i] == False:
                inversion_key = list(inv_dict.keys())[i]
                source_list = invert_sequence(source_list, inversion_key)
            else:
                print()

inversion_mutations(source_list,target_list)