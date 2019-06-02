
Sample_DNA = 'GATGGAACTTGACTACGTAAATT'

def dna_to_rna(dna_seq):
    final = []
    characters = list(dna_seq)
    for i in characters:
        if i != 'T':
            final.append(i)
        else:
            final.append('U')

    print(''.join(final))
if __name__ == '__main__':
    dna_to_rna(Sample_DNA)
