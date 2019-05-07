

def reverse_complement(strand):
    characters = list(strand)
    final = []
    for i in characters:
        if i == 'A':
            final.append('T')
        elif i == 'T':
            final.append('A')
        elif i == 'G':
            final.append('C')
        elif i == 'C':
            final.append('G')

    print(''.join(final[::-1]))

if __name__ == '__main__':
    sample = 'CAATGCCCGCAAACTCTCAACACTGCTACGTGTTCGAATCAACAAGCTCCGGATTTGTAACCAGCAACAAGTCGGGCGACCTCCCGTTTAAAACGAGTAGCGCAGAGTCCAGTCAATGAGTAGCTCAGCCCTCTCTTCAGTATCTTCACGGCGAAGGATTGGATGTTTAACACAGTTCCCGGTCGGGCTGGGTTTTTTGCGCCAGAAGTTCATGTCAGAAAGCCGGGGGCTAAGCCACATATTACCGGTCACGTGGTGTAGGCATCATACCCATTGGTGTCACTGATTACACGACGCGGATGCCTCCACCCAGCCAATATTAAAAGCCCTTTCGAGGTGTGGCGGTAGCTAACGATTAGACAAACCCGTTCCCGTTGTTGAAGTATCCCCTCTAAGACCTGCTCCACGGTCCGGATTAAACTGAGGTTTTTGTACTGCTCCGCTATAGAACCGGTCAGATATGGGGTTAAAGCACAATTCGGCACACCTAACCCGGAGGACAAGTGCCGGCGGACCACTGAATGCGGTATATGTACGCGGTTTGTTCGAACAGGTAGCCAGGCAGCGAGCGCGCCCACCCAGGGCATTCGTGCGCGCTAATTTATAACAAAGCCCTTCATACAATCGCAATCGGAGGGTAAAAAGCGGCGCTGATGCGCTTCTTTGCATCCAAAGCGCATAGTATCTTTCGTTTCGTAAGAATGCAGCGTCGCGAGACTATTGCATTGCAGCATAACCTTAGGGTATGCCAACCCCAGCCAGTAAGCCGTGAGAGTGTTACGTGATGGACCCGGGAAGGGGGCCAAGGTGCTTAGTAAGGACGTATGTCGACCGCTCCCGCTCTGCCAAGC'
    reverse_complement(sample)