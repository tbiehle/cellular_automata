from sys import argv
import random
from time import sleep
import curses

def main(stdscr, generations, rule) -> None:
    num_rows, num_cells = stdscr.getmaxyx()

    #cells = randomize_cells(num_cells)
    cells = ' ' * (num_cells // 2) + 'X' + ' ' * (num_cells // 2 - 5)
    ruleset = generate_ruleset(rule)

    gen = 0
    while gen < generations:
        # Clear the first line
        stdscr.move(0, 0)
        stdscr.deleteln()

        # Move cursor to the last line
        stdscr.move(num_rows - 1, 0)

        # Print new line
        for cell in cells:
            if cell == 'X':
                stdscr.addch('O')
            else:
                stdscr.addch(' ')
        
        cells = make_new_generation(cells, ruleset)
        gen += 1
        stdscr.refresh()
        sleep(0.05)

def randomize_cells(num_cells) -> str:
    """Generate a random list of zeroes and ones of specified length."""
    cells = ''.join([random.choice([' ', 'X']) for i in range(num_cells)])
    return cells

def make_new_generation(cur_gen, ruleset) -> str:
    """Creates the next generation of cells from previous generation"""
    new_gen = ''

    for i in range(len(cur_gen)):
        left_mid_right = cur_gen[i - 1:i + 2]  # list [left neighbour, current cell, right neighbor]

        if i == 0:
            left_mid_right = cur_gen[-1] + cur_gen[i] + cur_gen[i + 1]
        elif i == len(cur_gen) - 1:
            left_mid_right = cur_gen[i - 1] + cur_gen[i] + cur_gen[0] 

        new_gen += ruleset[left_mid_right]
    
    return new_gen

def generate_ruleset(rule) -> dict:
    """Generates a ruleset based on the rule number"""
    rule_bin_list = [' '] * 8
    bin_rule = format(rule, '08b')  # convert to binary and pad with leading zeros
    for i, letter in enumerate(bin_rule):
        rule_bin_list[i] = 'X' if letter == '1' else ' '

    ruleset = {
        'XXX': rule_bin_list[0],
        'XX ': rule_bin_list[1],
        'X X': rule_bin_list[2],
        'X  ': rule_bin_list[3],
        ' XX': rule_bin_list[4],
        ' X ': rule_bin_list[5],
        '  X': rule_bin_list[6],
        '   ': rule_bin_list[7]
    }

    return ruleset

if __name__ == "__main__":
    generations = int(argv[1])
    rule = int(argv[2])
    curses.wrapper(main, generations, rule)
