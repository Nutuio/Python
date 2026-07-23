States = {'Delhi' : 'DL', 'Haryana' : 'HR', 'Maharashtra' : 'MH', 'Rajasthan' : 'RJ'}
States['Tamil Nadu'] = 'TN'
States.setdefault('Karnataka','Sorry, no idea')
print("Code for Rajasthan : ", States['Rajasthan'])
print("-" * 5,  "CODES", "-" * 5)
for i in States.items():
    print(i)
print("Code for Karnataka : ", States.get('Karnataka'))