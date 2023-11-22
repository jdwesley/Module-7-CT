#create dict_1 for romm number
dict_1 = dict({'CSC101': '3004',
                'CSC102': '4501',
                  'CSC103': '6755',
                    'NET110': '1244',
                      'COM241': '1411'})
print(dict_1)
#create dictionary 2 for instructor name
dict_2 = dict({'CSC101': 'Haynes',
                'CSC102': 'Alvarado',
                  'CSC103': 'Rich',
                    'NET110': 'Burke',
                      'COM241': 'Lee'})
print(dict_2)
#create dictionary 3 for class time
dict_3 = dict({'CSC101': '8:00 a.m.',
                'CSC102': '9:00 a.m.',
                  'CSC103': '10:00 a.m.',
                    'NET110': '11:00 a.m.',
                      'COM241': '1:00 p.m.'})
print(dict_3)

#promt user to input a string defining course number x
x = input(str('What is your course number? '))
#if statement 
if dict_1.key(x):
        room_num = dict_1.get(x)
        intructor_name = dict_2.get(x)
        class_time = dict_3.get(x)

        print(f'{room_num}, {intructor_name}, {class_time}')
else:
    print("This class does not exist!")



