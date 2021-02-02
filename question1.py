# Question 1
# Author: Catherine Muthoni

class Array:
    def __init__(self, size, values=None):  # creating the static array giving size and values(default value is None)
        self.size = size
        self.values = values

        if self.values == None:  # setting the values of the array to none and appending them if there are no values
            self.elements = list()
            try:  # ensuring that the values given are integers only
                self.elements = int
            except TypeError:
                print("Values should be integers")

            for i in range(size):
                self.elements.append(self.values)

        else:
            self.elements = list()  # appending the given values to the list
            if len(self.values) == size or len(self.values) < size:
                for j in range(len(self.values)):
                    if self.values[j]:
                        self.elements.append(self.values[j])
                for i in range(len(self.values), size):
                    self.elements.append(None)
            else:
                print('Elements are more than the size specified')

    def length(self):  # determining the length of the array
        length = 0
        for i in self.elements:
            if i == None:
                continue
            else:
                length += 1
        return length

    def get(self, i):  # determining the value at a given index
        for index in range(len(self.elements)):
            if index == i:
                return self.elements[index]

    def set(self, val, i):  # replacing the value at the given index with a the given value
        for index in range(len(self.elements)):
            if index == i:
                self.elements[index] = val




if __name__ == '__main__':  # calling all the methods of the class
    Array1 = Array(8, [1,2,3,4,5])
    print("1. My array: " + str(Array1.elements))
    length_array = Array1.len()
    print("2. The length of my array is " + str(length_array))
    element = Array1.get(3)
    print("3. The element at index 3 is " + str(element))
    new_element = Array1.set(6,3)
    print("4. The new element at index 3 is " + str(Array1.get(3)))










