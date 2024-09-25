# YOUR CODE AND HEADING HERE
# Griffin King
# Unit 2 Lab 2
# Making a array class to follow some test code 
import ctypes
class DynamicArray:
  
  def __init__(self):
    self.__n = 0
    self.__capacity = 1
    self.__A = DynamicArray.__make_array(self,self.__capacity)
  
  def append(self, ele):
    # It will try to append to the array, it if can't because the capacity is too small then it will go to the except statement and work its way through that giving it more capacity and then adding the element to the array
    try:
      self.__A[self.__n] = ele
    
    
    except:
      DynamicArray.__resize(self)
      self.__A[self.__n] = ele
    self.__n += 1
  
  def __resize(self):
    #Expanding the capacity
    self.__capacity += self.__capacity
    #Make a new array that also has the new desired capacity
    Temp1 = DynamicArray.__make_array(self,self.__capacity)
    for a in range(self.__n):
      #This is giving the new array the elements from the original array and then making that temp array the main array
      Temp1[a] = self.__A[a]
    self.__A = Temp1
  
  def __make_array(self, c):
    return (c * ctypes.py_object)()
  
  def get_cap(self):
    return self.__capacity

  def __getitem__(self, k):
    """return element at index"""
    if k <= 0 or k >= self.__n:
        raise IndexError("invalid index")
    
    return self.__A[k]

  def __len__(self):
    return self.__n

  def __str__(self):
    if self.__n == 0:
        return "[]"

    out = '['
    for i, element in enumerate(self.__A):
        try:
            out += str(element) + ', '
            temp = self.__A[i+1]
        except:
            break
    return out[:-2] + ']'