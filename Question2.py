#Abideen Hamisu

#importing the parent file
# 
from Akatsuki_array import Array

# Importing unit test to help with the testing
# import unittest

#Creating my dyanamic array class
class DyArray(Array):
    #Defining the functions in the class
    def __init__(self, li):
        Array.__init__(self, li)
        
        self.li = li


    def add(self, value):
        self.li.append(value)
        return self.li

    # Space Complexity - O(1) It is constant because the algorithm will take the same amount of memory space everytime and it uses a return statement which means
    # Is recycling memory space
    #Time Complexity - O(1) Because no matter the size of the stuff you want to append it will always append in the same amount of time


    def delete(self):
        index = -1
        del self.li[index]
        return self.li

        

if __name__ == '__main__':
    array = DyArray([1,2,3,4,5,6])
    print('The Initial Array: ')
    print(array.li)
    new_Array0 = array.add(7)
    print("\n1. Let's add 7: ")
    print(new_Array0)
    new_Array1 = array.delete()
    print("\n2. Let's remove the last element: ")
    print(new_Array1)

    
    