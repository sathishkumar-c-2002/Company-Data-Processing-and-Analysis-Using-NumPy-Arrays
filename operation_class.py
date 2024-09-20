import numpy as np
import matplotlib.pyplot as plt


class IntArray:
    def __init__(self, int_array):
        if not isinstance (int_array,np.ndarray) or int_array.dtype != int:
            #Raise = Raising my own exception message 
            raise ValueError ("Input must be a NUMPY Array of Integers")             
        
        self.int_array = int_array
        
    def display(self):
        print(self.int_array)
    
    def salary(self):
        array_shape = self.int_array.shape
        #Creating the new array with FUll with shape and 7= value
        money_for_product = np.full(array_shape,7)              
        salaries = self.int_array * money_for_product
        
        print(f"People made {self.int_array} products and their salary is  ${salaries}.")
        
    def show_data(self):
        # np.arange is a sorting of the elements in the array
        x = np.arange(len(self.int_array))
        #marker is a way to plot the graph in visualization
        plt.plot(x,self.int_array,marker='o')   
        # grid is a way to create the graph line bg 
        plt.title("Productivity of Employees")
        plt.xlabel("Rank of Employee")
        plt.ylabel("Products/month")
        plt.xticks(x)
        
        plt.grid()
        plt.show()
        