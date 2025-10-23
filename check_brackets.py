from stack import Stack


def check_brackets(brackets: str) -> str:
        
    stack1, stack2, stack3 = [Stack() for _ in range(3)]

    bracket_dict = {
        '{': stack1, 
        '}': stack1,
        '(': stack2,
        ')': stack2,
        '[': stack3,
        ']': stack3
    }

    for lett in brackets:
      
        stack = bracket_dict.get(lett)
        if not stack:
            return 'В строке есть символы отличные от скобок'

        if lett in ('(', '{', '['):
            stack.push(lett)
        elif lett in (')', '}', ']'):
            if stack.is_empty():
                return 'Несбалансированно'
            else:
                stack.pop()

    if stack1.is_empty() and stack2.is_empty() and stack3.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'

    

if __name__ == '__main__':
    
    str1 = '(((([{}]))))'
    str2 = '[([])((([[[]]])))]{()}'
    str3 = '{{[()]}}'
    str4 = '}{}'
    str5 = '{{[(])]}}'
    str6 = '{1}'
    str7 = '{1(}'

    print(check_brackets(str1))
    print(check_brackets(str2))
    print(check_brackets(str3))
    print(check_brackets(str4))
    print(check_brackets(str5))
    print(check_brackets(str6))
    print(check_brackets(str7))