# input=array
# output=int==>sum of all the records
# operations:


# ops = ["5","2","C","D","+"]
# records=[]
# iterate the list:
    # if char.isnum():
        # list.append(int(char))
    # elif char=='+':
        #total= list[-1]+list[-2]
        # list.append(total)
    # elif char=='D':
        # double=list[-1] *2
        # list.append(double)
    # elif char =='C':
        # list.pop()
# return the sum of the elements in the list

# ops = ["5","2","C","D","+"]
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records=[]
        for char in operations:
            print(records)
            if char =="+":
                total=records[-1]+records[-2]
                records.append(total)
            elif char =="D":
                double=records[-1] *2
                records.append(double)
            elif char == "C":
                records.pop()
            else:
                records.append(int(char))
        return sum(records)
        

        