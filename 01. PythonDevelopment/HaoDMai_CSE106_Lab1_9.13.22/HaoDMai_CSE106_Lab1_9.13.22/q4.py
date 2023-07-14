class Data:
    def print_info(self):
        file = open('classesInput.txt', 'r')
        data = []
        for l in file:
            data.append(l.strip())

        cnt = int(data[0])
        i=1
        for course_cnt in range(1, cnt+1):
            recieved_data = []
            for j in range(8):
                recieved_data.append(data[i])
                i+=1
            line1 = f'Course {course_cnt}: {recieved_data[0]}{recieved_data[1]}: {recieved_data[2]}'
            print(line1)
            line2 = f'Number of Credits: {recieved_data[3]}'
            print(line2)
            line3 = f'Days of Lectures: {recieved_data[4]}'
            print(line3)
            line4 = f'Lecture Time: {recieved_data[5]}-{recieved_data[6]}'
            print(line4)
            line5 = f'Stat: on average, students get {recieved_data[7]} in this course'
            print(line5)
            print()

d=Data()
d.print_info()
