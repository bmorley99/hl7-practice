from PIDN import *
import os
import hl7

current_directory = os.getcwd()
os.chdir("/Users/bmorley/Documents")
documents = "C:\\users\\bmorley\\documents\\"

test_hl7_file = documents + 'file.oru'

pid_segement_name = Pid_segement_parse(test_hl7_file).pid_segement_parse(3)


print(pid_segement_name)
