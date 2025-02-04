#!/usr/bin/env python3
'''
fitsfields.py
History: 2024-02-12 original
    2025-02-03  Created standalone executable with new name fitsfields
Author: George Loyer

Accepts three user inputs:
  a list of space-delimited FITS header card names
     Examples: EXPTIME AIRMASS OBJECT FILTER DATE-OBS
  a list of space-delimited filenames that are wildcard expanded
  the output file name

A card name in a FITS file is a single record on a line.
Here I'm calling a card name a FITS header field.
After user input is read, list objects are created for the
fields and file names, and the output file is opened.
The fields are used as the text of the header line in the
output file, comma-delimited. Then the read_field_values()
function is executed once for each file and the file name and
fields are output to the output file, comma delimited.
When the program is complete, the output file is a CSV file
that can be read by Excel for additional review and analysis.
'''

import sys
import glob
from astropy.io import fits

def read_field_values(field_names, fits_filename):
    try:
        with fits.open(fits_filename) as hdul:
            values = [hdul[0].header.get(field, 'Not found') for field in field_names]
            return f"{', '.join(map(str, values))}"
    except Exception as e:
        print(f"Error reading {fits_filename}: {str(e)}")

def main():
    print(f"At the prompts, enter field names, file pattern, and output file.")
    print(f"Example field names: EXPTIME AIRMASS OBJECT FILTER DATE-OBS")
    field_names_input = input("Enter field names (space delimited): ")
    file_pattern = input("Enter file pattern (with wildcards): ")
    output_file = input("Enter output file name: ")

    field_names = field_names_input.split()

    fits_files = glob.glob(file_pattern)

    if len(field_names) == 0 or len(fits_files) == 0:
        print("Invalid input. Please provide at least one card name and match at least one FITS file.")
        sys.exit(1)

    # Print header line
    with open(output_file, 'w') as output_file_handle:
        output_file_handle.write("FILENAME, " + ", ".join(field_names) + "\n")

        for fits_file in fits_files:
            result = read_field_values(field_names, fits_file)
            output_file_handle.write(fits_file + ", " + result + "\n")

if __name__ == "__main__":
    main()

