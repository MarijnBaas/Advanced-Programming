# def mutation_finder(source_list, target_list):
#     mutation = []
#     for i in range(len(source_list)):
#         if source_list[i] != target_list[i]:
#             mutation.append(source_list[i])
#     return mutation
#--------------------------------------------------------------------------------------------------------
# def fastest_invert(mutation, source):
#     inversion_list = []
#     for i in range(len(mutation)):
#         target_index = mutation[i]-1
#         current_index = source_list.index(mutation[i]) 
#         min_list = min(current_index, target_index)
#         max_list = max(current_index, target_index)+1
#         invert_list = list(range(min_list, max_list))
#         inversion_list.append(invert_list)
#     return inversion_list
#--------------------------------------------------------------------------------------------------------
# def inversion_dict(inversion_list):
#     inv_dict = {}
#     for sublist in inversion_list:
#         sublist_tuple = tuple(sublist)
#         if sublist_tuple in inv_dict:
#             inv_dict[sublist_tuple] += 1
#         else:
#             inv_dict[sublist_tuple] = 1
#     return inv_dict
#--------------------------------------------------------------------------------------------------------
# dictionary = {(0, 1, 2, 3): 2, (0, 1, 2): 2, (4, 5, 6, 7): 2, (5, 6): 2, (7, 8, 9): 1}
#
# def combine_overlapping_keys(dictionary):
#     key_list = list(dictionary.keys())
#     class_list = []
#     new_dict = dictionary.copy()
#     for i in range(len(key_list)):  
#         for j in range(len(key_list)):  
#             if i != j and len(set(key_list[i]).intersection(set(key_list[j]))) == len(set(key_list[j])):
#                 print(key_list[j])
#                 del new_dict[key_list[j]]
#     print(new_dict)
#
# combine_overlapping_keys(dictionary)
#--------------------------------------------------------------------------------------------------------

new_dict = {(0, 1, 2, 3): 2, (4, 5, 6, 7): 2, (7, 8, 9): 1}

def check_overlaps(new_dict):
    key_list = list(new_dict.keys())
    print(key_list)

check_overlaps(new_dict)

# #source = '1 2 6 4 5 3 7 8 9'    #simple nested
# #source = '2 1 4 3 6 5 8 7 9'   #multiple simple
# #source = '1 8 3 4 5 6 7 2 9'   #subset overlap
# source = '4 3 2 1 8 7 6 5 9'
# target = '1 2 3 4 5 6 7 8 9'

# source_list = source.split()
# for i in range(len(source_list)):
#     source_list[i] = int(source_list[i])

# target_list = target.split()
# for i in range(len(target_list)):
#     target_list[i] = int(target_list[i])


# def combine_overlapping_keys(dictionary):
#     key_list = list(dictionary.keys())
#     class_list = []
#     new_dict = dictionary.copy()
#     for i in range(len(key_list)):  
#         for j in range(len(key_list)):  
#             if i != j and len(set(key_list[i]).intersection(set(key_list[j]))) == len(set(key_list[j])):
#                 print(key_list[j])
#                 del new_dict[key_list[j]]
#     return new_dict

# def invert_sequence(source_list, inversion_key): 
#     start_index = min(inversion_key)  
#     end_index = max(inversion_key) + 1  
#     inverted_sublist = source_list[start_index:end_index][::-1]
#     source_list[start_index:end_index] = inverted_sublist
#     print(source_list)
#     return source_list

# def inversion_mutations(source_list, target_list):
#     mutation =[0]
#     print(source_list)
#     while len(mutation) != 0:
#     #for i in range(2):
#         mutation = mutation_finder(source_list, target_list)
#         inversion_list = fastest_invert(mutation, source)
#         inv_dict = inversion_dict(inversion_list)
#         inv_dict = combine_overlapping_keys(inv_dict)
#         correction_factor = 0
#         for i in range(len(overlapping_list)):
#             if overlapping_list[i] == 0:
#                 inversion_key = list(inv_dict.keys())[i]
#                 source_list = invert_sequence(source_list, inversion_key)
#                 correction_factor = correction_factor+1
#             elif overlapping_list[i] == 2:
#                 inversion_key = list(inv_dict.keys())[i-1]                     # -1 might form a problem as i dont know why it needs it
#                 source_list = invert_sequence(source_list, inversion_key)
#             else:
#                 print('x')

# inversion_mutations(source_list,target_list)