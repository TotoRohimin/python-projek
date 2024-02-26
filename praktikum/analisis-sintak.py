from pyparsing import Word, alphas, nums, Literal, Suppress, Forward, Group, Optional

# Aturan leksikal sederhana
identifier = Word(alphas, alphas + nums + "_")
integer = Word(nums)

# Aturan sintaksis
if_keyword = Literal("if")
else_keyword = Literal("else")
open_paren = Suppress("(")
close_paren = Suppress(")")
colon = Suppress(":")

# Ekspresi untuk menyusun aturan if-else
expression = Forward()
if_statement = Group(if_keyword + open_paren + expression + close_paren + colon + expression)
else_statement = Group(else_keyword + colon + expression)
expression << (if_statement + Optional(else_statement))

# Contoh kode sumber
source_code_example = """
if (x > 0):
    print("Positive")
else:
    print("Non-positive")
"""

# Fungsi untuk menjalankan analisis sintaks
def parse_syntax(input_code):
    return expression.parseString(input_code, parseAll=True)

# Eksekusi parsing dan jalankan hasilnya
try:
    parsed_result = parse_syntax(source_code_example)
    print("Analisis sintaks berhasil.")
    print("Hasil parsing:", parsed_result)

    # Eksekusi hasil parsing
    if parsed_result[0][0]:
        print("Condition is True. Executing if block.")
        exec("\n".join(parsed_result[0][1]))
    elif parsed_result[0][1]:
        print("Condition is False. Executing else block.")
        exec("\n".join(parsed_result[0][1]))

except Exception as e:
    print("Kesalahan sintaks:", e)
