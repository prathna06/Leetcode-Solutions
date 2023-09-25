class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        newArr=[]
        i=0
        formattedArr =[]
        while(i<len(nums)):
            if len(newArr) !=0 and nums[i]-1 == newArr[-1][-1]:
                newArr[-1][-1]=nums[i] 
            else:
                newArr.append([nums[i],nums[i]])                       
            i+=1
        for i,j in newArr:
            if i ==j:
                formattedArr.append("{}".format(i))
            else:
                formattedArr.append("{}->{}".format(i,j))
        return formattedArr

        print(newArr)

 
        