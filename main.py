import os

def sort_file_list(files_dir_name):
    file_list = []

    file_names = os.listdir(files_dir_name)
    for file_name in file_names:
        with open(os.path.join(files_dir_name, file_name), "r", encoding="utf-8") as file:
            file_list.append({"path": os.path.join(files_dir_name, file_name),
                              "len": sum(1 for string in file)})
    file_list = sorted(file_list, key=lambda x: x['len'])
    return file_list


def merge_files(file_list, result_file_name, files_dir_name):
    file_result = open(os.path.join(files_dir_name, result_file_name), "w", encoding="utf-8")

    for file_item in file_list:
        if os.path.basename(file_item["path"]) != result_file_name:
            with open(file_item["path"], "r", encoding="utf-8") as file:
                file_result.write(os.path.basename(file_item["path"])+"\n")
                file_result.write(str(file_item["len"])+"\n")
                for string in file:
                    file_result.write(string)
                file_result.write("\n")
    file_result.close()


merge_files(sort_file_list("files"), "result.txt", "files")

