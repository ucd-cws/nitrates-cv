import os
import shutil

import arcpy

base_folder = os.path.split(os.path.abspath(__file__))[0]
prj_file = os.path.join(base_folder, "array_projection_information.prj")
metadata_file = os.path.join(base_folder, "Metadata_for_Nitrate_Model_Data_Release.xml")
processing_folder = os.path.join(base_folder, "processing")

txt_files = [os.path.join(base_folder, filename) for filename in os.listdir(base_folder) if filename.endswith(".asc")]

arcpy.env.overwriteOutput = True

def make_new_name(full_path, extension):
	return os.path.join(base_folder, "{}.{}".format(os.path.basename(full_path)[:-4], extension))


for filename in txt_files:
	print(filename)
	new_name = make_new_name(filename, "asc")
	os.rename(filename, new_name)  # rename txt to asc

	new_prj = make_new_name(filename, "prj")
	if not os.path.exists(new_prj):
		shutil.copyfile(prj_file, new_prj)

	new_xml = "{}.xml".format(make_new_name(filename, "tif"))
	if os.path.exists(new_xml):  # delete the existing metadata file, copy the main one
		os.remove(new_xml)
	shutil.copyfile(metadata_file, new_xml)

	new_tif = make_new_name(filename, "tif")

	try:
		arcpy.ASCIIToRaster_conversion(new_name, new_tif, "Float")
	except:
		print("Failed to make TIF for {}".format(filename))
		continue

	arcpy.DefineProjection_management(new_tif, coor_system=new_prj)


asc_files = [os.path.join(base_folder, filename) for filename in os.listdir(base_folder) if filename.endswith(".asc")]
for asc in asc_files:
	tif_file = make_new_name(asc, "tif")
	try:
		assert(os.path.exists(tif_file))  # make sure that for every asc file there's a tif now
	except AssertionError:
		print("{} has no matching tif".format(asc))

