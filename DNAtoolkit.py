import collections
from Sequences import *

def validateSeq(dna_seq):
    """Validates the DNA String"""
    tempseq = dna_seq.upper()
    for nuc in tempseq:
        if nuc not in Nucleotides:
            return False
    return tempseq;

def countNucFrequency(dna_seq):
    """Counts Nucleotide frequency"""
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in dna_seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

def transcription(dna_seq):
    """Changes Bases to RNA bases"""
    return dna_seq.replace("T", "U")

def reverse_complement(dna_seq):
    return ''.join([DNAcomplements[nuc] for nuc in dna_seq])[::-1]


