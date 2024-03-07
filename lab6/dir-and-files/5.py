def write_list_to_file(file, list):
    with open(file, 'w') as file:
        for pl in list:
            file.write(pl)

file = 'product_list.txt'

list = ["bread, milk, towels, eggs"]

write_list_to_file(file, list)