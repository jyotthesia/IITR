#AUTHOR: Jyot Thesia
#DATE: 20/6/2024
#8. DESC.: Merge positive and negative files and shuffle the order of rows

import os
import random

def merge_n_shuffle(tf_data):
    base_path = r"C:\Users\jyott\Desktop\IITRcopy"
    
    for transcription_factor, experiments in tf_data.items():
        for cell_line, experiment_accession in experiments:
            files_path = os.path.join(base_path, transcription_factor, cell_line)
            
            # Initialize empty lists for _neg and _pos files
            neg_files = []
            pos_files = []
            
            for file_name in os.listdir(files_path):
                if file_name.endswith('_neg'):
                    neg_files.append(file_name)
                elif file_name.endswith('_pos'):
                    pos_files.append(file_name)

            # Merge the files (e.g., concatenate them)
            merged_file = os.path.join(files_path, f"{cell_line}_merged.txt")
            with open(merged_file, 'w') as merged:
                for neg_file, pos_file in zip(neg_files, pos_files):
                    with open(os.path.join(files_path, neg_file)) as neg:
                        merged.write(neg.read())
                    with open(os.path.join(files_path, pos_file)) as pos:
                        merged.write(pos.read())

            # Shuffle the rows randomly
            with open(merged_file, 'r') as merged:
                lines = merged.readlines()
                random.shuffle(lines)
            with open(merged_file, 'w') as merged:
                merged.writelines(lines)

            print(f"Merged and shuffled files for {cell_line} into {merged_file}")

#tf_data = {
    #'NANOG': [('GM23338', 'ENCSR061DGF'), ('H1', 'ENCSR000BMT')],
    #'KLF4': [('MCF-7', 'ENCSR265WJC')],
    #'SOX6': [('K562', 'ENCSR788RSW'), ('HepG2', 'ENCSR766TSU')],
    #'POU5F1': [('H1', 'ENCSR000BMU'), ('GM23338', 'ENCSR264RJX'), ('K562', 'ENCSR364SNE')]
#}
#merge_n_shuffle(tf_data)
