def prnt(departments):
    with open('temp.txt', 'w') as f:
        f.write("".join(departments).strip())
    with open("temp.txt", 'r') as r, open('departments.txt', 'w') as o:
        for line in r:
            if line.strip():
                o.write(line)

