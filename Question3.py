
from Akatsuki_array import Array
from Question2 import DyArray

class Third(DyArray, Array):

    def __init__(self, array):
        DyArray.__init__(self, array)    
        Array.__init__(self, array)
        self.array = array

    def contains(self, val):
        exist = val in self.array
        return exist
        

    def reverse(self):
        rev_arr = self.array[::-1]
        return rev_arr

    def insert(self, val, i):
       return self.array[:i] + [val] + self.array[i:]


if __name__ == '__main__':
    arr = Third([1,2,3,4,5,6])
    print("The initial Array:")
    print(arr.array)
    contain = arr.contains(3)
    print("\n1. Let's see if 3 is in: ")
    print(contain)
    rversed_arr = arr.reverse()
    print("\n2. The reversed array is: ")
    print(rversed_arr)
    inserted_arr = arr.insert(7,0)
    print("\n3. The new array with inserted value:")
    print(inserted_arr)
        

"""
    Time Complexity: O(1)
    Space Complexity: O(1)
"""