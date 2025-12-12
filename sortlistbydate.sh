#!/bin/bash
#
(head -n 1 fieldlist && tail -n +2 fieldlist | sort -t, -k6,6) > sorted_fieldlist
