#!/usr/bin/env python
# coding: utf-8

# In[23]:


def fac(num):
    
    if(num > 1):
        return num * fac(num - 1)
    elif(num == 1):
        return 1
    else:
        return 0
    
if __name__ == "__main__":
    print("Q4.0부터 14까지의 짝수의 팩토리얼을 출력")
    for n in range(1, 9):
        print("{0:d}! = {1:d}".format(2*n-2, fac(2*n - 2)))

