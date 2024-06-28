#AUTHOR: Jyot Thesia
#DATE: 20/6/2024
#7. DESC.: Labelling positive and negative sequences

import os

def append_value_to_rows_inplace(input_file, value):
    try:
        with open(input_file, 'r+') as file:
            lines = file.readlines()
            file.seek(0)  # Move the file pointer to the beginning
            for line in lines:
                # Remove any trailing whitespace and split the line by tabs
                parts = line.strip().split('\t')
                # Append the desired value to the end of the line
                modified_line = '\t'.join(parts) + '\t' + value + '\n'
                # Write the modified line back to the file
                file.write(modified_line)
            file.truncate()  # Remove any remaining content beyond the modified lines
        print(f"Successfully appended '{value}' to rows in {input_file}.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")

def labelling(base_path):
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('_pos'):
                input_file = os.path.join(root, file)
                append_value_to_rows_inplace(input_file, '1')
            elif file.endswith('_neg'):
                input_file = os.path.join(root, file)
                append_value_to_rows_inplace(input_file, '0')

# Example usage:
#base_path = r'C:\\Users\\jyott\\Desktop\\IITR'
#labelling(base_path)
