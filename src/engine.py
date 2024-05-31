from hashlib import md5
from operator import le
import time
import os
import hashlib
import requests
import json

# start = time.time()


class Engine:

    def __init__(self, hashList):
            self.hashList = hashList
            self.ioList = []
            for i in self.hashList:
                self.ioList.append(self.hashToFullNum(i))

            self.ioList.sort()
            print(ioList)
            self.startTime = time.time()
            self.endTime = 0

    def hashToFullNum(self, hash):

        alpha = 'abcdefghijklmnopqrstuvwxyz'
        alphaNum = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
                    'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
                    'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

        j = ''

        sampleHash = hash.lower()

        for i in sampleHash:
            if i in alpha:
                i = alphaNum[i]

            j = j + str(i)

        return int(j)

    def binaryTreeSearch(self, hList, valueToFind):
        initialValue = 0
        lenghtOfList = len(hList) - 1
        pointFound = 0

        while (initialValue < lenghtOfList and pointFound == 0):
            middle = (initialValue + lenghtOfList) // 2

            if hList[middle] == valueToFind:
                pointFound = 1
                positionOfPoint = middle

            if hList[middle] > valueToFind:
                lenghtOfList = middle

            if hList[middle] < valueToFind:
                initialValue = middle + 1

        if pointFound == 1:
            return positionOfPoint

        else:
            return None

    def Md5_hash(self, filename):
        try:
            with open(filename, "rb") as f:
                bytes = f.read()
                md5Hash = hashlib.md5(bytes).hexdigest()

                f.close()
            return md5Hash
        except:
            return 0

    def virusScannerMd5(self, path):
        print("VirusScannerMd5")
        self.virusPath = []
        self.virusHashCyPy = []

        # Get the list of all files in directory tree at given path
        dir_list = list()
        for (dirpath, dirnames, filenames) in os.walk(path):
            dir_list += [os.path.join(dirpath, file) for file in filenames]

        for i in dir_list:
            try:
                a = self.Md5_hash(i)
                print(a)

                vIHash = self.binaryTreeSearch(
                    self.ioList, self.hashToFullNum(a))
                if vIHash:
                    self.virusHashCyPy.append(vIHash)
                    self.virusPath.append(i)

            except:
                pass

        self.endTime = time.time()

        return self.virusHashCyPy, self.virusPath, self.endTime - self.startTime

    # def CacheFileRemover(self):
    #
    #     # Temp Files Remover
    #
    #     temp_list = list()
    #
    #     # Windows username
    #
    #     username = os.environ.get('USERNAME').upper().split(" ")
    #
    #     for (dirpath, dirnames, filenames) in os.walk("C:\\Windows\\Temp"):
    #         temp_list += [os.path.join(dirpath, file) for file in filenames]
    #         temp_list += [os.path.join(dirpath, file) for file in dirnames]
    #
    #     for (dirpath, dirnames, filenames) in os.walk("C:\\Users\\{}~1\\AppData\\Local\\Temp".format(username[0])):
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

    def FlowDetectorIo(self, path, bit_size):

        with open("DataBase\\Flow Detection\\flow_exe.unibit", "r") as rFile:
            io = rFile.readlines()
            rFile.close()

        with open(path, "rb") as rFile:
            nj = list(rFile.read())
            rFile.close()

        njStr = ''

        for i in nj:
            njStr += str(i)

        bX = 0

        for f in io:
            for i in range(0, len(f), bit_size):
                if njStr.find(f[i:i + bit_size]) != -1:
                    bX += 1

            if flen := len(f) / bit_size:
                prLen = (bX / flen) * 100

        return prLen

    def malware_checker(self, path):
        print(path)
        print("checking")
        valueToFind = self.hashToFullNum(self.Md5_hash(path))
        initialValue = 0
        lenghtOfList = len(self.ioList) - 1
        pointFound = 0

        while (initialValue < lenghtOfList and pointFound == 0):
            middle = (initialValue + lenghtOfList) // 2

            if self.ioList[middle] == valueToFind:
                pointFound = 1
                positionOfPoint = middle

            if self.ioList[middle] > valueToFind:
                lenghtOfList = middle

            if self.ioList[middle] < valueToFind:
                initialValue = middle + 1

        if pointFound == 1:
            return [positionOfPoint, path]
        else:
            return None


def virusScannerAPI(path):
    print("ready")
    md5String = Md5_hash(path)
    url = f"https://www.virustotal.com/api/v3/files/{md5String}"
    headers = {
        "accept": "application/json",
        "x-apikey": "d67cfb9370d3b15a97f8b82ddd63d7c7989f504b4af90037265d6a822021eb53"
    }

    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    if 'data' not in data:
        return 0

    else:
        if ("type_tag" or "md5" or "last_analysis_stats" or "name") and 'popular_threat_classification' in data['data'][
            'attributes']:
            popular_threat_category = data['data']['attributes']['popular_threat_classification'][
                'popular_threat_category']
            type_tag = data['data']['attributes']['type_tag']
            md5 = data['data']['attributes']['md5']
            malicious = data['data']['attributes']['last_analysis_stats']['malicious']
            nameFile = data['data']['attributes']['names'][0]

            return {
                "popular_threat_category": popular_threat_category,
                "type_tag": type_tag,
                "md5": md5,
                "malicious": malicious,
                "nameFile": nameFile,
            }
        else:
            return 0





def Md5_hash(filename):
    try:
        with open(filename, "rb") as f:
            bytes = f.read()
            md5Hash = hashlib.md5(bytes).hexdigest()

            f.close()
        return md5Hash
    except:
        return 0


# io = Engine("md5")
# print(io.virusScannerMd5("C:\\Users\\trinhhuynh\\Desktop"))

# end = time.time()
# print(end - start)
