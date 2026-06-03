seq = ["ATATACGCGTA", "CTTCGGNGGA"]

for sequence in seq:
    print(f"\nПоследовательность: {sequence}")
    print("\nПострочно:")

    for nucleotide in sequence:
        print(nucleotide)

    print("-" * 35)
