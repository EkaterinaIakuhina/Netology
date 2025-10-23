from stack import Stack


def check_brackets(brackets: str) -> str:
        
    NUM = 3
    stacks = [Stack() for _ in range(NUM)]

    BRACKETS = '(){}[]'
    bracket_dict = {}

    for bracket in range(NUM * 2):
        key = BRACKETS[bracket]
        stacks_index = bracket // 2
        bracket_dict[key] = stacks[stacks_index]

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

    if sum(map(lambda x: x.size(), stacks)) == 0:
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
