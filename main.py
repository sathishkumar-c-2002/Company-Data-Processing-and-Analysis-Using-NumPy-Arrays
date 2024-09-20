import numpy as np
from operation_class import IntArray                        #operation_class.py



def file_handling():
    lines = []
    with open("company.txt",'r') as file:
        for line in file:
            values = line.strip().split(',')
            int_values = [int(val) for val in values if val.strip()] 
            lines.append(int_values)
        data_frame = np.array([np.array(row) for row in lines],dtype='object')
        for row in data_frame:
            for i in row:
                print(type(i))
                
        return data_frame
    

def main():
    data_frame = file_handling()
    print(data_frame)
    
    first_branch = IntArray(data_frame[0])
    first_branch.display()
    first_branch.salary()
    first_branch.show_data()
    
    
main() 