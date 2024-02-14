#!/usr/bin/env python3

# card-values.py
# History: 2024-02-12 original
# Author: George Loyer
#
# accepts three user inputs:
#   a list of space-delimited FITS header card names
#   a list of space-delimited filenames that are wildcard expanded
#   the output file name
#
# After user input is read in main(), lists are created for the
# card names and file names, and the output file is opened.
# The card names are used as the text of the header line in the
# output file, comma-delimited. Then the read_card_values()
# function is executed once for each file and the card values
# are output to the output file, comma delimited. When the
# program is complete, the output file is a CSV file that can
# be read by Excel for additional review and analysis.

import sys
import glob
from astropy.io import fits

def read_card_values(card_names, fits_filename):
    try:
        with fits.open(fits_filename) as hdul:
            values = [hdul[0].header.get(card, 'Not found') for card in card_names]
            return f"{', '.join(map(str, values))}"
    except Exception as e:
        print(f"Error reading {fits_filename}: {str(e)}")

def main():
    card_names_input = input("Enter card names (space delimited): ")
    file_pattern = input("Enter file pattern (with wildcards): ")
    output_file = input("Enter output file name: ")

    card_names = card_names_input.split()

    fits_files = glob.glob(file_pattern)

    if len(card_names) == 0 or len(fits_files) == 0:
        print("Invalid input. Please provide at least one card name and match at least one FITS file.")
        sys.exit(1)

    # Print header line
    with open(output_file, 'w') as output_file_handle:
        output_file_handle.write(", ".join(card_names) + "\n")

        for fits_file in fits_files:
            result = read_card_values(card_names, fits_file)
            output_file_handle.write(result + "\n")

if __name__ == "__main__":
    main()

