#AUTHOR: Jyot Thesia
#DATE: 21/6/2024
#9. DESC.: main file to call all other functions

# Import the functions from their respective files
from download_bed_files_copy import download_bed_files
from get_sequence_copy import get_pos_sequences
from sort_bed_file import sort_bed_files_in_directory
from update_coords import update_coordinates
from get_negatives import get_neg_sequences
from labelling import labelling
from merge_and_shuffle import merge_n_shuffle

def main():
    # Call the first function to download BED files and store the data
    tf_data = download_bed_files()
    
    # Call the second function to process the downloaded BED files and get sequences
    get_pos_sequences(tf_data)

    # Define your list of valid chromosomes
    valid_chromosomes = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10',
                     'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19',
                     'chr20', 'chr21', 'chr22', 'chrX', 'chrY', 'chrM']

    # Define the base path where your TF folders are located
    base_path = r"C:\Users\jyott\Desktop\IITRcopy"
    # Call the function with the base path and valid chromosomes
    sort_bed_files_in_directory(base_path, valid_chromosomes)

    base_path = r"C:\Users\jyott\Desktop\IITRcopy"
    update_coordinates(base_path)

    get_neg_sequences(tf_data)

    base_path = r'C:\\Users\\jyott\\Desktop\\IITRcopy'
    labelling(base_path)

    merge_n_shuffle(tf_data)


if __name__ == "__main__":
    main()
