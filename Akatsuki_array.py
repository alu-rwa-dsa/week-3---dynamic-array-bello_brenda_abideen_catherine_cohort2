
class Array:
    #Defining the objects in the class
    def __init__(self, array):
        self.array = array
        # self.size = 7

    #Defining the function to get length
    def length(self):
        return len(self.array)

    #Defining the function to get items
    def get(self, index):
        return self.array[index]

    #Defining the function to set a value to an index
    def set(self, value, index):
        self.array[index] = value
        return self.array


if __name__ == '__main__':
    Initial_Arr = Array([2,3,4,1,6,8,7])
    print("\nThe initial Array is: ")
    print(Initial_Arr.array)
    length_array = Initial_Arr.length()
    print("\n1. The length is: " + str(length_array))
    element = Initial_Arr.get(2)
    print("\n2. The 3rd element of the array is: " + str(element))
    new_array = Initial_Arr.set(9,3)
    print("\nThe new Array is: ")
    print(new_array)
    print("\n3. The element replaced at index 3 is: " + str(Initial_Arr.get(3)))
