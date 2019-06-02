
data = {
    'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V',
    'UUC':'F', 'CUC':'L', 'AUC':'I', 'GUC':'V',
    'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V',
    'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V',
    'UCU':'S', 'CCU':'P', 'ACU':'T', 'GCU':'A',
    'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A',
    'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A',
    'UCG':'S', 'CCG':'P', 'ACG':'T','GCG':'A',
    'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D',
    'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D',
    'UAA':'Stop', 'CAA':'Q', 'AAA':'K', 'GAA':'E',
    'UAG':'Stop', 'CAG':'Q', 'AAG':'K', 'GAG':'E',
    'UGU':'C', 'CGU':'R', 'AGU':'S', 'GGU':'G',
    'UGC':'C', 'CGC':'R', 'AGC':'S', 'GGC':'G',
    'UGA':'Stop', 'CGA':'R', 'AGA':'R', 'GGA':'G',
    'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G',
}

def main(path):
    file = open(path, "r")
    input = file.read()
    count = possible_mrna_count(input.rstrip())
    final = count % 1000000
    print(final)

def possible_mrna_count(pro_seq):
    poss_count = {}
    for key, val in data.items():
        if val not in poss_count:
            poss_count[val] = 1
        else:#counting number of possible codons per AA
            poss_count[val] += 1
    count = 1
    for i in pro_seq:
        count *= poss_count[i]

    return count * poss_count['Stop']


if __name__ == '__main__':
    path = './data/rosalind_mrna.txt'
    main(path)