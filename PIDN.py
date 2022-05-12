
class hl7_parse():

    def __init__(self, filename):
        self.filename = filename

    def parse_segement(self, input):
        with open(self.filename, 'rt') as file:

            lines = file.readlines()
            print(lines)

            segement_line_list = []
            for seg in lines:                   #loops through the file
                if "PID" in seg[0:3]:
                    print(seg)
                    print( segement_line_list)#Checks to make sure the file has a title indicator in this case PID
                    segement_line_list.append(seg) #if it has the indicator it adds that to the list segement_line_list
                    #output ['PID|1||Toka^Scott||19790301|M|||1170 S State St^^EPHRATA^PA^17522||\n']

            segement_list = []
            for segement in segement_line_list:
                segement_list.append(segement.split('|')) #turns the string into a list and divides each element by |
#output [['PID', '1', '', 'Toka^Scott', '', '19790301', 'M', '', '', '1170 S State St^^EPHRATA^PA^17522', '', '\n']]
            return segement_list

class Pid_segement_parse(hl7_parse): #Allows for the first class to be used in this class
#also uses the inputed file in a positioal sence to convert it to an object
    def pid_segement_parse(self, input):
        user_input = str()

        hl7_data = hl7_parse(self.filename) #the file has been turned into an object and is now being renamed

        segement_data = hl7_data.parse_segement("PID") #PID is used to select the line in the file
#segment_data = segement_list is what is actually happening
        for element in segement_data:
            user_input = str(element[int(input)]) #indexes the number you entered through the list of elements
#pid_segement_parse(0) would be the first value of the list becuase the 0 enter is the inputed value for input
        return user_input