from DNAtoolkit import *
from Utilities import *

DNAStr = validateSeq("GGTGGTGTGCGGAGCGAGTGCGAGAGTC")

print(f'\nSequence: {colored(DNAStr)}\n')
print(f"[1] + Sequence lenght: {len(DNAStr)}\n")
print(colored(f'[2] + Nucleotide frequency: {countNucFrequency(DNAStr)}\n'))
print(f'[3] + DNA/RNA Transcription: {colored(transcription(DNAStr))}\n')
print(f"[4] + DNA String + Reverse Complement: \n5' {colored(DNAStr)} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(colored(f"3' {(reverse_complement(DNAStr))[::-1]}5' [Complement]\n"))
print(f"5' {colored(reverse_complement(DNAStr))} 3' [Reverse complement]\n")