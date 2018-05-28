import os
import urllib.parse
lines = []
with open("./header.txt", 'r') as file:
    for i in file.readlines():
        line = i.strip()
        line = line.split(": ")
        lines.append(line)

obj = {}
for i in lines:
    obj[i[0]] = i[1]

print(obj)


# city_cn = "北京"
# city_encode = urllib.parse.quote(urllib.parse.quote(city_cn))
# print(city_encode)

ss = {'p': 'testSites',
      'm': 'ajax',
      'ym': '2018-05',
      'neeaID': '00000000',
      'cities': 'BEIJING_BEIJING;',
      'citiesNames': '%E5%8C%97%E4%BA%AC;',
      'whichFirst': 'AS',
      'isFilter': '0',
      'isSearch': '1'}
