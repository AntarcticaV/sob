from datetime import datetime, timedelta
import json


if __name__ == "__main__":
    file_result = []
    names_dict = {}
    line = []
    with open("competitors2.json", "r") as file:
            names_dict = json.load(file)
    with open("results_RUN.txt", "r", encoding='utf-8-sig') as file:
        for i in file:
            line.append(i.split(' '))
    first_line = line[0]
    
    for i in line:
        if i[1] != "finish":
            first_line = i
        if i[0] == first_line[0] and i[1] == "finish" and i[1] != first_line[1]:
            date1 = datetime.strptime(i[2].replace('\n', ''), "%H:%M:%S,%f")
            date2 = datetime.strptime(first_line[2].replace('\n', ''), "%H:%M:%S,%f")
            fio = names_dict[i[0]]
            
            file_result.append([i[0], fio, date1 - date2])

    file_result.sort(key= lambda x: x[2])
    print("|{0:^15}|{1:^15}|{2:^15}|{3:^15}|{4:^15}|\n".format("Занятое место", "Нагрудный номер", "Имя", "Фамилия", "Результат"))
    numder:int = 1

    for i in file_result:
        
        time :timedelta = i[2]
        minetu = (f"0{time.seconds // 60}", f"{time.seconds // 60}")[time.seconds // 60 > 9]
        secons = (f"0{time.seconds % 60}", f"{time.seconds % 60}")[time.seconds % 60 > 9]
        time_str = f"{minetu}:{secons},{time.microseconds // 10000}"
        print("|{0:^15}|{1:^15}|{2:^15}|{3:^15}|{4:^15}|".format(numder, i[0], i[1]['Surname'], i[1]['Name'], time_str))
        numder += 1
