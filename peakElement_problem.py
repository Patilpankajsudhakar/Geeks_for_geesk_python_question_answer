'''Given an 0-indexed array of integers arr[] of size n, find its peak element and return it's index. An element is considered to be peak if it's value is greater than or equal to the values of its adjacent elements (if they exist).

Note: The output will be 1 if the index returned by your function is correct; otherwise, it will be 0.

#Examples :

Input: n = 3, arr[] = {1, 2, 3} 
Output: 1
Explanation: If the index returned is 2, then the output printed will be 1. Since arr[2] = 3 is greater than its adjacent elements, and there is no element after it, we can consider it as a peak element. No other index satisfies the same property, so answer will be printed as 0.
'''

# Solution
# used here dsa concept called solve small and big problem
Class Solution:
  def __init__(self,arr,n):
    self.arr=arr
    self.n=n
  def PeakElement(self):
    if (self.n==1):
      return 0
    if self.arr[0] >= self.arr[1]:
      return 0
    if self.arr[n-1] >= self.arr[n-2]:
      return self.n-1
      
  for i in range(1,self.n-1):    # solve big problem if there adjecent is greater or equal to the number
    if (self.arr[i]>=self.arr[i-1] and self.arr[i]>=self.arr[i+1]):
      return i
    
