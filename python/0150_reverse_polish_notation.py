class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        stack = []
        for t in tokens:
            if t in operators:
                b = stack.pop()
                a = stack.pop()
                stack.append(int(self.evaluate(int(a), int(b), t)))
            else:
                stack.append(int(t))
        return stack.pop()
        
    def evaluate(self, a, b, operator):
        match operator:
            case "+":
                return a + b
            case "-":
                return a - b
            case "*":
                return a * b
            case "/":
                return a / b
            case _:
                raise Exception(f"Invalid operator {operator}")
            