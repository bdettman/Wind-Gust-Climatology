#!/usr/bin/env python
# coding: utf-8

# This script combines similar csv files together through the concatenate function.
# Used to combine individual files and create groups/zones.

# Coded by: Brennan Dettmann
# Date: 7/5/2020

# imports all of the necessary modules

import os
import glob
import pandas as pd

path = "/home/user/data/"

all_files = glob.glob(os.path.join(path, "data_*.csv"))

df_merged = (pd.read_csv(f, sep=',') for f in all_files)
df_merged   = pd.concat(df_from_each_file, ignore_index=True)
df_merged.to_csv( "merged.csv")

