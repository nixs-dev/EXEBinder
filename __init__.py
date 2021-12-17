from Generator import Generator
import sys


# Handle args and get data for start operation

args = sys.argv
args.pop(0)

files_to_bind = []
result_file = ''

if '-o' in args:
    name_index = args.index('-o') + 1
    result_file = args[name_index]

    args.pop(name_index)
    args.pop(name_index - 1)
else:
    result_file = 'result'

files_to_bind = args

confirm = input(f'{" + ".join(files_to_bind)} = {result_file + ".exe"}\n\nDo you really want to do that ?[y/n]')

if confirm.lower() == 'n':
    print('Operation cancelled')
    sys.exit()

Generator(files_to_bind, result_file)
