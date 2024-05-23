import random
import matplotlib.pyplot as plt
import numpy as np
import imageio
import io

def read_file(input_file):
    with open(input_file, 'r') as input_file:
        lines = input_file.readlines()
    I_Parameters = [int(x) for x in lines[0].split()]
    M_Parameters = [int(x) for x in lines[2].split()]
    T_Parameters = [int(x) for x in lines[4].split()]
    grid_size = int(lines[6])
    grid_buildup = []
    for i in range(grid_size):
        line = (i * 2) + 8
        grid_line = [*lines[line]]
        grid_line.pop(-1)
        grid_buildup.append(grid_line)
    number_of_iterations = int(lines[i * 2 + 10])
    seed = int(lines[i * 2 + 12])
    return I_Parameters, M_Parameters, T_Parameters, grid_size, grid_buildup, number_of_iterations, seed

class cell_type:
    def __init__(self, move, kill, growth, location):
        self.move = move
        self.kill = kill
        self.growth = growth
        self.location = location

    def generate_action(self, probability, move, kill, growth):
        action = 0
        if probability <= move / (move + kill + growth):
            action = 'move'
        elif probability <= (move + kill) / (move + kill + growth):
            action = 'kill'
        elif probability > (move + kill) / (move + kill + growth):
            action = 'growth'
        else:
            action = 'rest'
        return action

    def move_cells(self, location, grid_size, grid_buildup):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        move_squares = []
        for direction in directions:
            new_row = location[0] + direction[0]
            new_col = location[1] + direction[1]
            if 0 <= new_row < grid_size and 0 <= new_col < grid_size:
                if grid_buildup[new_row][new_col] == 'O':
                    move_squares.append([new_row, new_col])
        if len(move_squares) > 0:
            choice = random.choice(move_squares)
            new_location_row = choice[0]
            new_location_column = choice[1]
            grid_buildup[new_location_row][new_location_column] = grid_buildup[location[0]][location[1]]
            grid_buildup[location[0]][location[1]] = 'O'
        return grid_buildup

class Infected(cell_type):
    def __init__(self, move, kill, growth, location):
        super().__init__(move, kill, growth, location)

    def growth_cells(self, location, grid_size, grid_buildup):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        growth_squares = []
        for direction in directions:
            new_row = location[0] + direction[0]
            new_col = location[1] + direction[1]
            if 0 <= new_row < grid_size and 0 <= new_col < grid_size:
                if grid_buildup[new_row][new_col] == 'O':
                    growth_squares.append([new_row, new_col])
        if len(growth_squares) > 0:
            choice = random.choice(growth_squares)
            new_location_row = choice[0]
            new_location_column = choice[1]
            grid_buildup[new_location_row][new_location_column] = grid_buildup[location[0]][location[1]]
        return grid_buildup

class MCell(cell_type):
    def __init__(self, move, kill, growth, location):
        super().__init__(move, kill, growth, location)

    def kill_cells(self, location, grid_size, grid_buildup):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        kill_squares = []
        can_kill = False
        for direction in directions:
            new_row = location[0] + direction[0]
            new_col = location[1] + direction[1]
            if 0 <= new_row < grid_size and 0 <= new_col < grid_size:
                if grid_buildup[new_row][new_col] == 'I':
                    kill_squares.append([new_row, new_col])
                elif grid_buildup[new_row][new_col] == 'T':
                    can_kill = True
        if len(kill_squares) > 0 and can_kill == True:
            choice = random.choice(kill_squares)
            new_location_row = choice[0]
            new_location_column = choice[1]
            grid_buildup[new_location_row][new_location_column] = 'O'
        return grid_buildup

