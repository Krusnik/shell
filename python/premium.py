#!/usr/bin/python3.5

import sys

def unpack_line(line):
    list = line.split("|")
    if len(list) == 7:
        ackat = list[4]
        host = list[1].split("\"")[1]
        user = list[2].split("\"")[1]
        acktext = list[3][list[3].find("\"")+1: list[3].rfind("\"")]
        reacttime = list[6].split("\"")[1]
    elif  len(list) == 8:
        ackat = list[5]
        host = list[1].split("\"")[1]
        user = list[3].split("\"")[1]
        acktext = list[4][list[4].find("\"")+1: list[4].rfind("\"")]
        reacttime = list[6].split("\"")[1]
    else:
        print ("error in parse string: \n", line)
        return 0;
    return ackat, host, user, acktext, reacttime

dict = {}

for filename in sys.argv[1:]:
    file = open(filename, 'r')
    for line in file:
        unpack = unpack_line(line)
        key = unpack[0]+"|"+unpack[2]+"|"+unpack[3]
        if key in dict.keys():
            if dict[key] < int(unpack[4]):
                dict[key] = int(unpack[4])
        else:
            dict[key] = int(unpack[4])
    file.close()

dict2 = {}

for key,time in dict.items():
    user = key.split("|")[1]
    if user in dict2.keys():
        dict2[user].append(int(time))
    else:
        dict2[user] = [int(time)]


for keys in dict2.keys():
    print (keys + " " + str(round(sum(dict2[keys])/len(dict2[keys])/60,2)))
