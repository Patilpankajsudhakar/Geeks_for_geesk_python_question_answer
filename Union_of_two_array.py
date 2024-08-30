# to buid logic layman way approch

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,arr1,arr2):
        #code here
        arr_final=[]
        for ele in arr1:
            if ele not in arr_final:
                arr_final.append(ele)
        for ele1 in arr2:
            if ele1 not in arr_final:
                arr_final.append(ele1)
        return len(arr_final)

# function approch
class Solution:
  def Union_two_array(self,arr1,arr2):
      set1=set(arr1)
      set2=set(arr2)
      final_arr=list(set1.union(set2))
  return len(final_arr)
