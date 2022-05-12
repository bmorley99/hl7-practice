from HL7Ben import *
import os

current_directory = os.getcwd()
os.chdir("/Users/bmorley/Documents")
path = "C:\\users\\bmorley\\documents\\"

hl7_file = path + 'file.oru'

newfile = parse_segement(hl7_file)
test = choose_the_data(newfile,3)

print(test)
