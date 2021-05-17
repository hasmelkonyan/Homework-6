# noinspection PyGlobalUndefined
def file_work(file):
    global my_file
    try:
        my_file = open(file, encoding='utf-8')
    except IOError:
        print ('File not found or path is incorrect')

    num_of_the = 0
    num_of_if = 0
    num_of_e = 0
    data = my_file.read()
    words = data.split()

    for each in words:
        each = each.lower()
        if each == 'the':
            num_of_the += 1
        elif each == 'if':
            num_of_if += 1
    for each in words:
        for letter in each:
            if letter == 'e':
                num_of_e += 1
    print('num_of_the = ', num_of_the, '\nnum_of_if = ', num_of_if, '\nnum_of_e = ', num_of_e)
    my_file.close()

    try:
        my_file.read()
    except ValueError:
        print('File is closed')


file_work(r"C:\Users\hayk\Desktop\How_to_turn_dirt_into_gold.txt")
