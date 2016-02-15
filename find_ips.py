import os
import re
if not os.path.exists('out.txt'): open('out.txt', 'x').close()
with open('out.txt', 'w') as out_file:
    for file in os.listdir():
        temp_list = []
        if not os.path.isdir(file):
            with open(file) as f:
                for line in f:
                    matches = re.findall(r'\d+\.\d+\.\d+\.\d+', line)
                    if len(matches) > 0:
                        print(line)
                        temp_list.append(line)
            if len(temp_list) > 0:
                out_file.write('File ' + file + '\n')
                for l in temp_list:
                    out_file.write('    ' + l + '\n')
