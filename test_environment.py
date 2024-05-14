def read_file(file):
    with open(file, 'r') as file:
        lines = file.readlines()
    N = int(lines[0])
    lists = []
    for line in lines[1:]:
        lists.append([int(x) for x in line.split()])
    return N, lists

def mutation_finder(source_list, target_list):
    mutation = []
    for i in range(len(source_list)):
        if source_list[i] != target_list[i]:
            mutation.append(source_list[i])
    return mutation
#--------------------------------------------------------------------------------------------------------
def fastest_invert(mutation, source_list):
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
            if i != j and len(set(key_list[i]).intersection(set(key_list[j]))) == len(set(key_list[j])) and dictionary[key_list[i]] > 1:
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
def invert_sequence(source_list, inversion_key, number, mutation_order): 
    start_index = min(inversion_key)  
    end_index = max(inversion_key) + 1  
    inverted_sublist = source_list[start_index:end_index][::-1]
    source_list[start_index:end_index] = inverted_sublist
    #print(source_list)
    source_list_text = ' '.join(map(str, source_list)) 
    mutation_order.append(source_list_text)
    number = number+1
    return source_list, number
#--------------------------------------------------------------------------------------------------------
# source_list = [1, 2, 3, 4, 5, 9, 6, 8, 7]
# target_list =[1,2,3,4,5,6,7,8,9]
# source = '1 2 3 4 5 9 6 8 7'

def inversion_loop(source_list, target_list):
    mutation = mutation_finder(source_list, target_list)
    inversion_list = fastest_invert(mutation, source_list)
    inv_dict = inversion_dict(inversion_list)
    new_dict = combine_overlapping_keys(inv_dict)
    non_overlapping, overlapping = check_overlaps(new_dict)
    return non_overlapping, overlapping

#non_overlapping, overlapping = inversion_loop(source_list, target_list, source)

def inversion_mutations(file_name, new_file_name):
    N, sequences = read_file(file_name)
    new_file = open(new_file_name, "w")
    for j in range(N):
        mutation_order = []
        source_list = sequences[j]
        target_list = sorted(source_list)
        source = ' '.join(map(str, source_list))
        number = 0
        non_overlapping, overlapping =[0], [0]
        while len(non_overlapping)!= 0 or len(overlapping) != 0:
            non_overlapping, overlapping = inversion_loop(source_list, target_list )
            for i in range(len(non_overlapping)):
                source_list, number = invert_sequence(source_list, non_overlapping[i], number, mutation_order) 
            if len(overlapping) != 0:       
                longest_overlapping = max(overlapping, key=len)
                source_list, number = invert_sequence(source_list, longest_overlapping, number, mutation_order)
        new_file.write(str(number))
        new_file.write('\n')
        new_file.write(source)
        new_file.write('\n')
        for k in range(len(mutation_order)):
            new_file.write(mutation_order[k])
            new_file.write('\n')
    new_file.close()

#horror sequence = 7 6 1 9 8 2 10 5 3 4

inversion_mutations('sample_sequence_set2.txt', 'solved_sample_sequence_set2.txt')