#Stack Implementation

def create_stack(*num):
    return [*num]

def stack_push(stack, value):
    stack.append(value)

def stack_pop(stack):
    stack.pop()
    
def stack_peek(stack):
    return stack[-1]

def is_stack_empty(stack):
    return len(stack) == 0

def stack_to_string(stack):
    s = " TOP OF STACK\n"
    s += "-------------------\n"
    
    for v in reversed(stack):
        s+= str(v).center(20) + "\n"
    
    
        
    s += "-------------------\n"
    s += " BOTTOM OF STACK\n"
    
    print(s)
    

s = create_stack(100,80,60,70,60,75,80)
stack_to_string (s)

def stock_span_days(prices):
    
    days = []
    
    for i, price in enumerate(prices):
        c = 0
        
        for prev_price in prices[i::-1]:
            if prev_price > price:
                days.append(c)
                break
            else:
                c +=1
    return days
    
        
print(stock_span_days(s))

def stock_span_days2(prices):
    
    days = []
    
    st = create_stack(prices)
    
    while not is_stack_empty(st):
        prev_price = prices[stack_peek(st)]
        if prev_price > price:
            break
        else:
            stack_pop(st)
    
    
    for i, price in enumerate(prices):
        
        c = 0
        
        if is_stack_empty(st):
            c += 1
        else:
            c = i - stack_peek(st)
        
        days.append(c)
        stack_push(st, i)

print(stock_span_days(s))