def read_reg(reg_name):
    try:
        with open(reg_name,'r') as fd:
            t = []
            x = []
            y = []
            o = []
            for line in fd:
                line_striped = line.strip()
                elements = line_striped.split()
                t.append(float(elements[0]))
                x.append(float(elements[1]))
                y.append(float(elements[2]))
                o.append(float(elements[3]))
            return False, t, x, y, o
    except IOError:
        print('El registro "', reg_name, '" no existe.')
        return True, 0, 0, 0, 0
