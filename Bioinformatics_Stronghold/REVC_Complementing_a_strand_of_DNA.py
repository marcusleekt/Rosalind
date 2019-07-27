def findComplementary(DNA_sequence):
    def __complement(nucleotide):
        nucleotides = {
            "A":"T",
            "C":"G",
            "G":"C",
            "T":"A"
        }
        return nucleotides[nucleotide]

    return "".join(reversed(list(map(__complement, DNA_sequence))))

if __name__ == "__main__":
    DNA_sequence = input("Input DNA sequence: ")

    print(findComplementary(DNA_sequence))