import csv 

def parse_instance(file_name): 
    set_members = dict() 
    with open("instance01.txt") as csvfile: 
        contents =csvfile.read()
        print(contents)
        reader = csv.reader(csvfile, delimeter = " ")
        for row in reader:
            print(', '.join(row))

parse_instance("instance01.txt")
