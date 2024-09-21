import numpy as np
from operation_class import IntArray                        #operation_class.py

def productivity_of_company(order,data_frame):
    return np.sum(data_frame[order])

def max_productivity(data_frame):
    i = 0
    best_company = i+1
    num_of_products = 0
    
    for i in range(len(data_frame)):
        result  = productivity_of_company(i,data_frame)
        if result > num_of_products:
            num_of_products = result
            best_company = i+1
    print(f"The best company is  the {best_company}. company with {num_of_products}.")
    

def min_productivity(data_frame):
    i = 0
    worst_company = i+1
    num_of_products = productivity_of_company(0,data_frame)
    
    for i in range(len(data_frame)):
        result  = productivity_of_company(i,data_frame)
        if result < num_of_products:
            num_of_products = result
            worst_company = i+1
    print(f"The worst company is  the {worst_company}. company with {num_of_products}.")
        

def file_handling():
    lines = []
    with open("company.txt",'r') as file:
        for line in file:
            values = line.strip().split(',')
            int_values = [int(val) for val in values if val.strip()] 
            lines.append(int_values)
        data_frame = np.array([np.array(row) for row in lines],dtype='object')
        # for row in data_frame:
        #     for i in row:
        #         print(type(i))
                
        return data_frame
    
def mean_products(data_frame):
    for i in range(len(data_frame)):
        average = np.mean(data_frame[i])
        print(f"On Average, one employee from {i+1}. company produced {average} products ")
    
    sum_products = 0
    num_employee = 0
   
    for row in data_frame:
        for elements in row:
            num_employee += 1
    
    for row in range(len(data_frame)):
        row_sum = np.sum(data_frame[row])
        sum_products += row_sum
    
    total_mean = sum_products/num_employee
    
    print(f"Total Mean is {total_mean} per employee")
    
    
            
            
        
        

def main():
    data_frame = file_handling()
    print(data_frame)
    
    first_branch = IntArray(data_frame[0])
    first_branch.display()
    first_branch.salary()
    first_branch.show_data()
    max_productivity(data_frame)
    min_productivity(data_frame)
    mean_products(data_frame)
    
    
    
main() 