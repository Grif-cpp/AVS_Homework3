from Container import Container
import random
import sys
import time


def main(argv: list):
    global cont
    argc = len(argv)

    if argc == 4:
        # File input.
        if argv[1] == '-f':
            input_file = open(argv[2], 'r')
            output_file = open(argv[3], 'w')

            # Creating container.
            input_lines = input_file.readlines()
            cont = Container(int(input_lines[0]))

            # Filling container.
            input_lines = input_lines[1:]
            cont.file_in(input_lines)

            # Not sorted output.
            output_file.write('Filled Container \n')
            output_file.write(cont.out())

            # Sorting.
            cont.sorter()

            # Sorted output.
            output_file.write('Sorted Container \n')
            output_file.write(cont.out())

            # Closing.
            input_file.close()
            output_file.close()

        # Random input.
        elif argv[1] == '-n':
            output_file = open(argv[3], 'w')

            # Creating container.
            cont = Container(int(argv[2]))

            # Filling container.
            cont.random_in()

            # Not sorted output.
            output_file.write('Filled Container \n')
            output_file.write(cont.out())

            # Sorting.
            cont.sorter()

            # Sorted output.
            output_file.write('Sorted Container \n')
            output_file.write(cont.out())

            # Closing.
            output_file.close()

        else:
            print('Unknown argument:', argv[1])
            return
    else:
        print('Wrong number of arguments ')
        print('Needed:', 4)
        print('Got:', argc)
        return


if __name__ == '__main__':
    start = time.time()
    random.seed()
    main(sys.argv)
    end = time.time()
    # Time.
    print(str(end - start) + 'sec')
    # Memory.