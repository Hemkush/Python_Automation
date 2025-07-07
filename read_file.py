inputFile = open("inputFile.txt", "r")
for line in inputFile:
    split_line = line.split()
    if split_line[2] == "P":
        print(line)
inputFile.close()