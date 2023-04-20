import re
def prnt(departments):
    with open('temp.txt', 'w') as f:
        f.write("".join(departments))
    with open("temp.txt", 'r') as r, open('departments.txt', 'w') as o:
        for line in r:
            if line.strip().split():
                o.write(re.sub('^\s+|\s+$', '', line))
                o.write('\n')
