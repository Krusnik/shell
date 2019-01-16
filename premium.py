#!/usr/bin/python3.5

import sys

def unpack_line(line):
    list = line.split("|")
    if len(list) == 7:
        date = list[0]
        host = list[1].split("\"")[1]
        user = list[2].split("\"")[1]
        acktext = list[3][list[3].find("\"")+1: list[3].rfind("\"")]
        reacttime = list[6].split("\"")[1]
    elif  len(list) == 8:
        date = list[0]
        host = list[1].split("\"")[1]
        user = list[3].split("\"")[1]
        acktext = list[4][list[4].find("\"")+1: list[4].rfind("\"")]
        reacttime = list[6].split("\"")[1]
    else:
        print ("error in parse string: \n", line)
        return 0;
    return date, host, user, acktext, reacttime

dict = {}

for filename in sys.argv[1:]:
    file = open(filename, 'r')
    for line in file:
        key = unpack_line(line)[0]+"|"+unpack_line(line)[2]+"|"+unpack_line(line)[3]
        if key in dict:
            if int(dict[key]) < int(unpack_line(line)[4]):
                dict[key] = unpack_line(line)[4]
        else:
            dict[key] = unpack_line(line)[4]
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
