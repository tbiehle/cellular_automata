from sys import argv
import random

def main(num_cells, generations) -> None:
    cells = generate_cells(num_cells)

    gen = 0
    while gen <= generations:
        print(cells)
        cells = make_new_generation(cells)
        gen += 1

def generate_cells(num_cells) -> list[int]:
    """Generate a random list of zeroes and ones of specified length."""
    cells = [random.choice([0, 1]) for i in range(num_cells)]
    return cells

def make_new_generation(cells) -> list[int]:
    """Creates the next generation of cells from previous generation"""
    new_generation = [0] * len(cells) 

    for i in range(len(cells) - 3):
        prev_cells = cells[i:i + 3]

        match prev_cells:
            case [0, 0, 0]:
                new_generation[i] = 0
            case [0, 0, 1]:
                new_generation[i] = 1
            case [0, 1, 0]:
                new_generation[i] = 1
            case [0, 1, 1]:
                new_generation[i] = 1
            case [1, 0, 0]:
                new_generation[i] = 0
            case [1, 0, 1]:
                new_generation[i] = 1
            case [1, 1, 0]:
                new_generation[i] = 1
            case [1, 1, 1]:
                new_generation[i] = 0
    
    return new_generation
        

if __name__ == "__main__":
    num_cells = int(argv[1])
    generations = int(argv[2])
    main(num_cells, generations)
