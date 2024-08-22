def main(input_str: str) -> str:
    
    operators = {'+', '-', '*', '/'}
    
    try:
        parts = input_str.split()
        
        if len(parts) != 3:
            raise ValueError("throws Exception")
        
        a_str, operator, b_str = parts
        
        if operator not in operators:
            raise ValueError
        
        a = int(a_str)
        b = int(b_str)
        
        if not (1 <= a <= 10) or not (1 <= b <= 10):
            raise ValueError("throws Exception")
        
        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            result = a // b
            
        return str(result)
    
    except Exception as e:
        return str(e)
    
print(main("1 + 2"))
print(main("10 - 3"))
print(main("6 * 9"))
print(main("8 / 4"))
print(main("10 / 3"))
print(main("1"))
print(main("15 + 25"))
print(main("1 + 2 + 3 * 5"))
