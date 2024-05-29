def reverse_complement(sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N', 'R':'Y', 'Y':'R', 'M':'K', 'K':'M', 'S':'W', 'W':'S'}
    return "".join(complement[base] for base in reversed(sequence.upper()))

def convert_fasta_to_antisense(fasta_file):
    with open(fasta_file, 'r') as file:
        lines = file.readlines()
    
    antisense_fasta = ""
    current_sequence = ""
    header = ""

    for line in lines:
        if line.startswith('>'):
            if current_sequence:
                antisense_sequence = reverse_complement(current_sequence)
                antisense_fasta += f"{header}_antisense\n"
                antisense_fasta += '\n'.join([antisense_sequence[i:i+60] for i in range(0, len(antisense_sequence), 60)]) + '\n'
            header = line.strip()
            current_sequence = ""
        else:
            current_sequence += line.strip()
    
    if current_sequence:  # Add the last sequence
        antisense_sequence = reverse_complement(current_sequence)
        antisense_fasta += f"{header}_antisense\n"
        antisense_fasta += '\n'.join([antisense_sequence[i:i+60] for i in range(0, len(antisense_sequence), 60)]) + '\n'

    output_file = fasta_file.replace('.fasta', '_antisense.fasta')
    with open(output_file, 'w') as file:
        file.write(antisense_fasta)
    
    return output_file

# Example usage
input_fasta = '/Users/jibk/Downloads/GCF_000003025.6_Sscrofa11.1_genomic.fna'
antisense_fasta = convert_fasta_to_antisense(input_fasta)
print(f"Antisense FASTA saved to: {antisense_fasta}")
