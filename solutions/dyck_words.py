def is_a_dyck_word(word: str) -> bool:
    stack = []
    
    for char in word:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
        elif char == '<':
            stack.append(char)
        elif char == '>':
            if not stack:
                return False
            stack.pop()
        elif char == '«':
            stack.append(char)
        elif char == '»':
            if not stack:
                return False
            stack.pop()
        elif char == '[':
            stack.append(char)
        elif char == ']':
            if not stack:
                return False
            stack.pop()
        elif char == '→':
            stack.append(char)
        elif char == '←':
            if not stack:
                return False
            stack.pop()
        elif char == '「':
            stack.append(char)
        elif char == '」':
            if not stack:
                return False
            stack.pop()                        
        elif char == '{':
            stack.append(char)
        elif char == '}':
            if not stack:
                return False
            stack.pop()
        elif char == '☹':
            stack.append(char)
        elif char == '☺':
            if not stack:
                return False
            stack.pop()
        else:
            return False
    
    return len(stack) == 0
