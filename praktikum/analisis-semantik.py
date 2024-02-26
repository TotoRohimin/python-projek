import ast

class VariableDeclarationVisitor(ast.NodeVisitor):
    def __init__(self):
        self.declared_variables = set()

    def visit_FunctionDef(self, node):
        # Saat masuk ke fungsi, reset set variabel yang dideklarasikan
        self.declared_variables = set()
        self.generic_visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.declared_variables.add(target.id)
        self.generic_visit(node)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load) and node.id not in self.declared_variables:
            print(f"Error: bukan '{node.id}' used before declaration")

# Contoh kode sumber
source_code_example = """
# Simple Python code example

# Take user input
user_input = input("Enter a number: ")

# Check if the input is a positive number
try:
    number = float(user_input)
    if number > 0:
        print("The entered number is positive.")
    elif number == 0:
        print("The entered number is zero.")
    else:
        print("The entered number is negative.")
except ValueError:
    print("Invalid input. Please enter a valid number.")

"""

# Analisis sintaksis untuk mendapatkan AST (Abstract Syntax Tree)
ast_tree = ast.parse(source_code_example)

# Jalankan analisis semantik
semantic_analyzer = VariableDeclarationVisitor()
semantic_analyzer.visit(ast_tree)
