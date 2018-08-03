"""
	Author: Nick Santos (@nickrsan)
	Date: 8/3/2018
	Creates cloud-optimized GeoTIFFs for use in GDAL, QGIS, etc.
	Copied from the main `nitrates` repository since it is primarily used to create these data.
	
	Designed to be run with a functioning GDAL installation - this works well in the Windows Subsystem for Linux (WSL),
	also known as Ubuntu on Bash on Windows (UoBoW), which is where this was initially run.
"""

import os
import subprocess
import tempfile
import logging
import shutil

log = logging.getLogger("gdal_cloud_optimizer")

if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG)

def make_cloud_optimized(input_raster, output_raster, copy_metadata=True, compress="LZW", overview_type="average", additional_gdal_params=()):
	"""
		:param overview_type: defaults to averaging values, but for categorical values, provide "nearest" - other options described here: https://www.gdal.org/gdaladdo.html
	"""
	
	log.debug("Making main image for {}".format(input_raster))
	intermediate_dataset = tempfile.mktemp(prefix="cloud_optimized", suffix=".tif")

	main_call = ["gdal_translate", input_raster, intermediate_dataset, "-co", "TILED=YES", "-co",
						   "COMPRESS={}".format(compress)]

	if len(additional_gdal_params) > 0:
		main_call += additional_gdal_params

	subprocess.check_call(main_call)

	try:
		log.debug("    Adding overviews")
		subprocess.check_call(["gdaladdo", "-r", overview_type, intermediate_dataset, "2", "4", "8", "16", "32"])

		log.debug("    Making cloud-optimized")
		subprocess.check_call(["gdal_translate", intermediate_dataset, output_raster, "-co",
							   "TILED=YES", "-co", "COMPRESS=LZW", "-co", "COPY_SRC_OVERVIEWS=YES"])

		metadata_input = "{}.xml".format(input_raster)  # add .xml for metadata (not replace)
		if copy_metadata and os.path.exists(metadata_input):
			metadata_output = "{}.xml".format(output_raster)
			shutil.copyfile(metadata_input, metadata_output)  # copy metadata file
	finally:
		os.remove(intermediate_dataset)  # clean up after ourselves