import sys

def main(input_str: str) -> str:
    
    operators = {'+', '-', '*', '/'}
    
    try:
        
        parts = input_str.split()
        
       
        if len(parts) != 3:
            raise ValueError("throws Exception")  
        
        a_str, operator, b_str = parts
        
        
        if operator not in operators:
            raise ValueError("throws Exception")  
        
        
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

if __name__ == "__main__":
    
    input_str = input("Введите выражение: ")
    
   
    print(main(input_str))

