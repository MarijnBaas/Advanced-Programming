import random

def read_file(input_file):
    """
    Opens the file of the input and reads the contents and divides it into lists 
 
    Args:
        input_file = string with the filepath (example "sample_sequence_set2.txt")
 
    Returns:
        I_Parameters = list with move in index 0, kill in index 1 and growth in index 2 of I cells
        M_Parameters = list with move in index 0, kill in index 1 and growth in index 2 of M cells
        T_Parameters = list with move in index 0, kill in index 1 and growth in index 2 of T cells
        grid_size = integer of how large the grid is
        grid_buildup = list with sublists that contains all data of what cells are where
        number_of_iterations = integer with the amount if iterations the simulation should have
        seed = a integer used to define which seed random.seed should use
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
    number_of_iterations = int(lines[grid_size*2+10])
    seed = int(lines[grid_size*2+12])
    return I_Parameters,M_Parameters,T_Parameters,grid_size,grid_buildup,number_of_iterations,seed
    
    

class cell_type:
    """
    A class which represents a cell

    ...

    Attributes
    ----------
    move : int
        a integer which represents the ability of a cell to move and is used to calculate its probability
    kill : int
        a integer which represents the ability of a cell to kill and is used to calculate its probability
    growth : int
        a integer which represents the ability of a cell to duplicate itself and is used to calculate its probability
    location : list
        a list with its x position in the first index and y posisition in its second index

    Methods
    -------
    generate_action(probability, move, kill growth):
        generates an action for the cell to execute depending on its input parameters

    move_cells(location, grid_size, grid_buildup):
        executes the movement of a cell in the grid if the move action is selected
    
    """
    def __init__(self, move, kill, growth, location):
        self.move = move
        self.kill = kill
        self.growth = growth
        self.location = location

    def generate_action(self, probability, move, kill, growth):
        """
        Generates an action for the cell to do depending on input parameters
    
        Args:
            probability = random float of the probability of certain actions
            move = integer of the move ability of the cell
            kill = integer of the killing ability of the cell
            growth = integer of the growing ability of the cell
    
        Returns:
            action = string with what action the cell is going to do
        """
        action = 0
        if probability <= move/(move+kill+growth):          
            action = 'move'
        elif probability <= (move+kill)/(move+kill+growth): 
            action = 'kill'
        elif probability > (move+kill)/(move+kill+growth):
            action = 'growth'
        else:
            action = 'rest'
        return action

    def move_cells(self, location, grid_size, grid_buildup):
        """
        executes the movement of a cell in the grid if the move action is selected
    
        Args:
            location = list with its x position in the first index and y posisition in its second index
            grid_size = integer of how large the grid is
            grid_buildup = list with sublists that contains all data of what cells are where
    
        Returns:
            grid_buildup = list with sublists that contains all data of what cells are where
        """
        #Make a list of all possible cells that it can interact with
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        move_squares = []
        for direction in directions:
            new_row = location[0] + direction[0]
            new_col = location[1] + direction[1]
            if 0 <= new_row < grid_size and 0 <= new_col < grid_size:
                #If a neighbouring cell is empty add it to the list of possible moves
                if grid_buildup[new_row][new_col] == 'O':
                    move_squares.append([new_row, new_col])
        #If there are empty cells select at random one of the squares and move there
        if len(move_squares) > 0:
            choice = random.choice(move_squares) 
            new_location_row = choice[0]
            new_location_column = choice[1]
            grid_buildup[new_location_row][new_location_column] = grid_buildup[location[0]][location[1]]
            grid_buildup[location[0]][location[1]] = 'O'
        return grid_buildup



class Infected(cell_type):  
    """
    A class which represents a infected cell

    ...

    Attributes
    ----------
    move : int
        a integer which represents the ability of a cell to move and is used to calculate its probability
    kill : int
        a integer which represents the ability of a cell to kill and is used to calculate its probability
    growth : int
        a integer which represents the ability of a cell to duplicate itself and is used to calculate its probability
    location : list
        a list with its x position in the first index and y posisition in its second index

    
    Methods
    -------
    growth_cells(location, grid_size, grid_buildup):
        spawns another cell if the action growth is selected
    
    """    
    def __init__(self, move, kill, growth, location):
         super().__init__(move, kill, growth, location)

    def growth_cells(self, location, grid_size, grid_buildup):
        """
        executes the duplication of a cell in the grid if the growth action is selected
    
        Args:
            location = list with its x position in the first index and y posisition in its second index
            grid_size = integer of how large the grid is
            grid_buildup = list with sublists that contains all data of what cells are where
    
        Returns:
            grid_buildup = list with sublists that contains all data of what cells are where
        """
        #Make a list of all possible cells that it can interact with
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        growth_squares = []
        for direction in directions:
            new_row = location[0] + direction[0]
            new_col = location[1] + direction[1]
            if 0 <= new_row < grid_size and 0 <= new_col < grid_size:
                #If a neighbouring cell is empty add it to the list of possible moves
                if grid_buildup[new_row][new_col] == 'O':
                    growth_squares.append([new_row, new_col])
        #If there are empty cells select at random one of the squares and make another I cell there
        if len(growth_squares) > 0:
            choice = random.choice(growth_squares) 
            new_location_row = choice[0]
            new_location_column = choice[1]
            grid_buildup[new_location_row][new_location_column] = grid_buildup[location[0]][location[1]]
        return grid_buildup         


class MCell(cell_type):
    """
    A class which represents a macrophage cell

    ...

    Attributes
    ----------
    move : int
        a integer which represents the ability of a cell to move and is used to calculate its probability
    kill : int
        a integer which represents the ability of a cell to kill and is used to calculate its probability
    growth : int
        a integer which represents the ability of a cell to duplicate itself and is used to calculate its probability
    location : list
        a list with its x position in the first index and y posisition in its second index

    
    Methods
    -------
    kill_cells(location, grid_size, grid_buildup):
        kills a infected cell if it is present and the action kill is selected
    """    
    def __init__(self, move, kill, growth, location):
         super().__init__(move, kill, growth, location)

    def kill_cells(self, location, grid_size, grid_buildup):
        """
        executes the killing of a cell in the grid if the kill action is selected
    
        Args:
            location = list with its x position in the first index and y posisition in its second index
            grid_size = integer of how large the grid is
            grid_buildup = list with sublists that contains all data of what cells are where
    
        Returns:
            grid_buildup = list with sublists that contains all data of what cells are where
        """
        #Make a list of all possible cells that it can interact with
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        kill_squares = []
        for direction in directions:
            new_row = location[0] + direction[0]
            new_col = location[1] + direction[1]
            if 0 <= new_row < grid_size and 0 <= new_col < grid_size:
                #If a neighbouring cell is an I cell add it to the list of possible moves
                if grid_buildup[new_row][new_col] == 'I':
                    kill_squares.append([new_row, new_col])
        #If there are I cells select at random one of the squares and make delete the I cell there
        if len(kill_squares) > 0:
            choice = random.choice(kill_squares) 
            new_location_row = choice[0]
            new_location_column = choice[1]
            grid_buildup[new_location_row][new_location_column] = 'O'
        return grid_buildup

class TCell(cell_type):
    """
    A class which represents a t cell

    ...

    Attributes
    ----------
    move : int
        a integer which represents the ability of a cell to move and is used to calculate its probability
    kill : int
        a integer which represents the ability of a cell to kill and is used to calculate its probability
    growth : int
        a integer which represents the ability of a cell to duplicate itself and is used to calculate its probability
    location : list
        a list with its x position in the first index and y posisition in its second index

    
    Methods
    -------
    kill_cells(location, grid_size, grid_buildup):
        kills a infected cell if it is present, the action kill is selected and there is a macrophage adjecent to the t cell
    """    
    def __init__(self, move, kill, growth, location):
         super().__init__(move, kill, growth, location)
    
    def kill_cells(self, location, grid_size, grid_buildup):
        """
        executes the killing of a cell in the grid if the kill action is selected
    
        Args:
            location = list with its x position in the first index and y posisition in its second index
            grid_size = integer of how large the grid is
            grid_buildup = list with sublists that contains all data of what cells are where
    
        Returns:
            grid_buildup = list with sublists that contains all data of what cells are where
        """
        #Make a list of all possible cells that it can interact with
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        kill_squares = []
        can_kill = False
        for direction in directions:
            new_row = location[0] + direction[0]
            new_col = location[1] + direction[1]
            #If a neighbouring cell is an I cell add it to the list of possible moves and set can_kill to True
            #if there is a neighbouring M cell
            if 0 <= new_row < grid_size and 0 <= new_col < grid_size:
                if grid_buildup[new_row][new_col] == 'I':
                    kill_squares.append([new_row, new_col])
                elif grid_buildup[new_row][new_col] == 'M':
                    can_kill = True
        #If there are I cells and can_kill is True select at random one of the squares and make delete the I cell there
        if len(kill_squares) > 0 and can_kill == True:
            choice = random.choice(kill_squares) 
            new_location_row = choice[0]
            new_location_column = choice[1]
            grid_buildup[new_location_row][new_location_column] = 'O'
        return grid_buildup
        


def order_of_operations(grid_size, grid_buildup):
    """
    makes a list of where the cells are and in what order they should execute an action
    
    Args:
        grid_size = integer of how large the grid is
        grid_buildup = list with sublists that contains all data of what cells are where
    
    Returns:
        cell_locations = list with sublists of each cell locations in order of which should execute an action
    """
    cell_locations = []
    for rows in range(grid_size):
        for columns in range(grid_size):
            current_cell = grid_buildup[rows][columns]
            if current_cell == 'I' or current_cell == 'M' or current_cell == 'T':
                cell_locations.append([rows, columns])
    return cell_locations

def write_output(output_file, grid_buildup):
    """
    writes the final configuration of the grid into a output file
    
    Args:
        output_file = string of where you want to file and what the name should be
        grid_buildup = list with sublists that contains all data of what cells are where
    
    Returns:
        None
    """
    output_file = open(output_file, "w")   
    for i in range(len(grid_buildup)):
        grid_line = ' '.join(grid_buildup[i])
        output_file.write(grid_line)
        output_file.write('\n' + '\n')


def simulation(input_file, output_file):
    """
    executes all functions in the correct order 
    
    Args:
        input_file = string of what you want as input file and where it is
        output_file = string of where you want to file and what the name should be

    Returns:
        None
    """
    #Extract all data from input file
    I_Parameters,M_Parameters,T_Parameters,grid_size,grid_buildup,number_of_iterations,seed = read_file(input_file)
    #Make the random sequencen consistent by giving it a seed
    random.seed(seed)
    #loop over all iterations #number_of_iterations
    for i in range(number_of_iterations):         
        #get all locations with a cell in them
        cell_locations = order_of_operations(grid_size, grid_buildup)
        #generate random number for probability calculations
        for cells in range(len(cell_locations)):
            probability = random.random() #probability = random.seed(seed)
            #Check cell location and see what cell type is inside of them
            row = cell_locations[cells][0]
            column = cell_locations[cells][1]
            current_cell = grid_buildup[row][column]
            if current_cell == 'I':
                cell = Infected(I_Parameters[0], I_Parameters[1],I_Parameters[2], [row, column])
            elif current_cell == 'T':
                cell = TCell(T_Parameters[0], T_Parameters[1], T_Parameters[2], [row, column])
            elif current_cell =='M':
                cell = MCell(M_Parameters[0], M_Parameters[1], M_Parameters[2], [row, column])
            #See what action the cell will do depending on the probability and cell parameters
            action = cell.generate_action(probability, cell.move, cell.kill, cell.growth)
            if action == 'move':
                grid_buildup = cell.move_cells(cell.location, grid_size, grid_buildup)
            elif action == 'kill':
                grid_buildup = cell.kill_cells(cell.location, grid_size, grid_buildup)
            elif action == 'growth':
                grid_buildup = cell.growth_cells(cell.location, grid_size, grid_buildup)
            elif action == 'rest':
                print('Should not happen check code for logic errors when determining action')
    #Write the output of the simulation into the file
    write_output(output_file, grid_buildup)

            

simulation('initial_configuration1.txt','final_configuration.txt')