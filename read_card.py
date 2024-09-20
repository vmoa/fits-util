#!/usr/bin/env python3
'''
read_card.py
Opens the FITS file, takes card_name and a list of FITS files as
the arguments to the script, prints the card name and card value
for all of the files in the file list.
'''

import sys
from astropy.io import fits

def read_card_value(card_name, fits_filename):
    try:
        with fits.open(fits_filename) as hdul:
            card_value = hdul[0].header.get(card_name, 'Not found')
            print(f"{card_name} value in {fits_filename}: {card_value}")
    except Exception as e:
        print(f"Error reading {fits_filename}: {str(e)}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 read_card.py card_name fits_file1.fits fits_file2.fits ...")
        sys.exit(1)

    card_name = sys.argv[1]
    fits_files = sys.argv[2:]

    for fits_file in fits_files:
        read_card_value(card_name, fits_file)

if __name__ == "__main__":
    main()

