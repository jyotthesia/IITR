#AUTHOR: Jyot Thesia
#DATE: 18/06/2024
#2. DESC.: Download bed files for entered TFs and unzip them

import requests
import os
import gzip
import shutil

def download_bed_files():
    tf_dict = {}
    n = int(input("Enter the number of TF:"))
    for i in range(n):
        tf_name = input("Enter the name of TF:")
        tf_dict[tf_name] = []

    for transcription_factor in tf_dict.keys():
        url = f"https://www.encodeproject.org/search/?type=Experiment&replicates.library.biosample.donor.organism.scientific_name=Homo+sapiens&assay_title=TF+ChIP-seq&status=released&target.label={transcription_factor}&biosample_ontology.classification=cell+line&format=json"
        response = requests.get(url)
        data = response.json()

        tf_directory = os.path.join(r"C:\Users\jyott\Desktop\IITR", transcription_factor)
        os.makedirs(tf_directory, exist_ok=True)

        cell_lines = list(set([experiment['biosample_ontology']['term_name'] for experiment in data["@graph"]]))

        for cell_line in cell_lines:
            cell_line_directory = os.path.join(tf_directory, cell_line)
            os.makedirs(cell_line_directory, exist_ok=True)

            experiment_accession = next((experiment['accession'] for experiment in data["@graph"] if experiment['biosample_ontology']['term_name'] == cell_line), None)

            if experiment_accession is not None:
                tf_dict[transcription_factor].append((cell_line, experiment_accession))
                # ... rest of your code to download and process files ...
                # ENCODE REST API URL for the experiment
                experiment_url = f"https://www.encodeproject.org/experiments/{experiment_accession}/?format=json"

                # Send a GET request to the ENCODE REST API
                experiment_response = requests.get(experiment_url)
                experiment_data = experiment_response.json()

                # Loop through the files in the experiment
                for file in experiment_data["files"]:
                    # Check if 'file_format' key exists in file and if file format is 'bed'
                    if 'file_format' in file and file["file_format"] == "bed" and file["file_format_type"] == "idr_ranked_peak":
                        # Get download URL for file
                        download_url = f"https://www.encodeproject.org{file['href']}"

                        # Download file
                        file_response = requests.get(download_url)

                        # Get filename from accession name of file
                        filename = os.path.join(cell_line_directory, experiment_accession + ".gz")

                        # Write content to file
                        with open(filename, "wb") as f:
                            f.write(file_response.content)

                        print(f"Downloaded {filename}")

                        # Decompress gzip file
                        decompressed_filename = filename[:-3] + ".bed"  # remove '.gz' from filename and add '.bed'
                        with gzip.open(filename, 'rb') as f_in:
                            with open(decompressed_filename, 'wb') as f_out:
                                shutil.copyfileobj(f_in, f_out)

                        #print(f"Decompressed {filename} to {decompressed_filename}")

                        # Delete original gzip file
                        os.remove(filename)

                        #print(f"Deleted {filename}")

                        
                        # Stop after downloading the first file for the cell line
                        break

    return tf_dict

# Example usage:
#tf_data = download_bed_files()
#print(tf_data)
