def prnt(departments):
    with open('departments.txt', 'w') as f:
        f.write('\n'.join(departments))
