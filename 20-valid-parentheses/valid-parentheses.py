# input:string
# output:boolean

# 1-)  wrong
# 2- (] wrong
# 3-([)] wrong
# stack=[]
# hashmap=> key:closing -> opening 
# hashmap={')' : '('}
# iterate through the string:
    # if stack is not empty  and stack[-1]==hashmap[char]:
        # remove the char 
    # else:
        # append it to the stack
# return True if the stack is empty otherwise false

# '()'
class Solution:
    def isValid(self, s: str) -> bool:
        parenthese_dict={')' : '(' ,'}' :'{' , ']' : '['}
        stack=[]

        for char in s:
            if stack and char in parenthese_dict.keys() and stack[-1]==parenthese_dict[char]:
                stack.pop()
            else:
                stack.append(char)
        return True if not stack else False
        