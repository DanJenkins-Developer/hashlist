import json 

f_name = 'T716D854_dirwalkResponse_2024-09-09T16_02_04Z_data.json'

hash_256 = "15bf0ce72326f19568df7f0a8d2eda71fd907c7d3d0b3bb79240830b08009b21"

found_file = "None"

def main():
    with open(f_name) as f:
        data = json.load(f)


    print(data["data"].keys())
    print(data["data"]["file_list"])
    print(type(data["data"]["file_list"]))

    files = data["data"]["file_list"]

    file_count = 0
    found_file = "None"

    for file in files:

        if (file["meta_data"]["file_size"] != 0 ):
            print(file["file_path"])
            print(file["meta_data"]["hashes"]["sha256"])
            print("\n")

            file_count += 1


            if (file["meta_data"]["hashes"]["sha256"] == hash_256):
                print("Found the file!")
                found_file = file["file_path"]
                break

    print("Total files: " + str(file_count))
    print ("Searching for hash: " + hash_256)
    print("Found file: " + found_file)




if __name__ == '__main__':
    main()