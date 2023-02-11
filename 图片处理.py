import os
import hashlib
import shutil

if __name__ == '__main__':
    # 存放文件的目录地址，不要遗落最后的\\， Linux or Mac需要换分隔符
    source_path = "E:/待处理/"
    # 设置重复文件存放的目录
    repeat_file_path = "E:/重复文件/"
    file_list = os.listdir(source_path)

    files_map = {}
    index = 1
    repeat_num = 0

    for file in file_list:
        print("第【" + str(index) + "】个开始处理 --> " + file)
        index += 1

        with open(source_path + file, 'rb') as file_pointer:
            data = file_pointer.read()
        file_md5 = hashlib.md5(data).hexdigest()
        file_pointer.close()

        if files_map.get(file_md5) is None:
            files_map[file_md5] = file
        else:
            print("发现重复文件: " + file + "  -->  " + files_map[file_md5])
            if len(files_map[file_md5]) < len(file):
                shutil.move(source_path + file, repeat_file_path + file)

            else:
                temp_file = files_map[file_md5]
                files_map[file_md5] = file
                shutil.move(source_path + temp_file, repeat_file_path + temp_file)
            repeat_num += 1

    print("********处理完成********")
    print("重复数量 --> " + str(repeat_num))