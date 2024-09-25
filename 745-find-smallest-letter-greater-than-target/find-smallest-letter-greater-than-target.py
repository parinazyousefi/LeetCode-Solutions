# input= array , target
# output= string ==> closest character in alph after the target target and if it does not exsit then return the first element of the array

# low=0
# high=len(letters)-1


# letters = ["c","f","j"], target = "c"
# l   m
# h
# if taget ascii value is greater than the ascii value of last element:
# return letters[i]

# while low <= high:
# middle=(high-low)//2
# if the the ascii value of the target is greater than middle element :
# low+=middle+1
# else if ascii value of the target is less than middle element :
# high= middle-1
# else:
# return the middle element
# return high


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters) - 1

        while low <= high:
            middle = low + (high - low) // 2

            if (
                letters[middle] > target
            ):  
                high = middle - 1
            else:
                low = middle + 1
        return letters[low % len(letters)]
