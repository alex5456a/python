def remove_duplicates(numbers):
    new_list = []
    for number in numbers:
        if number not in new_list:
            new_list.append(number)
    return new_list

ids = [1, 2 , 2, 1, 3, 4, 5]
print(remove_duplicates(ids))