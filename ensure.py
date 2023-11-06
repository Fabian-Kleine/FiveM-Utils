import os

no_dir = ['stream', 'data', 'lib', 'gtav', 'gta_online', 'meta', 'client']

def process_directory(directory, f):
    for file in os.listdir(directory):
        d = os.path.join(directory, file)
        if os.path.isdir(d):
            dir_name = os.path.basename(d)
            if dir_name.startswith('[') and dir_name.endswith(']'):
                sub_dirs = [os.path.join(d, sub_dir) for sub_dir in os.listdir(d) if os.path.isdir(os.path.join(d, sub_dir))]
                for sub_dir in sub_dirs:
                    sub_dir_name = os.path.basename(sub_dir)
                    if sub_dir_name not in no_dir:
                        f.write('ensure ' + sub_dir_name + '\n')
                        process_directory(sub_dir, f)
            else:
                if dir_name not in no_dir and not any(char in dir_name for char in '[]'):
                    f.write('ensure ' + dir_name + '\n')
                    if any(char in dir_name for char in '[]'):
                        process_directory(d, f)

directory = input("resources directory:")

with open('output.txt', 'w') as f:
    f.write('ensure ' + os.path.basename(directory) + '\n')
    process_directory(directory, f)



