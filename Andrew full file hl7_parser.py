import os

cd = os.getcwd()

"""
Each class contains the corresponding segement parser. 
Input on these functions is the segement position to return a str of the value 

:arguement input: The user inputs segement position 
:type input: str or int
"""

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
        for element in segement_data:
            patient_id = str(element[3])
            patient_name = str(element[5])
            date_birth = str(element[7])
            sex = str(element[8])
            patient_address = str(element[11])
            patient_number = str(element[13])
            patient_social = str(element[19])
        return patient_id, patient_name, date_birth, sex, patient_address, patient_number, patient_social

    def pid_segement_parse(self, input):
        user_input = str()
        hl7_data = hl7_parse(self.filename)
        segement_data = hl7_data.parse_segement("PID")
        for element in segement_data:
            user_input = str(element[int(input)])
        return user_input

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


class obr_segement_parse(hl7_parse):

    def parse_aws_data(self):
        obr_list = []
        final_obr_list = []
        index_list = [2, 4, 7, 9, 10, 14, 15, 16, 25, 27]
        hl7_data = hl7_parse(self.filename)
        segement_data = hl7_data.parse_segement("OBR")
        for segements in segement_data:
            special_split = 'split@'
            #comp_list = [segements[index_pos] for index_pos in index_list]
            obr_list.append(str(segements)+special_split)
            final_obr_list = "".join(obr_list)
        return final_obr_list

    def obr_segement_parse(self, input):
        user_input = str()
        hl7_data = hl7_parse(self.filename)
        segement_data = hl7_data.parse_segement("OBR")
        for element in segement_data:
            user_input = str(element[int(input)])
        return user_input

class obx_segement_parse(hl7_parse):

    def parse_aws_data(self):
        obx_list = []
        index_list = [3, 5, 6, 7, 8, 11, 14, 15, 16]
        hl7_data = hl7_parse(self.filename)
        segement_data = hl7_data.parse_segement("OBX")
        for e in segement_data:
            if "PDF" in e[3]:
                segement_data.pop()
        for segements in segement_data:
            comp_list = [segements[index_pos] for index_pos in index_list]
            obx_list.append(tuple(comp_list))
        return obx_list

    def obx_segement_parse(self, input):
        user_input = str()
        hl7_data = hl7_parse(self.filename)
        segement_data = hl7_data.parse_segement("OBX")
        for e in segement_data:
            if "PDF" in e[3]:
                segement_data.pop()
        for element in segement_data:
            user_input = str(element[int(input)])
        return user_input

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
