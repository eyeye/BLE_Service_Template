'''
Created on 2013-4-28

@author: YangZhiyong
'''


import json
from jinja2 import Template
#import pprint

json_file = open("BLE_Service.json", 'r')
json_data = json.load(json_file)

ctemp_file = open("BLE_Nordic.ctemplate", 'r')
ctemplate = Template(ctemp_file.read())

htemp_file = open("BLE_Nordic.htemplate", 'r')
htemplate = Template(htemp_file.read())

#c_file = open("BLE_Service.json", 'r')
#h_file = open("BLE_Service.json", 'r')

for service in json_data['Services']:
    print '//////////////////////////////'
    fileName = 'BLE_' + service['name'] + '.c'
    fileData = ctemplate.render(service=service)
    print fileName
    print fileData
    print '//////////////////////////////'
    fileName = 'BLE_' + service['name']+'.h'
    fileData = htemplate.render(service=service)
    print fileName
    print fileData


json_file.close()
ctemp_file.close()
htemp_file.close()





