import re

def lexer(input_text):
    tokens = []
    while input_text:
        if input_text.startswith(' '):
            input_text = input_text[1:]
        elif input_text.startswith('+') or input_text.startswith('-') or input_text.startswith('*') or input_text.startswith('/') or input_text.startswith('%'):
            tokens.append(('OPERATOR', input_text[0]))
            input_text = input_text[1:]
        else:
            match = re.match(r"[a-zA-Z][a-zA-Z0-9]*", input_text)
            if match:
                tokens.append(('IDENTIFIER', match.group()))
                input_text = input_text[len(match.group()):]
            else:
                # Handle kesalahan jika karakter tidak sesuai dengan aturan
                raise Exception(f"Token tidak valid: {input_text}")
    return tokens

# Contoh penggunaan lexer
input_program = "x = 10 + y * 5"
tokens = lexer(input_program)
print(tokens)