class TCell(cell_type):
    def __init__(self, move, kill, growth, location):
        super().__init__(move, kill, growth, location)

    def kill_cells(self, location, grid_size, grid_buildup):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        kill_squares = []
        can_kill = False
        for direction in directions:
            new_row = location[0] + direction[0]
            new_col = location[1] + direction[1]
            if 0 <= new_row < grid_size and 0 <= new_col < grid_size:
                if grid_buildup[new_row][new_col] == 'I':
                    kill_squares.append([new_row, new_col])
                elif grid_buildup[new_row][new_col] == 'M':
                    can_kill = True
        if len(kill_squares) > 0 and can_kill == True:
            choice = random.choice(kill_squares)
            new_location_row = choice[0]
            new_location_column = choice[1]
            grid_buildup[new_location_row][new_location_column] = 'O'
        return grid_buildup

def order_of_operations(grid_size, grid_buildup):
    cell_locations = []
    for rows in range(grid_size):
        for columns in range(grid_size):
            current_cell = grid_buildup[rows][columns]
            if current_cell == 'I' or current_cell == 'M' or current_cell == 'T':
                cell_locations.append([rows, columns])
    return cell_locations

def write_output(output_file, grid_buildup):
    with open(output_file, "w") as output_file:
        for i in range(len(grid_buildup)):
            grid_line = ' '.join(grid_buildup[i])
            output_file.write(grid_line)
            output_file.write('\n' + '\n')

def save_plot(grid_buildup, iteration, grid_size):
    color_map = {'O': 0, 'I': 1, 'M': 2, 'T': 3}
    grid_numeric = np.array([[color_map[cell] for cell in row] for row in grid_buildup])
    
    plt.figure(figsize=(8, 8))
    plt.imshow(grid_numeric, cmap='viridis', vmin=0, vmax=3)
    plt.title(f'Iteration {iteration}')
    plt.axis('off')
    
    # Create a legend
    colors = [plt.cm.viridis(i / 3) for i in range(4)]
    labels = ['Empty', 'Infected', 'MCell', 'TCell']
    patches = [plt.plot([], [], marker="s", ls="", mec=None, color=colors[i], label="{:s}".format(labels[i]))[0] for i in range(4)]
    plt.legend(handles=patches, bbox_to_anchor=(1, 1), loc='upper left', ncol=1)

    # Save the plot to a buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    plt.close()
    return buf

def create_video_from_images(output_filename, image_buffers, number_of_iterations):
    with imageio.get_writer(output_filename, mode='I', fps=2) as writer:
        for buf in image_buffers:
            image = imageio.imread(buf)
            writer.append_data(image)

def simulation(input_file, output_file):
    I_Parameters, M_Parameters, T_Parameters, grid_size, grid_buildup, number_of_iterations, seed = read_file(input_file)
    random.seed(seed)
    
    image_buffers = []
    for iteration in range(number_of_iterations):
        cell_locations = order_of_operations(grid_size, grid_buildup)
        for location in cell_locations:
            cell_type = grid_buildup[location[0]][location[1]]
            if cell_type == 'I':
                cell = Infected(I_Parameters[0], I_Parameters[1], I_Parameters[2], location)
            elif cell_type == 'M':
                cell = MCell(M_Parameters[0], M_Parameters[1], M_Parameters[2], location)
            elif cell_type == 'T':
                cell = TCell(T_Parameters[0], T_Parameters[1], T_Parameters[2], location)
            else:
                continue
            action = cell.generate_action(random.random(), cell.move, cell.kill, cell.growth)
            if action == 'move':
                grid_buildup = cell.move_cells(location, grid_size, grid_buildup)
            elif action == 'kill':
                grid_buildup = cell.kill_cells(location, grid_size, grid_buildup)
            elif action == 'growth':
                grid_buildup = cell.growth_cells(location, grid_size, grid_buildup)
        image_buffers.append(save_plot(grid_buildup, iteration, grid_size))

    create_video_from_images('simulation_video.mp4', image_buffers, number_of_iterations)
    write_output(output_file, grid_buildup)


simulation('initial_configuration1.txt','final_configuration.txt')