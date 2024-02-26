import numpy as np

# Fungsi keanggotaan untuk variabel input A


def membership_A(x):
    if x <= 30:
        return 1
    elif 30 < x <= 70:
        return (70 - x) / 40
    else:
        return 0

# Fungsi keanggotaan untuk variabel input B


def membership_B(x):
    if x <= 50:
        return 1
    elif 50 < x <= 80:
        return (80 - x) / 30
    else:
        return 0

# Fungsi keanggotaan untuk variabel output Z


def membership_Z(x):
    return x / 100

# Fuzzyfikasi


def fuzzyfication(input_A, input_B):
    fuzzy_A = membership_A(input_A)
    fuzzy_B = membership_B(input_B)
    return fuzzy_A, fuzzy_B

# Inferensi


def inference(fuzzy_A, fuzzy_B):
    rule1 = min(fuzzy_A, fuzzy_B)
    rule2 = fuzzy_A
    rule3 = fuzzy_B

    return rule1, rule2, rule3

# Defuzzifikasi


def defuzzification(rule1, rule2, rule3):
    output_Z = (rule1 * 50 + rule2 * 70 + rule3 * 90) / (rule1 + rule2 + rule3)
    return output_Z


# Input
input_A = float(input("Masukkan nilai untuk A (0-100): "))
input_B = float(input("Masukkan nilai untuk B (0-100): "))

# Fuzzyfikasi
fuzzy_A, fuzzy_B = fuzzyfication(input_A, input_B)

# Inferensi
rule1, rule2, rule3 = inference(fuzzy_A, fuzzy_B)

# Defuzzifikasi
output_Z = defuzzification(rule1, rule2, rule3)

print(f"Hasil defuzzifikasi: {output_Z}")
