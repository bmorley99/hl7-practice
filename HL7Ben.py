def parse_segement(filename):
    with open(filename, 'rt') as file:
        lines = file.readlines()

        PID_lst = [value for value in lines if "PID" in value[0:]]

        string_conversion = ""
        seperated_list = []
        for newval in PID_lst:
            string_conversion += newval
            string_values = string_conversion.split("|")
            seperated_list.append(string_values)
        return seperated_list

def choose_the_data(list,input):
    seperated_list = list
    for element in seperated_list:
        inputed = element[int(input)]
    return inputed







