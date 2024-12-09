import ast
import astunparse  
 
mutant_counter = 0
class MutationVisitor(ast.NodeTransformer):
    def visit_BinOp(self, node):
            """
            Mutate binary operators (e.g., replace '+' with '-').
            """
            self.generic_visit(node)  # Ensure child nodes are processed
            if isinstance(node.op, ast.Add):  # Replace '+' with '-'
                node.op = ast.Sub()
                global mutant_counter
                mutant_counter += 1
            return node
    
def generate_mutants(file_path):
    """
    Read a Python file, generate mutants, and return the mutated code.
    """
    try:
        with open(file_path, "r") as file:
            code = file.read()
        
        # Parse the code into an AST
        tree = ast.parse(code)
        
        # Apply mutations
        mutator = MutationVisitor()
        mutated_tree = mutator.visit(tree)
        ast.fix_missing_locations(mutated_tree)  # Ensure AST is consistent
        
        # Convert the mutated AST back to code
        mutated_code = astunparse.unparse(mutated_tree)
        return mutated_code 
    except Exception as e:
            print(f"Error generating mutants: {e}")
            return None


file_path = "exCode.py"  
mutated_code = generate_mutants(file_path)



with open("mutated_code1.py", "w") as mutated_file:
    mutated_file.write(mutated_code)


print("Number of mutants generated: ", mutant_counter)

