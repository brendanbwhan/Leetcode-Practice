class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for x in tokens:
            if x == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif x == '-':
                temp = int(stack.pop())
                stack.append(int(stack.pop()) - temp)
            elif x == '/':
                temp = int(stack.pop())
                stack.append(int(int(stack.pop()) / temp))
            elif x == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            else:
                stack.append(x)
        
        return int(stack[-1])
