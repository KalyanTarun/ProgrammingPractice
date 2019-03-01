# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 15:46:47 2019

@author: Tarun
"""
#Edit Distance problem using a recursive approach

def EditDist(str1,str2,m,n):
    #The following are three terminating conditions for the problem
    
    #If both the strings reach to end then no operations are required hence return 0
    if m==len(str1) and n==len(str2):
        return 0
    #If target string reaches to the end i.e the extra content of the source string is to be removed
    if n==len(str2):
        return len(str2)-m
    
    #If source string reaches to the end i.e contents need to be added to it
    if m==len(str1):
        return len(str1)-n
    
    #If there is a match of characters then move both indices forward
    if str1[m]==str2[n]:
        return EditDist(str1,str2,m+1,n+1)
    
   """
   1)Insert into source string i.e m,n+1
   2)Replace the source string i.e m+1,n+1
   3)Remove the character in source string
   """
    else:
        return min(EditDist(str1,str2,m,n+1),EditDist(str1,str2,m+1,n+1),EditDist(str1,str2,m+1,n))+1
    
    
def main():
    str1="cat" #source string
    str2="cut" #Target string
    print(EditDist(str1,str2,0,0))
    
if __name__ == "__main__":
    main()
