#AUTHOR: Jyot Thesia
#DATE: 18/06/2024
#3. DESC.: Extract positive sequence from reference genome

import os

def get_pos_sequences(tf_data):
    base_path = r"C:\Users\jyott\Desktop\IITRcopy"
    valid_chromosomes = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10',
                         'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19',
                         'chr20', 'chr21', 'chr22', 'chrX', 'chrY', 'chrM']

    for transcription_factor, experiments in tf_data.items():
        
        for cell_line, experiment_accession in experiments:
            bed_files_path = os.path.join(base_path, transcription_factor, cell_line)
            
            for bed_file_name in os.listdir(bed_files_path):
                
                if bed_file_name.endswith('.bed'):
                    line_counter = 0
                    pos_filename = os.path.splitext(bed_file_name)[0] + '_pos'
                    pos_file_path = os.path.join(bed_files_path, pos_filename)
                    
                    with open(pos_file_path, 'a') as pos_file:
                        bed_file_path = os.path.join(bed_files_path, bed_file_name)
                        
                        with open(bed_file_path, 'r') as bed_file:
                            
                            for line in bed_file:
                                fields = line.strip().split('\t')
                                chromosome = fields[0]
                                start_position = int(fields[1])
                                end_position = int(fields[2])
                                
                                if chromosome in valid_chromosomes:
                                    genome_file_path = os.path.join(base_path, "hg38", chromosome + '.fa')
                                    
                                    with open(genome_file_path, 'r') as genome_file:
                                        next(genome_file)
                                        genome_sequence = genome_file.read().replace('\n', '')
                                        sequence = genome_sequence[start_position:end_position]
                                        sequence = sequence.upper()
                                        
                                        if len(sequence) >= 200:  # Only consider sequences with length >= 200
                                            start = (len(sequence) - 200) // 2
                                            sequence = sequence[start:start+200]
                                            
                                            pos_file.write(sequence + '\n')
                                            line_counter += 1
                                            
                                    if line_counter >= 6000:
                                        break
                            print("Positive sequence retrieved for", bed_file_name)

# Example usage:
#tf_data = download_bed_files()  # This is your function from the first part

#get_pos_sequences(tf_data)
