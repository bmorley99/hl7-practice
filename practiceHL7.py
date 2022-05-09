from PIDN import *
import os
import hl7

current_directory = os.getcwd()
os.chdir("/Users/bmorley/Documents")
documents = "C:\\users\\bmorley\\documents\\"

test_hl7_file = documents + 'file.oru'

pid_segement_name = pid_segement_parse(test_hl7_file).pid_segement_parse(5)

print(pid_segement_name)
print('smelly')