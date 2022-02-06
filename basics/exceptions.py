#Key concepts

#1. Raising an exception
#2. Handling an exception
#3. Unhandled exceptions
#4. Exception objects

import sys


DIGIT_MAP = {
    'zero':'0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}

def convert(s):
    try:
        number=''
        for token in s:
            number+=DIGIT_MAP[token]    
        
        return int(number)

    # you can merge except block
    except (KeyError,TypeError) as e:
        
        print(f"Conversion error{e!r}",file= sys.stderr)
        return -1
