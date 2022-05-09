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
class in1_segement_parse(hl7_parse):

    def parse_aws_data(self):
        insurance_short_name = str()
        insurance_company_code = str()
        insurance_company_name = str()
        insurance_company_address = str()
        insurance_company_phone_number = str()
        group_number = str()
        name_of_insured = str()
        patient_relationship = str()
        insured_date_birth = str()
        insured_address = str()
        policy_number = str()
        hl7_data = hl7_parse(self.filename)
        segement_data = hl7_data.parse_segement("IN1")
        for element in segement_data:
            insurance_short_name = str(element[2])
            insurance_company_code = str(element[3])
            insurance_company_name = str(element[4])
            insurance_company_address = str(element[5])
            insurance_company_phone_number = str(element[7])
            group_number = str(element[8])
            name_of_insured = str(element[16])
            patient_relationship = str(element[17])
            insured_date_birth = str(element[18])
            insured_address = str(element[19])
            policy_number = str(element[36])
        return insurance_short_name, insurance_company_code, insurance_company_name, insurance_company_address, insurance_company_phone_number, group_number, name_of_insured, patient_relationship, insured_date_birth, insured_address, policy_number

    def in1_segement_parse(self, input):
        user_input = str()
        hl7_data = hl7_parse(self.filename)
        segement_data = hl7_data.parse_segement("IN1")
        for element in segement_data:
            user_input = str(element[int(input)])
        return user_input