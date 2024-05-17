from collections import deque

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

def mutation_finder(source_list, target_list):
    """
    Checks the sequence acquired from the lists to the target sequence to locate all mutations.
 
    Args:
        source_list = The source list acquired from the sample_sequence.txt which is altered during the running of the program
        target_list = List of ascending numbers of the same length as the source_list
 
    Returns:
        mutation = A list of all mutated indices in the source_list when comparing to target_list
    """
    mutation = []
    for i in range(len(source_list)):
        if source_list[i] != target_list[i]:
            mutation.append(source_list[i])
    return mutation

def fastest_invert(mutation, source_list):
    """
    Makes a list of the shortest way to fix each individual invert without checking if this interferes 
    with other shortest ways of the other indices.
 
    Args:
        mutation = A list of all mutated indices in the source_list when comparing to target_list
        source_list = The source list acquired from the sample_sequence.txt which is altered during the program
 
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

def inversion_dict(inversion_list):
    """
    Combines the same keys into a dictionary with as value the amount of times a request for inversion occurred and as
    key the requested inversion.
 
    Args:
        inversion_list = A list of the shortest way to fix each invert in sublists (example [[1, 2, 3], [1, 2, 3], [4, 5], [4, 5], [7, 8, 9], [7, 8, 9]])
 
    Returns:
        inv_dict = Dictionary with as value the amount of times a request for inversion occurred and as
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

def combine_overlapping_keys(possible_inversions):
    """
    Combines keys that are a subset of a larger key so [2,3,4,5] and [3,4] would be combined.
 
    Args:
        possible_inversions = Dictionary with all keys of possible inversions
 
    Returns:
        combined_inversions = new dictionary with combined keys if they are overlapping
    """
    key_list = list(possible_inversions.keys())
    combined_inversions = possible_inversions.copy()
    to_delete = set()
    
    for i in range(len(key_list)):  
        for j in range(len(key_list)):
            if i != j and key_list[j] not in to_delete:
                if len(set(key_list[i]).intersection(set(key_list[j]))) == len(set(key_list[j])) and possible_inversions[key_list[i]] > 1:
                    to_delete.add(key_list[j])
                    
    for key in to_delete:
        if key in combined_inversions:
            del combined_inversions[key]
    
    return combined_inversions

def check_overlaps(combined_inversions):
    """
    Takes the new_dict and splits them up into lists of overlapping and non-overlapping inversion requests.
 
    Args:
        new_dict = dictionary with as value the amount of times an inversion is requested and key a list of the inversion key
 
    Returns:
        overlapping = list of all inversion requests that overlap
        non_overlapping = list of all inversion requests that do not overlap
    """
    key_list = list(combined_inversions.keys())
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

def invert_sequence(source_list, inversion_key): 
    """
    Inverts the sequence depending on what inversion_key is given as input.
 
    Args:
        source_list = list on which you want to invert
        inversion_key = list of indices you want to invert
 
    Returns:
        source_list = new source_list with inversion done
    """
    start_index = min(inversion_key)  
    end_index = max(inversion_key) + 1  
    inverted_sublist = source_list[start_index:end_index][::-1]
    source_list[start_index:end_index] = inverted_sublist
    return source_list

def minimal_inversions(source_list, target_list):
    """
    Uses BFS to find the minimal sequence of inversions to reach the target_list.
 
    Args:
        source_list = list on which you want to perform inversions
        target_list = list you want source_list to reach through inversions
 
    Returns:
        mutation_order = list of all the steps (inversions) taken to reach target_list
        num_inversions = total number of inversions performed
    """
    #make a tuple containing the current list the order of mutations and the amount of inversions done
    queue = deque([(source_list, [], 0)]) 

    #List of processed mutations to not do duplicates
    visited = set()
    visited.add(tuple(source_list))

    while queue:
        #print("yes")
        #Get the first element in the queue
        current_list, mutation_order, inversion_count = queue.popleft()
        #Check if there is mutations left
        if current_list == target_list:
            return mutation_order, inversion_count
        #Find the mutations
        mutation = mutation_finder(current_list, target_list)
        #Generate the list of possible moves
        inversion_list = fastest_invert(mutation, current_list)
        #Make a dictionary with the amount of times a move a requested
        possible_inversions = inversion_dict(inversion_list)
        #Combine the moves if they are overlapping
        combined_inversions = combine_overlapping_keys(possible_inversions)
        #Split them into non_overlapping and overlapping moves
        non_overlapping, overlapping = check_overlaps(combined_inversions)
        #Execute all possibilties
        for inv_key in non_overlapping + overlapping:
            new_list = current_list.copy()
            new_list = invert_sequence(new_list, inv_key)
            new_mutation_order = mutation_order + [new_list]
            if tuple(new_list) not in visited:
                visited.add(tuple(new_list))
                queue.append((new_list, new_mutation_order, inversion_count + 1))
        #I wanted to split the possibilities so that non_overlapping are executed first and then not looked at anymore
        #But I ran out of time

def inversion_mutations(file_name, new_file_name):
    """
    Final function that uses all predefined functions and writes the result into the output file.
 
    Args:
        file_name = string of the file name you want to process in the program
        new_file_name = string of the file name in which you want your output to be written
    Returns:
        None
    """
    N, sequences = read_file(file_name)
    new_file = open(new_file_name, "w")
    for j in range(N):
        source_list = sequences[j]
        target_list = sorted(source_list)
        mutation_order, number = minimal_inversions(source_list, target_list)
        new_file.write(str(number))
        new_file.write('\n')
        new_file.write(' '.join(map(str, source_list)))
        new_file.write('\n')
        for step in mutation_order:
            new_file.write(' '.join(map(str, step)))
            new_file.write('\n')
    new_file.close()

inversion_mutations('test_sequence_set.txt', 'solved_test_set.txt')
