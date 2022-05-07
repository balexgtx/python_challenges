def validate(string):
    res = ''
    if 'def' not in string:
        return 'missing def'
    
    if ':' not in string:
        return 'missing :'
    
    if '(' not in string or ')' not in string:
        return 'missing paren'
    
    if '(' + ')' in string:
        return 'missing param'
    
    if '    ' not in string:
        return 'missing indent'
    
    if 'validate' not in string:
        return 'wrong name'
    
    if 'return' not in string:
        return 'missing return'
    
    
    return True
    

def run():
    string = 'def'
    print(validate(string))

if __name__ == "__main__":
    run()