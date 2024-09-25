# binary search through rows(outer array):
    # rows,cols:len(matrix),len(matrix[0])
    # top,bottom:matrix[0],rows-1
    # while top<=bottom:
        # middle_row=(top+bottom)//2
        # if(target >matrix[middle_row][-1]):
            # top=middle_row+1
        # elif( target <matrix[middle_row][0]):
            # bottom:middle_row-1
        # else:
            # break
        
    # if()

        
# binary search through cols (outter array)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix),len(matrix[0])

        top,bottom=0,rows-1
        while top<=bottom:
            middle_row=(top+bottom)//2
            if (target > matrix[middle_row][-1]):
                top=middle_row+1
            elif(target<matrix[middle_row][0]):
                bottom=middle_row-1
            else:
                break
        if not (top<=bottom):
            return False
        
        middle_row=(top+bottom)//2

        low,high=0,cols-1
        while low<=high:
            middle=(high+low)//2
            if (target > matrix[middle_row][middle]):
                low=middle+1
            elif (target < matrix[middle_row][middle]):
                high=middle-1
            else:
                return True
        return False

        
        