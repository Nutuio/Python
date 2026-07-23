Dict = {'Roll_No' : '16/001', 'Name' : 'Saptarshi', 'Course' : 'Btech'}
inverted = {}
for key, val in Dict.items():
    inverted[val] = key
print("Dict : ", Dict)
print("Inverted Dict : ", inverted)