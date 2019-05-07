#returns hamming distance, counting point mutations

def main(path):
    file = open(path, "r")
    data = file.read()
    items = data.split("\n")
    diff_count(items[0], items[1])

def diff_count(string1, string2):
    count = 0
    for idx, val1 in enumerate(string1):
        if val1 != string2[idx]:
            count += 1
    print(count)

if __name__ == '__main__':
    main("./data/rosalind_hamm.txt")
