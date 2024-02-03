def maxSubArray(nums):
        sum = nums[0]
        sum2 = 0
        temp=0
        if len(nums)==1:
              return sum
        for i in nums[1:]:
            if i>sum and sum<0:
                sum=i
                continue
            if i > sum and sum2<0:
                  sum=i
                  sum2=0
                  if temp>0:
                        sum+=temp
                  continue
            if sum==0 and i<0:
                 continue
            if i>0 and sum==0:
                  sum=i
                  continue
            if sum>0 and i<0 and sum2==0:
                  sum2=i
                  continue
            if i>0 and sum2!=0:
                  sum2+=i
                  temp+=i
                  continue
            if i>0 and sum2==0:
                  sum+=i
                  continue
            if i<0 and sum2>0:
                  sum+=sum2
                  sum2=i
                  continue
            if i<0 and sum2<0:
                  sum2=i
                  if abs(i)<temp:
                        temp+=i
        if sum2>0:
            return sum+sum2
        else:
              return sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))