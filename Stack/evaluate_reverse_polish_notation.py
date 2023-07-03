def eval_rpn(tokens):
    stack = []

    for i in tokens:
        if i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '-':
            x, y = stack.pop(), stack.pop()
            stack.append(y - x)
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
        elif i == "/":
            x, y = stack.pop(), stack.pop()
            stack.append(int(float(y) / x))
        else:
            stack.append(int(i))

    return int(stack[0])

print(eval_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
