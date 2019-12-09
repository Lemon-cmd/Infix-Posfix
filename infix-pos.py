def infix_to_postfix(input_str):
    """Takes in an expression written in the common infix notation and transforms it into an expression
    in the postix notation"""
    precedence = {'(': 1, '-': 2, '+': 2, '/': 3, '*': 3, '^': 4}
    op_stack = Stack(30)
    
    postfix_list = []
    token_list = input_str.split()
    
    for token in token_list:
        if ");" in token:
            token = token.replace(");", "")
        
        elif ";" in token:
            token = token.replace(";", "")
        
        elif "(" in token and "()" not in token:
            token = token.replace("(", "")
        
        elif ")" in token and "()" not in token:
            token = token.replace(")", "")
        
        if token not in "^*/+-()":
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            while op_stack.peek() != '(':
                postfix_list.append(op_stack.pop())
            op_stack.pop()
        else:
            prec = precedence[token]
            while (not op_stack.is_empty()) and \
                  ((token != "^" and precedence[op_stack.peek()] >= prec) or (precedence[op_stack.peek()] > prec)):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
    
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    return ' '.join(postfix_list)

