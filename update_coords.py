#AUTHOR: Jyot Thesia
#DATE: 19/06/2024
#5. DESC.: Get a new bed file with updated coordinates for negative sequences

import os

def update_coordinates(base_path):
    # Walk through the directory
    for root, dirs, files in os.walk(base_path):
        for file in files:
            # Check if the file is a sorted BED file
            if file.endswith('_sorted.bed'):
                sorted_file_path = os.path.join(root, file)
                negcoords_file_path = sorted_file_path.replace('_sorted.bed', '_negcoords.bed')

                with open(sorted_file_path, 'r') as sorted_bed, open(negcoords_file_path, 'w') as negcoords_bed:
                    sorted_lines = sorted_bed.readlines()
                    for i in range(len(sorted_lines)-1):
                        current_line = sorted_lines[i].strip().split('\t')
                        next_line = sorted_lines[i+1].strip().split('\t')
                        
                        # Calculate midpoint and updated coordinates if the condition is met
                        if int(next_line[1]) - int(current_line[2]) > 6000:
                            midpoint = (int(current_line[2]) + int(next_line[1])) // 2
                            updated_start = midpoint - 100
                            updated_end = midpoint + 100

                            # Write the new coordinates to the negcoords file
                            negcoords_bed.write(f"{current_line[0]}\t{updated_start}\t{updated_end}\n")

                print("Coordinates updated for", file)

# Example usage:
# base_path = r"C:\Users\jyott\Desktop\IITR"
# update_coordinates(base_path)
