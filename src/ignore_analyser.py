def get_params():
    params = []  # table that will contain the parameters
    ignore_file = open('.ignore', 'r')

    for line in ignore_file.readlines():
        if line[0] == "#":
            pass
        else:
            params.append(line)

    ignore_file.close()

    return params

if __name__ == "__main__":
    print("Dogo Yeb")