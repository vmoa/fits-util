#!/bin/bash
# upandout.sh
# uploads all of the fits files in this folder to astrometry.net
# and outputs a set of sequentially numbered files to a new folder
# with the seed of the new files as the folder name
#

# Check if a seed name is provided as an argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <seedname>"
    exit 1
fi

seed_name=$1
output_folder="${seed_name}"

# Create the output folder if it doesn't exist
mkdir -p "$output_folder"

# Counter for the three-character leading zero sequence number
counter=1

# Loop through all .fits files in the current folder
for fits_file in *.fits; do
    # Generate the new filename with the seed name and sequence number
    new_filename="${seed_name}$(printf "%03d" "$counter").fits"
    
    # Upload the file using client.py
    client.py --apikey="cjescejoayzhyrxd" --upload="$fits_file" --newfits="$new_filename"

    # Copy the new file to the output folder
    mv "$new_filename" "$output_folder/"

    # Increment the counter for the next file
    ((counter++))
    echo "$fits_file"+" "+"$new_filename"
done


