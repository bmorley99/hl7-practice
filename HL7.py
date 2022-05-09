

#comments

from hl7_parser import *
import os
import pandas as pd
import hl7

current_directory = os.getcwd()
print(current_directory)
os.chdir("/Users/bmorley/Documents")
documents = "C:\\users\\bmorley\\documents\\"

test_hl7_file = documents + 'file.oru'

pid_segement_name = in1_segement_parse(test_hl7_file).in1_segement_parse(0)


print(pid_segement_name)

'''
file = open('file.oru', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

for line in lines:
    print(line)

lst1 = [str.split(line) for line in lines for newline in line]
print(lst1)

lst = []
for line in lines:
    for x in line:
        str.split(x)
        if x == "|":
            lst.append(x)


file = open('file.oru','r')
data = file.readlines()
file.close()

line_one = data[0]
line_two = data[1]
line_three = data[2]
line_four = data[3]
new_data_line1 = ""
new_data_line2 = ""
new_data_line3 = ""
new_data_line4 = ""
line1 = new_data_line1.join(line_one)
line2 = new_data_line2.join(line_two)
line3 = new_data_line3.join(line_three)
line4 = new_data_line4.join(line_four)

message = str(line1 + "\r")
message += str(line2 + "\r")
message += str(line3 + "\r")
message += str(line4 + "\r")
print(message)
#HL7data = hl7.parse(message)
#print(HL7data)
#print(HL7data.segment('PID')[0])

#print(type(HL7data))
#MSH = (HL7data.segment('MSH')[0:13])
#PID = (HL7data.segment('MSH')[13:32])
#PV1 = (HL7data.segment('MSH')[32:84])
#IN1 = (HL7data.segment('MSH')[84:129])
#print(MSH)


message = 'MSH|^~\&|GHH LAB|ELAB-3|GHH OE|BLDG4|200202150930||ORU^R01|CNTRL-3456|P|2.4\r'
message += 'PID|||555-44-4444||EVERYWOMAN^EVE^E^^^^L|JONES|196203520|F|||153 FERNWOOD DR.^^STATESVILLE^OH^35292||(206)3345232|(206)752-121||||AC555444444||67-A4335^OH^20030520\r'
message += 'OBR|1|845439^GHH OE|1045813^GHH LAB|1554-5^GLUCOSE|||200202150730||||||||555-55-5555^PRIMARY^PATRICIA P^^^^MD^^LEVEL SEVEN HEALTHCARE, INC.|||||||||F||||||444-44-4444^HIPPOCRATES^HOWARD H^^^^MD\r'
message += 'OBX|1|SN|1554-5^GLUCOSE^POST 12H CFST:MCNC:PT:SER/PLAS:QN||^182|mg/dl|70_105|H|||F\r'
h = hl7.parse(message)
h.segment(('PID')[5])
'''

