def del_phone_number(contact):
    f = open(r'telephon_book.txt', 'r')
    Line_new = f.readlines()
    f.close()
    f = open(r'telephon_book.txt', 'w')
    for line in Line_new: 
        if line.find(contact) == -1:
            f.write(line)
    f.close()