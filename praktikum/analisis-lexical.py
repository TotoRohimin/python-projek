import re

def lexical_analysis(source_code):
    # Definisikan pola token menggunakan regular expressions
    patterns = [
        (r'\bif\b', 'IF_KEYWORD'),
        (r'\belse\b', 'ELSE_KEYWORD'),
        (r'\bwhile\b', 'WHILE_KEYWORD'),
        (r'\bfor\b', 'FOR_KEYWORD'),
        (r'\bint\b', 'INT_KEYWORD'),
        (r'\bfloat\b', 'FLOAT_KEYWORD'),
        (r'\bprint\b', 'PRINT_KEYWORD'),
        (r'\b(\d+(\.\d+)?)\b', 'NUMBER'),  # Mendeteksi angka, termasuk float
        (r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', 'IDENTIFIER'),  # Mendeteksi identifier
        (r'\b(\+\+|--|\+=|-=|\*=|/=|==|!=|<=|>=)\b', 'OPERATOR'),  # Mendeteksi operator
        (r'\b[\(\)\{\}\[\];,]\b', 'PUNCTUATION'),  # Mendeteksi tanda baca
    ]

    tokens = []

    for pattern, token_type in patterns:
        matches = re.finditer(pattern, source_code)
        for match in matches:
            tokens.append((match.group(), token_type))

    return tokens

# Contoh kode sumber
source_code_example = """
#include <stdio.h>

int main() {
    // Deklarasi variabel
    float sisi, luas;

    // Meminta pengguna memasukkan panjang sisi persegi
    printf("Masukkan panjang sisi persegi: ");
    scanf("%f", &sisi);

    // Menghitung luas persegi
    luas = sisi * sisi;

    // Menampilkan hasil
    printf("Luas persegi dengan sisi %.2f adalah %.2f\n", sisi, luas);

    return 0;
}
"""

# Jalankan analisis leksikal
result_tokens = lexical_analysis(source_code_example)

# Tampilkan hasil
for token, token_type in result_tokens:
    print(f"{token}: {token_type}")
