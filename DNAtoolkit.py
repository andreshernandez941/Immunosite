import collections

Nucleotides = ["A", "C", "G", "T"]
dict.DNANucleotides = {"A", "C", "G", "T"}
dict.RNANucleotides = {"A", "C", "G", "U"}

def validateSeq(dna_seq):
    tempseq = dna_seq.upper()
    for nuc in tempseq:
        if nuc not in Nucleotides:
            return False
    return tempseq + " is a valid DNA sequence";

def countNucFrequency(dna_seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in dna_seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict



