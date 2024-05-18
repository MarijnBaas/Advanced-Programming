import random

def read_file(input_file):
    """
    Opens the file of the input and reads the contents and divides it into lists 
 
    Args:
        input_file = string with the filepath (example "sample_sequence_set2.txt")
 
    Returns:

    """
    with open(input_file, 'r') as input_file:
        lines = input_file.readlines()
    I_Parameters = [int(x) for x in lines[0].split()]
    M_Parameters = [int(x) for x in lines[2].split()]
    T_Parameters = [int(x) for x in lines[4].split()]
    grid_size = int(lines[6])
    grid_buildup = []
    for i in range(grid_size):
        line = (i*2)+8
        grid_line = [*lines[line]]
        grid_line.pop(-1)
        grid_buildup.append(grid_line)
    number_of_iterations = int(lines[18])
    seed = int(lines[20])
    return I_Parameters,M_Parameters,T_Parameters,grid_size,grid_buildup,number_of_iterations,seed
    
    

class cell_type:
    def __init__(self, move, kill, growth, location):
        self.move = move
        self.kill = kill
        self.growth = growth
        self.location = location

    def move_cell(location):
        True;

    def generate_action(self, probability, move, kill, growth):
        action = 0
        if probability <= move/(move+kill+growth):          #0.5/0.3
            action = 'move'
        elif probability <= (move+kill)/(move+kill+growth): #1/1
            action = 'kill'
        elif probability > (move+kill)/(move+kill+growth):
            action = 'growth'
        else:
            action = 'rest'
        return action

    #def get_move_squares(self, location):




class Infected(cell_type):      #mobility, location, growth
    def __init__(self, move, kill, growth, location):
         super().__init__(move, kill, growth, location)

class MCell(cell_type):      #mobility, location, growth
    def __init__(self, move, kill, growth, location):
         super().__init__(move, kill, growth, location)

class TCell(cell_type):      #mobility, location, growth
    def __init__(self, move, kill, growth, location):
         super().__init__(move, kill, growth, location)
        


def order_of_operations(grid_size, grid_buildup):
    cell_locations = []
    for rows in range(grid_size):
        for columns in range(grid_size):
            current_cell = grid_buildup[rows][columns]
            if current_cell == 'I' or current_cell == 'M' or current_cell == 'T':
                cell_locations.append([rows, columns])
    return cell_locations



def simulation(input_file, output_file):
    #Extract all data from input file
    I_Parameters,M_Parameters,T_Parameters,grid_size,grid_buildup,number_of_iterations,seed = read_file(input_file)
    for i in range(1):     #loop over all iterations #number_of_iterations    
        #get all locations with a cell in them
        cell_locations = order_of_operations(grid_size, grid_buildup)
        #generate random number for probability calculations
        probability = random.random()
        for cells in range(len(cell_locations)):
            #Check cell location and see what cell type is inside of them
            row = cell_locations[cells][0]
            column = cell_locations[cells][1]
            current_cell = grid_buildup[row][column]
            if current_cell == 'I':
                cell = Infected(I_Parameters[0], I_Parameters[1],I_Parameters[2], [row, column])
            elif current_cell == 'T':
                cell = TCell(T_Parameters[0], T_Parameters[1], T_Parameters[2], [row, column])
            else:
                cell = MCell(M_Parameters[0], M_Parameters[1], M_Parameters[2], [row, column])
            #See what action the cell will do depending on the probability and cell parameters
            action = cell.generate_action(probability, cell.move, cell.kill, cell.growth)
            print(action)
            

            
                
                

simulation('initial_configuration1.txt','final_configuration.txt')