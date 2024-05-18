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
    def __init__(self, move, location):
        self.move = move
        self.location = location

    def move_cell(location):
        True;

    def generate_action(move, kill, growth):
        True;


class Infected(cell_type):      #mobility, location, growth
    def __init__(self, move, location, growth):
         super().__init__(move,location)
         self.growth = growth
    
    def duplicate_cell(location):
        True;

class MCell(cell_type):
    def __init__(self, move, location, kill):
         super().__init__(move,location)
         self.kill = kill
        
    def kill_cell(location):    #check if there is a I cell in surrounding blocks and then 
        True;

class TCell(cell_type):
    def __init__(self, move, location, kill):
         super().__init__(move,location)
         self.kill = kill
        
    def kill_cell(location):
        True;

def order_of_operations(grid_size, grid_buildup):
    cell_locations = []
    for rows in range(grid_size):
        for columns in range(grid_size):
            current_cell = grid_buildup[rows][columns]
            if current_cell == 'I' or current_cell == 'M' or current_cell == 'T':
                cell_locations.append([rows, columns])
    return cell_locations



def simulation(input_file, output_file):
    I_Parameters,M_Parameters,T_Parameters,grid_size,grid_buildup,number_of_iterations,seed = read_file(input_file)

    cell_locations = order_of_operations(grid_size, grid_buildup)

    for i in range(1): #number_of_iterations
        for cells in range(len(cell_locations)):
                row = cell_locations[cells][0]
                column = cell_locations[cells][1]
                current_cell = grid_buildup[row][column]
                print(current_cell)
                if current_cell == 'I':
                    cell = Infected(I_Parameters[0], [row, column],I_Parameters[2])
                elif current_cell == 'T':
                    cell = TCell(T_Parameters[0], [row, column], T_Parameters[1])
                else:
                    cell = MCell(M_Parameters[0], [row, column], M_Parameters[1])

simulation('initial_configuration1.txt','final_configuration.txt')