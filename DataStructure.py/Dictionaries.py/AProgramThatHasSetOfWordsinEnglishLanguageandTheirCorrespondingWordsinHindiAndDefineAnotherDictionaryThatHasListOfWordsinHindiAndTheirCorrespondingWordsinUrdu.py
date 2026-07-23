E_H = {'Friend' : 'Mitr', 'Teacher' : 'Shikshak', 'Book' : 'Pustak', 'Queen' : 'Rani'}
H_U = {'Mitr' : 'Dost', 'Shikshak' : 'Adhyapak', 'Pustak' : 'Kitab', 'Rani' : 'Begum'}
for i in E_H:
    print(i, "in Hindi means", E_H[i], "and in Urdu means", H_U[E_H[i]])