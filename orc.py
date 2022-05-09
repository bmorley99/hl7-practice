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
class orc_segement_parse(hl7_parse):

    def parse_aws_data(self):
        order_control = str()
        order_num = str()
        filler_order_num = str()
        order_status = str()
        date_time_transaction = str()
        entered_by = str()
        ordering_provider = str()
        enterers_location = str()
        hl7_data = hl7_parse(self.filename)
        segement_data = hl7_data.parse_segement("ORC")
        for element in segement_data:
            order_control = str(element[1])
            order_num = str(element[2])
            filler_order_num = str(element[3])
            order_status = str(element[5])
            date_time_transaction = str(element[9])
            entered_by = str(element[10])
            ordering_provider = str(element[12])
            enterers_location = str(element[13])
        return order_num, order_control, order_num, filler_order_num, order_num, order_status, date_time_transaction, entered_by, ordering_provider, enterers_location

    def orc_segement_parse(self, input):
        user_input = str()
        hl7_data = hl7_parse(self.filename)
        segement_data = hl7_data.parse_segement("ORC")
        for element in segement_data:
            user_input = str(element[int(input)])
        return user_input
