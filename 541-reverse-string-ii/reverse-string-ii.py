# s="abc"   k=2
# output = "bac"

# s="abcdefghij" k=3
# output=cbadefihgj

# input ==>string , int
# out=string

# opeartion :

# i=0
# j=i+2k

# iterate through the string: 
    # if we can slice 2k:
        # slice k
        # reverse the first k strings 
        # join them to the second k 
    # else:
        # if we slice k elements :
            # slice k elements
            # reverse the first k elemts
            # join them to remaining
        # else:
            # reverse



            



class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        result=''

        for i in range(0,len(s),2*k):
            j=i+2*k
            if j<len(s):
                sliced_string= s[i:i+k]
                reversed_string=sliced_string[::-1]
                print(reversed_string)
                result+=reversed_string+ s[i+k:i+2*k]
            else:
                z=i+k
                if z< len(s):
                    sliced_string= s[i:i+k]
                    reversed_string=sliced_string[::-1]
                    result+= reversed_string + s[i+k:len(s)]
                else:
                    sliced_string=s[i:len(s)]
                    reversed_string=sliced_string[::-1]
                    result+=reversed_string
        return result 




                
        