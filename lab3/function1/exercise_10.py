def uniq_(numbers : list):
    unique_elements = []
    for x in numbers:
        if x not in unique_elements:
            unique_elements.append(x)
    
    return unique_elements

# print(uniq_([1, 3, 4, 1, 4, 2, 3, 4 ,5 ,6 ,2 ,3, 54, 6, 1, 3, 6]))
