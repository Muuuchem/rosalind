comp = {
    'A':'T',
    'G':'C',
    'T':'A',
    'C':'G',
}

def rev_palindromes(seq):
    palindromes = []
    length = len(seq)
    for i in range(length):
        j = i + 1
        while j < length+1:
            current = seq[i:j]
            if len(current) in range(4, 13) and rev_comp(current, i+1) == current:
                palindromes.append(current)
                print(i+1, len(current))
            j += 1
    return palindromes
  

def rev_comp(seq, j):
    final = ''
    for i in reversed(seq):
        final += comp[i]
    return final

def split_title(fasta):
    split = fasta.split('\n')
    return ''.join(split[1:])


if __name__ == '__main__':
    path = './data/rosalind_revp.txt'
    file = open(path, "r")
    inp = split_title(file.read())
    rev_palindromes(inp)