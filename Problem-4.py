import numpy as np

def max_sum_ContSubArray(x):
    Array = np.array(x)
    Max = 0
    for j in range(1,Array.size):
     for i in range(0,Array.size): 
        if Array[i:i+j].sum() > Max:
            Max = Array[i:i+j].sum()
        if i+j == Array.size:
            break
    if Max < Array.sum():
       Max = Array.sum()
    print("Output:%d" %(Max))
try:    
  n = int(input("Enter Number of elements: "))
  user_list = []
  for i in range(0,n):
     user_list.append(int(input("Enter Element:\n")))
except:
    print("Invalid Input")
max_sum_ContSubArray(user_list)
