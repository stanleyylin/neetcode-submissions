class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.isdigit() or (token.startswith("-") and token[1:].isdigit()):
                stack.append(int(token))
            else:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                match token:
                    case "+":
                        result = operand_1 + operand_2
                    case "-":
                        result = operand_1 - operand_2
                    case "*":
                        result = operand_1 * operand_2
                    case "/":
                        result = int(operand_1 / operand_2)
                    case _:
                        raise ValueError(f"Invalid operator: {token}")
                stack.append(result)
        
        return stack[0] if stack else 0
                
                    
