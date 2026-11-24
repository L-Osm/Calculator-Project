# Almost 3 hours to develop, started on 23/11/26 and finished on 24/11/26.
# Future versions will come in the following weeks.

print("------------------------------")
print("----------Calculator----------")
print("------------------------------")
print("Basic Arithmetic Calculator [Enter calculations like so: 3 * 7 / 2 - 5]")
print("Syntax: Enter values normally [decimals + negative numbers accepted]")
print("Use *, /, and () for multiplication, division and brackets.")
print("------------------------------")
print("Note: Do not enter an operation before a bracket, e.g. 6 / (4 * 2).")
print("Perform the bracketed calculation seperately, note it down, and then use it in other calculations.")
print()

math_list = []

class Calculator:
    def calculate(self, math_list):
         def current_token():
          return tokens[0] if tokens else None

         def consume_token():
          return tokens.pop(0) if tokens else None
         
         def parse_expression():
           result = parse_term()
           while current_token() in ('+', '-'):
             op = consume_token()
             if op == '+':
                result += parse_term()
             elif op == '-':
                result -= parse_term()
           return result

         def parse_term():
           result = parse_factor()
           while current_token() in ('*', '/'):
            op = consume_token()
            if op == '/':
               divisor = parse_factor()
               if divisor == 0:
                 raise ValueError("Cannot divide by zero.")
               result /= divisor
            elif op == '*':
               result *= parse_factor()
           return result

         def parse_factor():
           if current_token() == '(':
            consume_token() # consume '('
            result = parse_expression()
            if current_token() != ')':   # 4. Checks that ')' is next
              raise ValueError("Missing closing ')'")
            consume_token() # consume ')'
            return result
           elif current_token() == '-':
            consume_token() # handles negative numbers like -5
            return -parse_factor()
           elif current_token() is None:
            raise ValueError("Unexpected end of expression")
           else:
             return float(consume_token())
          
         def tokenise():
             result = []
             i = 0
             while i < len(math_list):
              char = math_list[i]
        
              if char == ' ':
                i += 1  # Skip spaces
              elif char in '+-*/()':
                result.append(char)
                i += 1
              elif char.isdigit() or char == '.':
                # Keep reading until the full number (including decimals) ends
                num_str = ''
                while i < len(math_list) and (math_list[i].isdigit() or math_list[i] == '.'):
                   num_str += math_list[i]
                   i += 1
                result.append(num_str)
              else:
                raise ValueError("Unknown character:", char)
            
             return result
         
         tokens = tokenise()
         return parse_expression()

while True:
    math_list = str(input("Enter some calculations (or q to quit, press Enter when done): "))
    if math_list == 'q':
        break
    calc = Calculator()
    try:     
      answer = calc.calculate(math_list)
      print(answer)
    except ValueError as e:
      print("Error:", e)
    except Exception as x:
      print("Error, invalid mathematical expression.")