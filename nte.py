import os

cd = os.getcwd()


class hl7_parse():

    def __init__(self, filename):
        self.filename = filename

    def parse_segement(self, input):
        with open(self.filename, 'rt') as file:
            lines = file.readlines()
            segement_line_list = [seg for seg in lines if str(input) in seg[0:3]]
            segement_list = [segement.split('|') for segement in segement_line_list]

            """
            Parse HL7 file by given segement. 

            :arguement input: The users segement, PID for example
            :type input: str

            """
            return segement_list
class nte_segement_parse(hl7_parse):

    def parse_aws_data(self):
        nte_list = []
        hl7_data = hl7_parse(self.filename)
        segement_data = hl7_data.parse_segement("NTE")
        for element in segement_data:
            comment_message = [element[3]]
            nte_list.append(tuple(comment_message))
        return nte_list

    def nte_segement_parse(self, input):
        user_input = str()
        hl7_data = hl7_parse(self.filename)
        segement_data = hl7_data.parse_segement("NTE")
        for element in segement_data:
            user_input = str(element[int(input)])
        return user_input