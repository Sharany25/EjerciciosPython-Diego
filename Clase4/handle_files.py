try:
    path = 'C:\\DataFiles\\archivo.txt'
    new_file = open(path, 'r')
    #data = new_file.readlines()
    #print(data)
    one_line = new_file.readline()
    print(one_line)

    #for line in new_file:
        #print(line)

    #new_file = open("C:\\DataFiles\\archivo.txt", "w")
    #new_file.write("Hello world\n")
    #new_file.write("Hola mundo\n")
    #new_file.write("Hola UTVT\n")
    #new_file.write("Hola Diego Osorio\n")
    #new_file.close()
except Exception as e:
    print(e)