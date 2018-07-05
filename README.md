# Nitrates-CV  

This project distributes the nitrates data for the Central Valley and Salinas. These layers were the final GNLM outputs created in Fall 2017. See http://ucd-cws.github.io/nitrates/ for more information and interactive maps.

## Accessing Data
Data in this repository are sorted into folders by modeled year, and withing
those folders, each variable is a separate GeoTIFF. ArcGIS-compatible
metadata is stored in "sidecar" files, associated with each separate raster.
Users of other GIS packages can open metadata as text for viewing (we tried
to make cross-platform metadata in geotiffs - unfortunately there isn't a good method).

Data can be accessed using a number of methods:
* Download of individual files by browsing in this interface
* Downloading a copy of this [entire repository](https://github.com/ucd-cws/nitrates-cv/archive/master.zip)
* Via GIS services available at https://atlas.cws.ucdavis.edu/arcgis/rest/services/Nitrates/
* As [Cloud-Optimized GeoTIFFs](https://www.cogeo.org) in compatible GIS packages (eg: QGIS) - individual rasters in this repository
can be used if you use the download links for each one. This can save you disk space while
still making data available for visualization and processing.

## Variables

| Variable                                                                                                  | Raster          |
|-----------------------------------------------------------------------------------------------------------|-----------------|
| Atmospheric Losses                                                                                        | NatmLosses      |
| Atmospheric Deposition                                                                                    | Ndeposition     |
| Synthetic Fertilizer                                                                                      | Nfertilizer     |
| Potential Groundwater Loading from All Sources                                                            | Ngw             |
| Potential Groundwater Loading from Crops and Natural Vegetation                                           | Ngw_nondirect   |
| Potential Groundwater Loading: Urban Areas, Golf Courses, Wastewater Lagoons, Corrals, and Alfalfa/Clover | NgwDirect       |
| Potential Harvest                                                                                         | Nharvest        |
| Actual Harvest                                                                                            | Nharvest_actual |
| Irrigation                                                                                                | Nirrigation     |
| Land-applied Manure, Effluent, or Biosolids                                                               | NlandApplied    |
| Manure Sale                                                                                               | NmanureSale     |
| Potential Synthetic Fertilizer                                                                            | Nnorm           |
| Actual Runoff                                                                                             | Nrunoff_actual  |
| Potential Groundwater Loading from Septic Systems                                                         | Nseptic         |


# Citations
Reports for all data can be found at http://groundwaternitrate.ucdavis.edu

Salinas data is from the original report and can be cited as:

Harter, T., J. R. Lund, J. Darby, G. E. Fogg, R. Howitt, K. K. Jessoe, G. S. Pettygrove, J.
 F. Quinn, J. H. Viers, D. B. Boyle, H. E. Canada, N. DeLaMora, K. N. Dzurella, A. Fryjoff-Hung,
 A. D. Hollander, K. L. Honeycutt, M. W. Jenkins, V. B. Jensen, A. M. King, G. Kourakos, D.
 Liptzin, E. M. Lopez, M. M. Mayzelle, A. McNally, J. Medellin-Azuara, and T. S. Rosenstock. 2012.
 Addressing Nitrate in California's Drinking Water with a Focus on Tulare Lake Basin and Salinas
 Valley Groundwater. Report for the State Water Resources Control Board Report to the Legislature.
 Center for Watershed Sciences, University of California, Davis. 78 p. http://groundwaternitrate.ucdavis.edu.


Central Valley data is from the more recent FREP report and can be cited as:

Harter, T., K. Dzurella, G. Kourakos, A. Hollander, A. Bell, N. Santos, Q. Hart, A.King, J. Quinn,
 G. Lampinen, D. Liptzin, T. Rosenstock, M. Zhang, G.S. Pettygrove, and T. Tomich, 2017. Nitrogen
 Fertilizer Loading to Groundwater in the Central Valley. Final Report to the Fertilizer Research
 Education Program, Projects 11-0301 and 15-0454, California Department of Food and Agriculture and
 University of California Davis, 333p., http://groundwaternitrate.ucdavis.edu.

# Processing
For processing, combination and metadata were set with arcpy and arcpy_metadata
using scripts available in https://github.com/ucd-cws/nitrates. Where possible,
data were translated into cloud-optimized GeoTIFFs for export
using GDAL 2.2 via Bash on Ubuntu on Windows 10