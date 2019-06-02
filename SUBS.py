
def motif_in_dna(seq, sub):
    final = []
    i = 0
    slen = len(sub)
    while i < (len(seq)-slen):
        if seq[i:i+slen] == sub:
            print(i + 1)
        i += 1

if __name__ == '__main__':
    st = 'GTCCATTTTCCATTTGTCCATTTATCTATCAGGTCCATTTTCCATTTCCCTCCATTTTCCATTTGACAGGGTTCCATTTTCCATTTGTGTCCATTTTTTCCATTTTCCATTTTATCCATTTCATCCATTTTCCATTTCGTCCATTTCGACGCTTGTTCCATCCATTTTACCGCTCCATTTGCATCCATTTGCGTCCATTTGTTCCATTTCTCCATTTCTCCATTTACTACGTCCATTTTCCATTTATTCCATTTGGGTCCATTTTCCATTTAAGTGTCCATTTTCCATTTTCCATTTTCCATTTATCCATTTATACTCCATTTCGTCCATTTGTCATCCATTTGTCCATTTCTCCATTTCGTCCATTTTCCATTTCTTCCATTTATCCATTTCATATCCATTTTTCCATTTTCCATTTAATCCATTTGTCCATTTATCCATTTAATTCCATTTGTTCCATTTCAAAACTCCATTTTCCATTTCTCACGACGATCCATTTGTTGTCCATTTTCCATTTTCCATTTTCCATTTTAGACGTCTCCATTTTCCATTTTTCCATTTCTTATCCATTTTCCATTTTAATGTCCATTTTCCATTTATTCCATTTGGTCCATTTCATCCATTTTCCATTTCTCCATTTAATTCCATTTTCCATTTCTATCCATTTTCCATTTACTATCCATCCATTTGATCCATTTTGGCGTCCATTTGACGTTGATCCATTTCTCGAATTTGCACCTCCATTTCTCCATTTACTTCCATTTCTCCATTTGTCATTTCCATTTTCCATTTATATCCATTTGTCCATTTTCCGCTCCATTTGCATCCATTTTTCCATTTCTTCCATTTCATCCATTTTTCCATTTGGGTCGAAAAGTGCCTTCCATTTGATTCCATTT'
    s2 = 'TCCATTTTC'
    motif_in_dna(st, s2)