import csv 

with open('test.csv', mode='r') as file:

    csv_reader = csv.DictReader(file)

    data_list = []

    for row in csv_reader:
        data_list.append(row)


# print(data_list[1]["Target.process.name"])

target_process_list = []

for data in data_list:
    #print(data["Target.process.name"])
    target_process_list.append(data["Target.process.name"])

#print(target_process_list)

unique_target_process_list = list(set(target_process_list))

#print(unique_target_process_list)

process_count = 0
for process in unique_target_process_list:
    process_count += 1
    print(process)

print("Number of unique processes :: " + str(process_count))