class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val == '+':
                stack.append(stack.pop() + stack.pop())
            elif val == '-':
                stack.append(-(stack.pop()) + stack.pop())
            elif val == '*':
                stack.append(stack.pop() * stack.pop())
            elif val == '/':
                divisor = stack.pop()
                dividend = stack.pop()
                stack.append(int(dividend / divisor))
            else:
                stack.append(int(val))
        
        return stack[0]