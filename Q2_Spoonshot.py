#in this problem, we need to display the output array for a given input array based on an underlying pattern
import numpy as np

#taking the input from the user and converting it into a numpy array
in_lst = eval(input("Input  : "))
in_arr = np.array(in_lst)
out_arr = []

'''the underlying pattern for this problem is that at any given index, the output value at that index is the 
product of all terms in the input array except the element at that index in the input array'''
for i in range (len(in_arr)):
    temp_arr = np.delete(in_arr, i) #storing all the remaining elements of the input array and taking the product of that array
    out_arr.append(np.product(temp_arr))
print("Output :", out_arr)