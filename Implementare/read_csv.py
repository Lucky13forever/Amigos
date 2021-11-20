with open(r'Baze_de_Date\primul.csv', 'r') as file:
    head = file.readline()
    for col in head.split(';'):
        print(col, end=' ')
    
    print()


    for row in file:
        for col in row.split(';'):
            print(col, end = ' ')
        print()
        
        
        