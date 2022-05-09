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

class pid_segement_parse(hl7_parse):
    '''
    def parse_aws_data(self):
        patient_id = str()
        patient_name = str()
        date_birth = str()
        sex = str()
        patient_address = str()
        patient_number = str()
        patient_social = str()
        hl7_data = hl7_parse(self.filename)
        segement_data = hl7_data.parse_segement("PID")
        print(segement_data)
        for element in segement_data:
            patient_id = str(element[3])
            patient_name = str(element[5])
            date_birth = str(element[7])
            sex = str(element[8])
            patient_address = str(element[11])
            patient_number = str(element[13])
            patient_social = str(element[19])
        return patient_id, patient_name, date_birth, sex, patient_address, patient_number, patient_social
'''
    def pid_segement_parse(self, input):
        user_input = str()
        hl7_data = hl7_parse(self.filename)
        segement_data = hl7_data.parse_segement("PID")
        for element in segement_data:
            user_input = str(element[int(input)])
        return user_input