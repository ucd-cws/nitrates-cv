"""
	Needs to be run somewhere that gdal is available on the command line. cloud_optimize library is from the main
	nitrates repository's scripts folder.
"""

import os
import shutil

import cloud_optimize

base_folder = os.path.split(os.path.abspath(__file__))[0]
cogt_folder = os.path.join(base_folder, "cogt")

tif_files = [os.path.join(base_folder, filename) for filename in os.listdir(base_folder) if filename.endswith(".tif")]

if os.path.exists(cogt_folder):
	shutil.rmtree(cogt_folder)
os.makedirs(cogt_folder)

for tif in tif_files:
	cloud_optimize.make_cloud_optimized(tif, os.path.join(cogt_folder, os.path.basename(tif)))

