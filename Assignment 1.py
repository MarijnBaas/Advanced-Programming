def read_file(file):
    """
    Opens the file of the input and reads the contents into a number of sequences N and a list of the sequences.
 
    Args:
        file = string with the filepath (example "sample_sequence_set2.txt")
 
    Returns:
        N = integer of the amount of sequences to be processed
        lists = list of all the sequences to be processed
    """
    with open(file, 'r') as file:
        lines = file.readlines()
    N = int(lines[0])
    lists = []
    for line in lines[1:]:
        lists.append([int(x) for x in line.split()])
    return N, lists
#--------------------------------------------------------------------------------------------------------
def mutation_finder(source_list, target_list):
    """
    Checks the sequence aquired from the lists to the target sequence to locate all mutations
 
    Args:
        source_list = The source list aquired from the sample_sequence.txt which is altered during the running of the program
        target_list = List of ascending numbers of the same length as the source_list
 
    Returns:
        mutation = A list of all mutated indeces in the source_list when comparing to target_list

    """
    mutation = []
    for i in range(len(source_list)):
        if source_list[i] != target_list[i]:
            mutation.append(source_list[i])
    return mutation
#--------------------------------------------------------------------------------------------------------
def fastest_invert(mutation, source_list):
    """
    Makes a list of the shortest way to fix each individual invert without checking if this interferes 
    with other shortests ways of the other indeces.
 
    Args:
        mutation = A list of all mutated indeces in the source_list when comparing to target_list
        source_list = The source list aquired from the sample_sequence.txt which can is altered during the program
 
    Returns:
        inversion_list = A list of the shortest way to fix each invert in sublists (example [[1, 2, 3], [1, 2, 3], [4, 5], [4, 5], [7, 8, 9], [7, 8, 9]])

    """
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
    """
    Combines the same keys into a dictionary with as value the amount of times a request for inversion occured and as
    key the requested inversion. 
 
    Args:
        inversion_list = A list of the shortest way to fix each invert in sublists (example [[1, 2, 3], [1, 2, 3], [4, 5], [4, 5], [7, 8, 9], [7, 8, 9]])
 
    Returns:
        inv_dict = Dictionary with as value the amount of times a request for inversion occured and as
                    key the requested inversion

    """
    inv_dict = {}
    for sublist in inversion_list:
        sublist_tuple = tuple(sublist)
        if sublist_tuple in inv_dict:
            inv_dict[sublist_tuple] += 1
        else:
            inv_dict[sublist_tuple] = 1
    return inv_dict
#-------------------------------------------------------------------------------------------------------
def combine_overlapping_keys(dictionary):
    """
    Combines keys that are a subset of a larger key so [2,3,4,5] and [3,4] would be combined
 
    Args:
        dictionary = Dictionary with all keys of possible inversions
 
    Returns:
        new_dict = new dictionary with combined keys if they are overlapping

    """
    key_list = list(dictionary.keys())
    class_list = []
    new_dict = dictionary.copy()
    for i in range(len(key_list)):  
        for j in range(len(key_list)):
            if i != j and len(set(key_list[i]).intersection(set(key_list[j]))) == len(set(key_list[j])) and dictionary[key_list[i]] > 1:
                del new_dict[key_list[j]]
    return new_dict
#--------------------------------------------------------------------------------------------------------
def check_overlaps(new_dict):
    """
    Takes the new_dict and splits them up into lists of overlapping and non overlapping inversion requests.
 
    Args:
        new_dict = dictionary with as value the amount of times a inversion is requested and key a list of the inversion key
 
    Returns:
        overlapping = list of all inversion requests that overlap
        non_overlapping = list of all inversion requests that do not overlap

    """
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
    """
    Inverts the sequence depending on what inversion_key is given as input 
 
    Args:
        source_list = list on which you want to invert
        inversion_key = list of indeces you want to invert
        number = total amount of inversions done
        mutation_order = list with sublists which you append the new source_list to
 
    Returns:
        source_list = new source_list with inversion done
        number = amount of inversions done

    """
    start_index = min(inversion_key)  
    end_index = max(inversion_key) + 1  
    inverted_sublist = source_list[start_index:end_index][::-1]
    source_list[start_index:end_index] = inverted_sublist
    source_list_text = ' '.join(map(str, source_list)) 
    mutation_order.append(source_list_text)
    number = number+1
    return source_list, number
#--------------------------------------------------------------------------------------------------------
def inversion_loop(source_list, target_list):
    """
    Overshadowing function that calls all previous functions in order.
 
    Args:
        source_list = list on which you want to invert
        target_list = list you want source_list to reach through inversions
 
    Returns:
        overlapping = list of all inversion requests that overlap
        non_overlapping = list of all inversion requests that do not overlap

    """
    mutation = mutation_finder(source_list, target_list)
    inversion_list = fastest_invert(mutation, source_list)
    inv_dict = inversion_dict(inversion_list)
    new_dict = combine_overlapping_keys(inv_dict)
    non_overlapping, overlapping = check_overlaps(new_dict)
    return non_overlapping, overlapping
#--------------------------------------------------------------------------------------------------------
def inversion_mutations(file_name, new_file_name):
    """
    Final function that uses all predefined functions and writes the result into the output file
 
    Args:
        file_name = string of the file name you want to process in the programm
        new_file_name = string of the file name in which you want your output to be written
    Returns:
        None
    """
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
            non_overlapping, overlapping = inversion_loop(source_list, target_list)
            for i in range(len(non_overlapping)):
                source_list, number = invert_sequence(source_list, non_overlapping[i], number, mutation_order) 
            if len(overlapping) != 0:       
                longest_overlapping = max(overlapping, key=len)
                source_list, number = invert_sequence(source_list, longest_overlapping, number, mutation_order)
                #Can be rewritten to recursion to find the minimal invert sequence
        new_file.write(str(number))
        new_file.write('\n')
        new_file.write(source)
        new_file.write('\n')
        for k in range(len(mutation_order)):
            new_file.write(mutation_order[k])
            new_file.write('\n')
    new_file.close()

inversion_mutations('sample_sequence_set2.txt', 'solved_sample_sequence_set2.txt')