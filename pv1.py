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
class pv1_segement_parse(hl7_parse):
    #
    # def __init__(self, filename):
    #     self.filename = filename

    def parse_aws_data(self):
        set_id = str()
        patient_location = str()
        attending_doctor = str()
        visit_number = str()
        hl7_data = hl7_parse(self.filename)
        segement_data = hl7_data.parse_segement("PV1")
        for element in segement_data:
            set_id = str(element[1])
            patient_location = str(element[3])
            attending_doctor = str(element[7])
            visit_number = str(element[8])
        return set_id, patient_location, attending_doctor, visit_number

    def pv1_segement_parse(self, input):
        user_input = str()
        hl7_data = hl7_parse(self.filename)
        segement_data = hl7_data.parse_segement("PV1")
        for element in segement_data:
            user_input = str(element[int(input)])
        return user_input
