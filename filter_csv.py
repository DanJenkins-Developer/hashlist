import csv 

file_name = str(input("Enter file name :: "))

with open(file_name, mode='r') as file:

    csv_reader = csv.DictReader(file)

    data_list = []

    for row in csv_reader:
        data_list.append(row)


column = str(input("Enter column name :: "))


# print(data_list[1]["Target.process.name"])

target_process_list = []

for data in data_list:
    #print(data["Target.process.name"])
    target_process_list.append(data[column])

#print(target_process_list)

unique_target_process_list = list(set(target_process_list))

#print(unique_target_process_list)

process_count = 0
for process in unique_target_process_list:
    process_count += 1
    print(process + "\n")

print("Number of unique items :: " + str(process_count))