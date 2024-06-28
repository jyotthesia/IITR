#AUTHOR: Jyot Thesia
#DATE: 19/06/2024
#4. DESC.: Sort bed files, first according to chr no. and then according to starting coordinates

import os

def sort_bed_files_in_directory(tf_folder_path, valid_chromosomes):
    for tf_name in os.listdir(tf_folder_path):
        tf_path = os.path.join(tf_folder_path, tf_name)
        if os.path.isdir(tf_path):
            for cell_line in os.listdir(tf_path):
                cell_line_path = os.path.join(tf_path, cell_line)
                if os.path.isdir(cell_line_path):
                    for bed_file in os.listdir(cell_line_path):
                        if bed_file.endswith('.bed'):
                            bed_file_path = os.path.join(cell_line_path, bed_file)
                            #print(f"Attempting to sort BED file: {bed_file_path}")  # Debugging print statement
                            sort_bed_file(bed_file_path, valid_chromosomes)



def sort_bed_file(bed_file_path, valid_chromosomes):
    #print(f"Trying to open: {bed_file_path}")  # Debugging print statement

    # Read the BED file
    with open(bed_file_path, 'r') as bed_file:
        lines = bed_file.readlines()

    # Filter and sort the lines
    filtered_sorted_lines = sorted(
        (line for line in lines if line.split('\t')[0] in valid_chromosomes),
        key=lambda line: (valid_chromosomes.index(line.split('\t')[0]), int(line.split('\t')[1]))
    )

    # Write to a new file
    sorted_file_path = bed_file_path.replace('.bed', '_sorted.bed')
    with open(sorted_file_path, 'w') as sorted_bed_file:
        for line in filtered_sorted_lines:
            sorted_bed_file.write(line)
    print( bed_file, "was sorted" )
# Example usage:
#base_path = r"C:\Users\jyott\Desktop\IITR"
#valid_chromosomes = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10', 
                     #'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 
                     #'chr20', 'chr21', 'chr22', 'chrX', 'chrY', 'chrM']
#sort_bed_files_in_directory(base_path, valid_chromosomes)
