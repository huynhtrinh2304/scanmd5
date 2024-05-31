import hashlib
import os
import time

# Global Variable
malware_hashes = list(open("src/DataBase/HashDataBase/Sha256/virusHash.unibit", "r").read().split('\n'))
virusInfo = list(open("src/DataBase/HashDataBase/Sha256/virusInfo.unibit", "r").read().split('\n'))


# Get Hash Of File
def sha256_hash(filename):
    with open(filename, "rb") as f:
        byte = f.read()
        sha256hash = hashlib.sha256(byte).hexdigest()
        f.close()
    # print(sha256hash)
    return sha256hash


def malware_checker(pathOffile):
    global malware_hashes
    global virusInfo
    hash_malware_check = sha256_hash(pathOffile)
    counter = 0
    for i in malware_hashes:
        if i == hash_malware_check:
            return virusInfo[counter]
        counter += 1
    return 0


virusName = []
virusPath = []
time_execute = 0


# def folderScanner1():
#     # Get the list of all files and directories
#     path = "C:\\Users\\trinhhuynh\\Desktop\\Labs\\Chapter_3L"
#     fill_files_only = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
#
#     fileN = ""
#     for i in fill_files_only:
#         fileN = path + "\\" + i
#         if malware_checker(fileN) != 0:
#             virusName.append("Threat categories: " + malware_checker(fileN) + " :: File name :: " + i)


def folderScanner(pathFolderScan):
    start = time.time()
    count = 1
    path = pathFolderScan
    for root, directories, files in os.walk(path):
        for file in files:
            index = str(count)
            fileN = root + "\\" + file
            if malware_checker(fileN) != 0:
                virusName.append(index + ":" + " Threat categories: " + malware_checker(
                    fileN) +"\n" + " :: File name :: " + file + "\n :: Location :: " + fileN)
                count += 1
                virusPath.append(fileN)

    end = time.time()
    elapsed_time = end - start
    elapsed_time_formatted = "{:.3f}".format(elapsed_time)
    time_execute = elapsed_time_formatted
    return elapsed_time_formatted

# print(virusName)


# def virusRemover(path):
#     folderScanner(path)
#     if virusPath:
#         for i in virusPath:
#             os.remove(i)
#     else:
#         return 0


# def juckFileRemover():
#     # Temp Files Remover
#     temp_list = list()
#     # Windows username
#     username = os.environ.get('USERNAME').upper().split(" ")
#
#     for (dirpath, dirnames, filenames) in os.walk("C:\\Windows\\Temp"):
#
#         temp_list += [os - path.join(dirpath, file) for file in filenames]
#         temp_list += [os - path.join(dirpath, file) for file in dirnames]


# for (dirpath, dirnames, filenames) in os.walk("C:\\Users\\{}~1\\AppData\\Local\\Temp".format(username[0])):
#         temp_list += [os.path.join(dirpath, file) for file in filenames]
#         temp_list += [os.path.join(dirpath, file) for file in dirnames]
#
#     for (dirpath, dirnames, filenames) in os.walk("C:\\Windows\\Prefetch"):
#         temp_list += [os.path.join(dirpath, file) for file in filenames]
#         temp_list += [os.path.join(dirpath, file) for file in dirnames]
#
#     if temp_list:
#
#         for i in temp_list:
#             print(i)
#
#             try:
#                 os.remove(i)
#
#             except:
#                 pass
#
#             try:
#                 os.rmdir(i)
#
#             except:
#                 pass
#
#     else:
#         return 0
