# Richard Abdullah
# student number: 1739115
# ======================================================================================
def get_sequences(filepath):
    """
    Extracts DNA sequences from a given text file and returns
    a list containing the extracted sequences.
    """
    sequences = []
    with open(filepath) as f:
        for line in f:
            sequences.append(
                [int(i) for i in line.strip().split()]
            )  # Convert the string of numbers to a list
    return sequences


def get_wrong_pos(sequence):
    t = [
        x + 1 for x in range(len(sequence))
    ]  # Creates refference list to compare to the DNA sequence
    wrong_pos = []
    for x in t:
        if x != sequence[x - 1]:
            wrong_pos.append((x - 1, t.index(sequence[x - 1])))
    return wrong_pos


def locate_best_inversion(wrong_positions):
    """
    Given a list of all incorrect element positions within a sequence,
    locate the best inversion possible to minimize the number of inversions
    """
    if wrong_positions != []:
        inversion_selection = []  # Creates an empty list to store efficient inversions
        for element in wrong_positions:
            if (
                element[1],
                element[0],
            ) in wrong_positions:  # Checks if any inversion can be made that directly corrects two element positions
                if (
                    element[0] - 1,
                    element[1] + 1,
                ) in wrong_positions:  # Checks if the inversion is nested
                    wrong_positions.pop(wrong_positions.index(element))
                    continue
            if (
                element[0] + 1,
                element[1] - 1,
            ) in wrong_positions:  # Checks if the current element is positioned left to an element that preceeds current element
                inversion_selection.append(element)
            elif (
                element[0] + 1,
                element[1] + 1,
            ) in wrong_positions:  # Checks if the current element is positioned left to an element that succeeds current element
                inversion_selection.append(element)

        if len(inversion_selection) == 1:
            best_inversion = inversion_selection[
                0
            ]  # Skips any method of determining the best inversion if there is only one possibility
        elif inversion_selection == []:
            best_inversion = wrong_positions[
                0
            ]  # If a selection cannot be made, choose the first inversion from the input list as the best inversion
        elif len(inversion_selection) % 2 == 0:
            middle_inversion = int((len(inversion_selection) - 1) / 2)
            best_inversion = inversion_selection[
                middle_inversion
            ]  # Chooses to perform inversions from the inside to the outside of the DNA sequence
        else:
            best_inversion = inversion_selection[int(len(inversion_selection) / 2)]
    else:
        best_inversion = []
    return best_inversion


def perform_inversions(mutate_list):
    """
    Executes inversions on specific slices within a given sequence
    """
    wrong_positions = get_wrong_pos(
        mutate_list
    )  # Find the positions of the numbers that are not in the correct place
    k = 0  # Set initial counter for number of inversions
    intermediate_steps = []
    while wrong_positions != []:  # Checks if an inverse is required
        inversion = locate_best_inversion(wrong_positions)  # Finds the best inversion
        if inversion[0] > inversion[1]:
            inversion = (
                inversion[1],
                inversion[0],
            )  # Fixes problem caused by slicing with a higher value for the left bound  than the right bound

        original_slice = mutate_list[
            inversion[0] : inversion[1] + 1
        ]  # Creates slice of the segment containing all values between the left and right element in inversion and stores it
        flipped_slice = original_slice[::-1]  # Flips the stored slice
        mutate_list[inversion[0] : inversion[1] + 1] = (
            flipped_slice  # Substitute the inverted slice in the sequence
        )
        mutate_list_copy = [x for x in mutate_list]
        intermediate_steps.append(mutate_list_copy)
        wrong_positions = get_wrong_pos(
            mutate_list
        )  # Re-analyse the sequence for incorrect positions

        k += 1  # Increment inversion count
    return mutate_list, intermediate_steps, k


def inversion_mutations(input_file, output_file):
    file = get_sequences(input_file)
    with open(output_file, "w") as f:
        for sequence in file[1:]:
            original_sequence = [x for x in sequence]
            mutated_list, intermediate_steps, k = perform_inversions(sequence)
            f.write(str(k))
            f.write("\n")
            f.write(" ".join(str(x) for x in original_sequence))
            f.write("\n")
            for step in intermediate_steps:
                f.write(" ".join(str(x) for x in step))
                f.write("\n")
            f.write(" ".join(str(x) for x in mutated_list))
            f.write("\n")
    return output_file

inversion_mutations(r'C:\Users\20223809\Desktop\Universiteit\Jaar 2\Q4\Advanced Programming\Assignment 1\sample_sequence_set2.txt',r'C:\Users\20223809\Desktop\Universiteit\Jaar 2\Q4\Advanced Programming\Assignment 1\solved_sample_sequence_set2.txt')