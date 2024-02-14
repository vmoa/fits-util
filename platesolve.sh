#!/bin/bash
'''
platesolve.sh
Uploads all of the fits files in this folder to astrometry.net
and outputs a set of sequentially numbered files to a new folder
with the seed of the new files as the folder name

The upload and monitoring is handled by a python scrip, client.py,
that is provided by a git repository maintained by astrometry.net.
The client.py program contains an API key that individual users should 
change to their own key before using this code. The key in this repository
is broken and will not work.

The platesolve.sh and client.py program files should be made 
executable and stored in the path. I recommend /usr/local/bin.

The recommended usage is to run this in the background, especially
for folders with more than a dozen or so files to platesolve.

> platesolve.sh wcs > log.file 2>&1 &

where 'wcs' is the seedname for the platesolved files in a folder named
'wcs', and log.file is where you can see the output of the program as it
goes through the process of doing platesolves at astrometry.net. This is
especially useful when a platesolve fails to identify which file is having
the problem.
'''

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
    #  fails for folders with more than 999 files
    new_filename="${seed_name}$(printf "%03d" "$counter").fits"
    
    # Upload the file using client.py
    client.py --apikey="cxescxjoayzxyrxd" --upload="$fits_file" --newfits="$new_filename"

    # Copy the new file to the output folder
    mv "$new_filename" "$output_folder/"

    # Increment the counter for the next file
    ((counter++))
    echo "$fits_file"+" "+"$new_filename"
done


