import random

class CFG:
    def __init__(self, non_terminals, terminals, production_rules, start_symbol):
        
        self.non_terminals = non_terminals 
        self.terminals = terminals 
        self.production_rules = production_rules 
        self.start_symbol = start_symbol 

    def generate_string(self, max_length=10, max_derivations=50):
        
        current_string = self.start_symbol
        derivations_count = 0

        while any(nt in self.non_terminals for nt in current_string) and derivations_count < max_derivations:
            if len(current_string) > max_length: 
                return None 

            found_non_terminal = False
            for i, char in enumerate(current_string):
                if char in self.non_terminals:
                    replacements = self.production_rules.get(char)
                    if replacements:
                        chosen_replacement = random.choice(replacements)
                        current_string = current_string[:i] + chosen_replacement + current_string[i+1:]
                        found_non_terminal = True
                        break
            if not found_non_terminal:
                break 

            derivations_count += 1

        if all(t in self.terminals for t in current_string) and len(current_string) <= max_length:
            return current_string
        return None

    def derive_path(self, target_string):
        
        path = []
        
        def derive(current_symbol_string, target, steps_taken=0, max_steps=50):
            path.append(current_symbol_string) 

            if current_symbol_string == target: 
                return True
            
            if steps_taken > max_steps or len(current_symbol_string) > len(target) * 2 + 2: 
                path.pop()
                return False

            for i, char in enumerate(current_symbol_string):
                if char in self.non_terminals:
                    non_terminal = char
                    
                    for replacement in self.production_rules.get(non_terminal, []):
                        new_string = current_symbol_string[:i] + replacement + current_symbol_string[i+1:]
                        if derive(new_string, target, steps_taken + 1):
                            return True
                    break 
            
            path.pop() 
            return False

        if derive(self.start_symbol, target_string):
            print("Derivation Steps:")
            for step in path:
                print(step)
            return True
        else:
            print(f"No derivation found for '{target_string}' within limits.")
            return False

    def checker(self, input_string):
        
        if len(input_string) > 12:
            return False

        def check(current_string, remaining_input):
            if not remaining_input and not current_string:
                return True
            if not remaining_input and current_string:
               
                if current_string == 'S' and '' in self.production_rules.get('S', []):
                    return True 
                return False
            if not current_string and remaining_input:
                return False

            if current_string[0] in self.terminals:
                if remaining_input and current_string[0] == remaining_input[0]:
                    return check(current_string[1:], remaining_input[1:])
                else:
                    return False
            elif current_string[0] in self.non_terminals:
                non_terminal = current_string[0]
                for production in self.production_rules.get(non_terminal, []):
                    if check(production + current_string[1:], remaining_input):
                        return True
                return False
            else: 
                return False

        return check(self.start_symbol, input_string)

# Task 1: Define a CFG 
# The grammar is S -> aSb | epsilon 
non_terminals = {'S'}
terminals = {'a', 'b'}
production_rules = {
    'S': ['aSb', ''] 
}
start_symbol = 'S'

cfg = CFG(non_terminals, terminals, production_rules, start_symbol)

if __name__ == "__main__":
    print("Task 1:CFG ")
    print(f"Non-terminals: {cfg.non_terminals}")
    print(f"Terminals: {cfg.terminals}")
    print(f"Production Rules: {cfg.production_rules}")
    print(f"Start Symbol: {cfg.start_symbol}")
    print()
    print("Task 2: String Generator ")
    
    nr = 0
    while nr < 10: 
        s = cfg.generate_string(max_length=10) 
        if s is not None:
            print(f"Generated string: '{s}' (Length: {len(s)})")
            nr += 1
  
    print()
    print(" Task 3: Derivation ")
    test_strings_derivation = ["aabb", "aaabbb", "ab", "",'aab']
    for i in test_strings_derivation:
        print(f"\nDerivation for: '{i}'")
        cfg.derive_path(i)
        print()
   
    print()
    print("Task 4: Membership Tester")
    test_strings_membership = ["aabb", "ab", "", "aaabbb", "aab", "aba", "bbbaaa", "aaaaabbbbb",'aaaaaaaaaa',"abba", "ababab", "aaab"]
   
    for i in test_strings_membership:
        is_member = cfg.checker(i)
        print({i},'==',{is_member}) 
   