import json

print('Press 1 for creating student name and grade\n'
      'Press 2 for knowing the grade of a student\n'
      'Press 3 for editing the grade\n'
      'Press 4 for deleting a grade\n')

query = int(input('Enter the relevant number\n'))
file = open('grades.txt', 'r+')
data = json.load(file)

if query == 1:
    name = input('enter the name of student\n')
    grade = float(input('enter the grade\n'))
    data[name]=grade

elif query == 2:
    name = input('enter the name of student\n')
    print(data[name])

elif query == 3:
    name = input('enter the name of student\n')
    grade = float(input('enter the new grade\n'))
    data[name] = grade

elif query == 4:
    name = input('enter the name of student\n')
    del data[name]

else:
    print('enter a valid query')

file.seek(0)
file.truncate()
json.dump(data, file)
