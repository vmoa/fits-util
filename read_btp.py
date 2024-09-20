#!/usr/bin/env python3
'''
read_btp.py
history: 2/12/2024
author: george loyer
description: opens a FITS file, reads the BTP card,
prints the BTP value.
'''
import sys
from astropy.io import fits

def read_btp_card(fits_filename):
    try:
        with fits.open(fits_filename) as hdul:
            btp_value = hdul[0].header.get('BTP', 'Not found')
            print(f"BTP value in {fits_filename}: {btp_value}")
    except Exception as e:
        print(f"Error reading {fits_filename}: {str(e)}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 read_btp.py fits_file1.fits fits_file2.fits ...")
        sys.exit(1)

    fits_files = sys.argv[1:]

    for fits_file in fits_files:
        read_btp_card(fits_file)

if __name__ == "__main__":
    main()

