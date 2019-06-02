def main(path):
    file = open(path, "r")
    fasta = file.read()
    chains = extract_items(fasta)
    counts = {}
    for chain in chains:
        count = count_GC(chains[chain])
        counts[chain] = count
    max = 0
    current = ""
    for title in counts:
        if counts[title] > max:
            max = counts[title]
            current = title
    print(current)
    print(max * 100)

def extract_items(fasta):
    split = fasta.split(">")
    chains = {}
    for value in split:
        if (value == ''):
            continue
        else:
            parts = value.split("\n")
            count = 0
            title = ""
            seq = ""
            for part in parts:
                cleaned = part.strip()
                if count == 0:
                    title = cleaned
                else:
                    seq += cleaned
                count += 1
            chains[title] = seq

    return chains

def count_GC(seq):
    count = 0
    for value in seq:
        if (value == "G" or value == "C"):
            count += 1

    #print(seq.count("G") + seq.count("C"))
    return count/len(seq)

if __name__ == '__main__':
    main('./data/rosalind_gc.txt')
