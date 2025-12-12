#!/usr/bin/env python3
'''
extract_photometry.py
History: 2024-02-12 original
    2025-02-03  Created standalone executable with new name fitsfields
Author: George Loyer
'''

from astropy.io import fits
import argparse

def extract_photometry_data(fits_file):
    # Open the FITS file (automatically handles .fz compressed files)
    with fits.open(fits_file) as hdul:
        header = hdul[0].header  # Primary header

        # Extract relevant photometry data
        photometry_data = {
            "Object": header.get("OBJECT", "Unknown"),
            "RA": header.get("RA", "Unknown"),
            "DEC": header.get("DEC", "Unknown"),
            "Airmass": header.get("AIRMASS", "Unknown"),
            "Exposure Time (s)": header.get("EXPTIME", "Unknown"),
            "Filter": header.get("FILTER", "Unknown"),
            "Zero Point (MAGZERO)": header.get("MAGZERO", "Unknown"),
            "Zero Point Error (PHOTZPER)": header.get("PHOTZPER", "Unknown"),
            "Instrumental Magnitude": header.get("MAGINST", "Unknown"),
            "Magnitude Error": header.get("MAGERR", "Unknown"),
            "Sky Brightness": header.get("SKYVAL", "Unknown"),
            "Seeing": header.get("SEEING", "Unknown"),
            "Telescope": header.get("TELESCOP", "Unknown"),
            "Instrument": header.get("INSTRUME", "Unknown"),
        }

    # Print the extracted photometry information
    print("\nPhotometry Data from FITS Header:")
    for key, value in photometry_data.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract photometry data from LCO FITS files.")
    parser.add_argument("fits_file", help="Path to the FITS (.fz) file")
    args = parser.parse_args()

    extract_photometry_data(args.fits_file)

