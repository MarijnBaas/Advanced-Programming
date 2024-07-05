def determine_class(number_of_amino_acids, codon_dict, trna_dict, amino_list):
    states = []
    amino_molecule_count = []

    for i in range(number_of_amino_acids):
        amino_name = amino_list[i][0]
        codon_number = amino_list[i][1]

        if codon_number in codon_dict:
            numbers = codon_dict[codon_number]

            cognates = numbers[0]
            amino_cognates = []
            for j in range(len(cognates)):
                amino_cognates.append([trna_dict[int(cognates[j])][0], trna_dict[int(cognates[j])][2]])

            near_cognates = numbers[1]
            amino_near_cognates = []
            for k in range(len(near_cognates)):
                amino_near_cognates.append([trna_dict[int(near_cognates[k])][0], trna_dict[int(near_cognates[k])][2]])

            found_cognate = False
            for l in range(len(amino_cognates)):
                if amino_name == amino_cognates[l][0]:
                    states.append('cognate')
                    amino_molecule_count.append(float(amino_cognates[l][1]))
                    found_cognate = True
                    break
            
            if not found_cognate:
                for m in range(len(amino_near_cognates)):
                    if amino_name == amino_near_cognates[m][0]:
                        states.append('near_cognate')
                        amino_molecule_count.append(float(amino_near_cognates[m][1]))
                        break
                else:
                    states.append('non_cognate')
                    amino_molecule_count.append(0)
        else:
            states.append('non_cognate')
            amino_molecule_count.append(0)

    return states, amino_molecule_count

def read_cognates(input_file):
    """
    Opens the cognate file and reads them into usable variables
 
    Args:
        input_file = string with the filepath (example "example_input.txt")
 
    Returns:
        codon_dict = dictionary with as key a codon and value a list with sublist in the form [[cognates], [near_cognates]]

    """
    codon_dict = {}
    with open(input_file, 'r') as file:
        lines = file.readlines()[1:]
    for line in lines:
        entries = line.split()
        for i in range(0, len(entries), 3):
            codon = entries[i]
            cognates = entries[i+1].split(',')
            if i+2 < len(entries) and entries[i+2]:
                near_cognates = entries[i+2].split(',')
            else:
                near_cognates = []
            codon_dict[codon] = [cognates, near_cognates]
    return codon_dict

def read_tRNAs(input_file):
    trna_dict = {}
    total_molecule_count = 0
    with open(input_file, 'r') as file:
        lines = file.readlines()[1:]

    for line in lines:
        line_list = line.split()
        one_letter_code = line_list[2]
        codon_count = len(line_list) - 5
        molecule_count = line_list[-1]
        total_molecule_count = total_molecule_count + float(molecule_count)
        good_codons = []
        for i in range(codon_count):
            good_codons.append(line_list[i+4])
        trna_dict[int(line_list[0])] = [one_letter_code, good_codons, molecule_count]
    return trna_dict, total_molecule_count


def read_file(input_file):
    """
    Opens the input file and reads it contents into usable variables
 
    Args:
        input_file = string with the filepath (example "example_input.txt")
 
    Returns:
        number_of_amino_acids = integer representing the amount of amino acids to be processed

    """
    lines = open(input_file, 'r').readlines()
    number_of_amino_acids = int(lines[0])
    amino_list = []
    for i in range(number_of_amino_acids):
        amino_list.append(lines[2+i*2].split())
    iteration_count = lines[4+i*2]
    return number_of_amino_acids, amino_list, iteration_count



class cognates:
    def binding_state(self, molecule_count, total_molecule_count, random, state):
        if molecule_count/total_molecule_count > random:
            state = state + 1
        else:
            state = 0
        
        return state


#Classes used for cognate, near cognate, no cognate

def simulation(input_file, output_file):
    import random

    #read the 3 input files
    number_of_amino_acids, amino_list, iteration_count = read_file("C:/Users/20223809/Desktop/Universiteit/Jaar 2/Q4/Advanced Programming/Extra Assignment 2/example_input.txt")
    codon_dict = read_cognates("C:/Users/20223809/Desktop/Universiteit/Jaar 2/Q4/Advanced Programming/Extra Assignment 2/CognatesAndNearCognatesPerCodon.txt")
    trna_dict, total_molecule_count = read_tRNAs("C:/Users/20223809/Desktop/Universiteit/Jaar 2/Q4/Advanced Programming/Extra Assignment 2/tRNAs.txt")

    #define paramters
    k2 = 190
    kminus1 = 85 
    k3c = 260
    k3nc = 0.40
    kminus2c = 0.23
    kminus2nc = 80
    k4c = 167
    krc = 60
    krnc = 1000

#calculating probability
    classes, amino_molecule_count = determine_class(number_of_amino_acids, codon_dict, trna_dict, amino_list)
    for i in range(number_of_amino_acids):

        if classes[i] == 'cognate':
            amino_acid = cognates()
        
        total_passes = 0
        for j in range(int(iteration_count)):
            state = 1
            done = False
            while done == False:
                probability = random.random()
                if state == 1:
                    state = amino_acid.binding_state(amino_molecule_count[i], total_molecule_count, probability, state)
                elif state == 2:
                    done = True
                    total_passes = total_passes + 1
                elif state == 3:
                    True
                    #Check state 3->2 transition or 3->4 transition
                elif state == 4:
                    True
                    #check state 4->5 transition or end
                elif state ==5:
                    True
                    #add 1 to succes rate
                else:
                    done = True
            print(total_passes)


        



simulation(1, 2)