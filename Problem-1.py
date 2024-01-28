def is_valid_parentheses(string):
   Open = "([{"
   close = ")]}"
   stack = []
   for i in string:
      if i in Open:
        stack.append(i)
      elif i in close:
         if len(stack) == 0:
            return False
         if Open[close.index(i)] == stack[-1]:
            stack.pop()
         else:
            return False
   if string[-1] in Open:
       return False
   if len(stack) == 0:
            return True
      
      
  
string = input("Enter String:\n")

print(is_valid_parentheses(string))
