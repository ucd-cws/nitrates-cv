# CAML Land Cover Data

California Augmented Multisource Landcover (CAML) layer. Created as part of the 2017 FREP Report, available at http://groundwaternitrate.ucdavis.edu/files/268749.pdf - Chapter 2 describes the 1990 and 2005 CAML layers. Chapter 10.5 describes the methods used in backcasting for the 1975, 1960, and 1945 layers. 

Data are provided as GeoTIFFs. Files in the `cogt` folder are Cloud-Optimized GeoTIFFs, usable directly at the URL from software such as QGIS.

Classification is as follows - Raster value applies to data in this folder, while the grouped values apply to the maps in the online viewer

| Land Cover Type                                                                    | Raster Value  |  Grouped Classification                        |  Grouped Value | 
|------------------------------------------------------------------------------------|---------------|------------------------------------------------|----------------| 
| No data                                                                            | 0             | No data                                        | 0              | 
| Urban (backcasted)                                                                 | 1             | Urban                                          | 1              | 
| Natural Vegetation (backcasted)                                                    | 2             | Native Vegetation                              | 2              | 
| Annual Grassland                                                                   | 3             | Pasture                                        | 3              | 
| Alkali Desert Scrub                                                                | 4             | Native Vegetation                              | 2              | 
| Aspen                                                                              | 5             | Native Vegetation                              | 2              | 
| Barren                                                                             | 6             | Barren                                         | 4              | 
| Bitterbrush                                                                        | 7             | Native Vegetation                              | 2              | 
| Blue Oak-Foothill Pine                                                             | 8             | Native Vegetation                              | 2              | 
| Blue Oak Woodland                                                                  | 9             | Native Vegetation                              | 2              | 
| Coastal Oak Woodland                                                               | 10            | Native Vegetation                              | 2              | 
| Closed-Cone Pine-Cypress                                                           | 11            | Native Vegetation                              | 2              | 
| Chamise-Redshank Chaparral                                                         | 12            | Native Vegetation                              | 2              | 
| Coastal Scrub                                                                      | 13            | Native Vegetation                              | 2              | 
| Douglas-Fir                                                                        | 14            | Native Vegetation                              | 2              | 
| Desert Riparian                                                                    | 15            | Native Vegetation                              | 2              | 
| Desert Scrub                                                                       | 17            | Native Vegetation                              | 2              | 
| Desert Succulent Shrub                                                             | 18            | Native Vegetation                              | 2              | 
| Desert Wash                                                                        | 19            | Water                                          | 5              | 
| Eastside Pine                                                                      | 20            | Native Vegetation                              | 2              | 
| Estuarine                                                                          | 21            | Water                                          | 5              | 
| Freshwater Emergent Wetland                                                        | 22            | Native Vegetation                              | 2              | 
| Jeffrey Pine                                                                       | 24            | Native Vegetation                              | 2              | 
| Joshua Tree                                                                        | 25            | Native Vegetation                              | 2              | 
| Juniper                                                                            | 26            | Native Vegetation                              | 2              | 
| Klamath Mixed Conifer                                                              | 27            | Native Vegetation                              | 2              | 
| Lacustrine                                                                         | 28            | Water                                          | 5              | 
| Lodgepole Pine                                                                     | 29            | Native Vegetation                              | 2              | 
| Low Sage                                                                           | 30            | Native Vegetation                              | 2              | 
| Marine                                                                             | 31            | Water                                          | 5              | 
| Mixed Chaparral                                                                    | 32            | Native Vegetation                              | 2              | 
| Montane Chaparral                                                                  | 34            | Native Vegetation                              | 2              | 
| Montane Hardwood-Conifer                                                           | 35            | Native Vegetation                              | 2              | 
| Montane Hardwood                                                                   | 36            | Native Vegetation                              | 2              | 
| Montane Riparian                                                                   | 37            | Native Vegetation                              | 2              | 
| Perennial Grassland                                                                | 39            | Pasture                                        | 3              | 
| Pinyon-Juniper                                                                     | 40            | Native Vegetation                              | 2              | 
| Palm Oasis                                                                         | 41            | Native Vegetation                              | 2              | 
| Ponderosa Pine                                                                     | 42            | Native Vegetation                              | 2              | 
| Riverine                                                                           | 43            | Water                                          | 5              | 
| Redwood                                                                            | 44            | Native Vegetation                              | 2              | 
| Red Fir                                                                            | 45            | Native Vegetation                              | 2              | 
| Subalpine Conifer                                                                  | 48            | Native Vegetation                              | 2              | 
| Saline Emergent Wetland                                                            | 49            | Native Vegetation                              | 2              | 
| Sagebrush                                                                          | 50            | Native Vegetation                              | 2              | 
| Sierran Mixed Conifer                                                              | 51            | Native Vegetation                              | 2              | 
| Urban                                                                              | 53            | Urban                                          | 1              | 
| Valley Oak Woodland                                                                | 55            | Native Vegetation                              | 2              | 
| Valley Foothill Riparian                                                           | 56            | Native Vegetation                              | 2              | 
| Water                                                                              | 57            | Water                                          | 5              | 
| White Fir                                                                          | 58            | Native Vegetation                              | 2              | 
| Wet Meadow                                                                         | 59            | Native Vegetation                              | 2              | 
| Undetermined Shrub Type                                                            | 62            | Native Vegetation                              | 2              | 
| Undetermined Conifer Type                                                          | 63            | Native Vegetation                              | 2              | 
| Non-Irrigated Pasture                                                              | 72            | Pasture                                        | 3              | 
| Eucalyptus                                                                         | 77            | Native Vegetation                              | 2              | 
| Citrus and Subtropical (Also Miscellaneous subtropical and jojoba)                 | 300           | Citrus and Subtropical                         | 6              | 
| Grapefruit                                                                         | 301           | Citrus and Subtropical                         | 6              | 
| Lemons                                                                             | 302           | Citrus and Subtropical                         | 6              | 
| Oranges                                                                            | 303           | Citrus and Subtropical                         | 6              | 
| Dates                                                                              | 304           | Citrus and Subtropical                         | 6              | 
| Avocados                                                                           | 305           | Citrus and Subtropical                         | 6              | 
| Olives                                                                             | 306           | Citrus and Subtropical                         | 6              | 
| Kiwis                                                                              | 308           | Citrus and Subtropical                         | 6              | 
| Eucalyptus                                                                         | 310           | Native Vegetation                              | 2              | 
| Deciduous Fruits and Nuts                                                          | 400           | Decidious Fruits and Nuts                      | 7              | 
| Mixed deciduous (Apples)                                                           | 401           | Decidious Fruits and Nuts                      | 7              | 
| Apricots                                                                           | 402           | Decidious Fruits and Nuts                      | 7              | 
| Cherries                                                                           | 403           | Decidious Fruits and Nuts                      | 7              | 
| Peaches and Nectarines                                                             | 405           | Decidious Fruits and Nuts                      | 7              | 
| Pears                                                                              | 406           | Decidious Fruits and Nuts                      | 7              | 
| Plums                                                                              | 407           | Decidious Fruits and Nuts                      | 7              | 
| Prunes                                                                             | 408           | Decidious Fruits and Nuts                      | 7              | 
| Figs                                                                               | 409           | Decidious Fruits and Nuts                      | 7              | 
| Almonds                                                                            | 412           | Decidious Fruits and Nuts                      | 7              | 
| Walnuts                                                                            | 413           | Decidious Fruits and Nuts                      | 7              | 
| Pistachios                                                                         | 414           | Decidious Fruits and Nuts                      | 7              | 
| No Access                                                                          | 500           | No data                                        | 0              | 
| "Field Crops (includes Flax, Hops, Castor Beans, Miscellaneous Field, and Millet)" | 600           | Field Crops                                    | 8              | 
| Cotton                                                                             | 601           | Field Crops                                    | 8              | 
| Safflower                                                                          | 602           | Field Crops                                    | 8              | 
| Sugar Beets                                                                        | 605           | Field Crops                                    | 8              | 
| Corn (Field and Sweet)                                                             | 606           | "Corn, Sorghum, Sudan"                         | 9              | 
| Grain sorghum                                                                      | 607           | "Corn, Sorghum, Sudan"                         | 9              | 
| Sudan                                                                              | 608           | "Corn, Sorghum, Sudan"                         | 9              | 
| Beans (dry)                                                                        | 610           | Field Crops                                    | 8              | 
| Sunflowers                                                                         | 612           | Field Crops                                    | 8              | 
| Grain and Hay (includes miscellaneous)                                             | 700           | Grain                                          | 10             | 
| Barley                                                                             | 701           | Grain                                          | 10             | 
| Wheat                                                                              | 702           | Grain                                          | 10             | 
| Oats                                                                               | 703           | Grain                                          | 10             | 
| Idle – Cropped Past 3 Years                                                        | 901           | Barren                                         | 4              | 
| Idle – New Lands                                                                   | 902           | Barren                                         | 4              | 
| Barren and Wasteland                                                               | 1410          | Barren                                         | 4              | 
| Dry stream channels                                                                | 1411          | Barren                                         | 4              | 
| Mine Tailings                                                                      | 1412          | Barren                                         | 4              | 
| Barren Land                                                                        | 1413          | Barren                                         | 4              | 
| Salt Flats                                                                         | 1414          | Barren                                         | 4              | 
| Sand dunes                                                                         | 1415          | Barren                                         | 4              | 
| Native Vegetation (unsegregated)                                                   | 1420          | Native Vegetation                              | 2              | 
| Riparian Vegetation                                                                | 1430          | Native Vegetation                              | 2              | 
| Riparian Marsh                                                                     | 1431          | Native Vegetation                              | 2              | 
| Riparian Meadow                                                                    | 1432          | Native Vegetation                              | 2              | 
| Riparian Tree                                                                      | 1433          | Native Vegetation                              | 2              | 
| Riparian seasonal duck marsh                                                       | 1434          | Native Vegetation                              | 2              | 
| Riparian permanent duck marsh                                                      | 1435          | Native Vegetation                              | 2              | 
| Not surveyed                                                                       | 1440          | No data                                        | 0              | 
| Native Vegetation                                                                  | 1450          | Native Vegetation                              | 2              | 
| Grassland                                                                          | 1451          | Pasture                                        | 3              | 
| Light Brush                                                                        | 1452          | Native Vegetation                              | 2              | 
| Medium Brush                                                                       | 1453          | Native Vegetation                              | 2              | 
| Heavy Brush                                                                        | 1454          | Native Vegetation                              | 2              | 
| Brush and Timber                                                                   | 1455          | Native Vegetation                              | 2              | 
| Forest                                                                             | 1456          | Native Vegetation                              | 2              | 
| Oak grassland                                                                      | 1457          | Pasture                                        | 3              | 
| Water Surface                                                                      | 1460          | Water                                          | 5              | 
| River                                                                              | 1461          | Water                                          | 5              | 
| Water channel                                                                      | 1462          | Water                                          | 5              | 
| "Freshwater lake, reservoir"                                                       | 1464          | Water                                          | 5              | 
| Brackish water                                                                     | 1465          | Water                                          | 5              | 
| Pasture                                                                            | 1600          | Pasture                                        | 3              | 
| Alfalfa                                                                            | 1601          | Alfalfa                                        | 11             | 
| Clover                                                                             | 1602          | Alfalfa                                        | 11             | 
| Mixed pasture                                                                      | 1603          | Pasture                                        | 3              | 
| Native Pasture                                                                     | 1604          | Pasture                                        | 3              | 
| Induced high water table native pasture                                            | 1605          | Pasture                                        | 3              | 
| Miscellaneous grasses                                                              | 1606          | Pasture                                        | 3              | 
| Turf farms                                                                         | 1607          | Pasture                                        | 3              | 
| Rice (includes rice & wild rice subclasses)                                        | 1800          | Rice                                           | 14             | 
| Farmstead (with residence)                                                         | 1901          | Semiagricultural and Incidental to Agriculture | 12             | 
| Livestock feedlot operation                                                        | 1902          | Semiagricultural and Incidental to Agriculture | 12             | 
| Dairy farm                                                                         | 1903          | Semiagricultural and Incidental to Agriculture | 12             | 
| Poultry farm                                                                       | 1904          | Semiagricultural and Incidental to Agriculture | 12             | 
| Farmstead (without residence)                                                      | 1905          | Semiagricultural and Incidental to Agriculture | 12             | 
| "Truck,Nursery, Berry Crops (includes cole mix, mixed, and misc. truck crops)"     | 2000          | "Truck, Nursery, and Berry Crops"              | 13             | 
| Artichokes                                                                         | 2001          | "Truck, Nursery, and Berry Crops"              | 13             | 
| Asparagus                                                                          | 2002          | "Truck, Nursery, and Berry Crops"              | 13             | 
| Beans (green)                                                                      | 2003          | "Truck, Nursery, and Berry Crops"              | 13             | 
| Carrots                                                                            | 2006          | "Truck, Nursery, and Berry Crops"              | 13             | 
| Celery                                                                             | 2007          | "Truck, Nursery, and Berry Crops"              | 13             | 
| Lettuce                                                                            | 2008          | "Truck, Nursery, and Berry Crops"              | 13             | 
| "Melons, squash, cucumbers"                                                        | 2009          | "Truck, Nursery, and Berry Crops"              | 13             | 
| Onions and garlic                                                                  | 2010          | "Truck, Nursery, and Berry Crops"              | 13             | 
| Peas                                                                               | 2011          | "Truck, Nursery, and Berry Crops"              | 13             | 
| Potatoes                                                                           | 2012          | "Truck, Nursery, and Berry Crops"              | 13             | 
| Sweet Potatoes                                                                     | 2013          | "Truck, Nursery, and Berry Crops"              | 13             | 
| Spinach                                                                            | 2014          | "Truck, Nursery, and Berry Crops"              | 13             | 
| Tomatoes (processing)                                                              | 2015          | "Truck, Nursery, and Berry Crops"              | 13             | 
| "Flowers, nursery, Christmas tree farms"                                           | 2016          | "Truck, Nursery, and Berry Crops"              | 13             | 
| Bush berries                                                                       | 2019          | "Truck, Nursery, and Berry Crops"              | 13             | 
| Strawberries                                                                       | 2020          | "Truck, Nursery, and Berry Crops"              | 13             | 
| Peppers                                                                            | 2021          | "Truck, Nursery, and Berry Crops"              | 13             | 
| Broccoli                                                                           | 2022          | "Truck, Nursery, and Berry Crops"              | 13             | 
| Cabbage                                                                            | 2023          | "Truck, Nursery, and Berry Crops"              | 13             | 
| Cauliflower                                                                        | 2024          | "Truck, Nursery, and Berry Crops"              | 13             | 
| Brussels Sprouts                                                                   | 2025          | "Truck, Nursery, and Berry Crops"              | 13             | 
| Greenhouse                                                                         | 2027          | Urban                                          | 1              | 
| Urban                                                                              | 2100          | Urban                                          | 1              | 
| Commercial                                                                         | 2110          | Urban                                          | 1              | 
| Offices                                                                            | 2111          | Urban                                          | 1              | 
| Hotels                                                                             | 2112          | Urban                                          | 1              | 
| Motels                                                                             | 2113          | Urban                                          | 1              | 
| RV Parking                                                                         | 2114          | Urban                                          | 1              | 
| Institutions                                                                       | 2115          | Urban                                          | 1              | 
| Schools                                                                            | 2116          | Urban                                          | 1              | 
| Municipal buildings                                                                | 2117          | Urban                                          | 1              | 
| Miscellaneous high water use                                                       | 2118          | Urban                                          | 1              | 
| Industrial                                                                         | 2120          | Urban                                          | 1              | 
| Manufacturing                                                                      | 2121          | Urban                                          | 1              | 
| Extractive Industries                                                              | 2122          | Urban                                          | 1              | 
| Storage and distribution                                                           | 2123          | Urban                                          | 1              | 
| Saw Mills                                                                          | 2126          | Urban                                          | 1              | 
| Oil refineries                                                                     | 2127          | Urban                                          | 1              | 
| Paper mills                                                                        | 2128          | Urban                                          | 1              | 
| Meat Packing Plants                                                                | 2129          | Urban                                          | 1              | 
| Urban landscape                                                                    | 2130          | Urban                                          | 1              | 
| Lawn - irrigated                                                                   | 2131          | Urban                                          | 1              | 
| Golf course                                                                        | 2132          | Urban                                          | 1              | 
| Ornamental landscape                                                               | 2133          | Urban                                          | 1              | 
| Cemeteries - irrigated                                                             | 2134          | Urban                                          | 1              | 
| Cemeteries - non-irrigated                                                         | 2135          | Urban                                          | 1              | 
| Residential                                                                        | 2140          | Urban                                          | 1              | 
| Single family > 1 acre                                                             | 2141          | Urban                                          | 1              | 
| Single family 1-8 units/acre                                                       | 2142          | Urban                                          | 1              | 
| Multiple family                                                                    | 2143          | Urban                                          | 1              | 
| Trailer Courts                                                                     | 2144          | Urban                                          | 1              | 
| Vacant                                                                             | 2150          | Barren                                         | 4              | 
| Unpaved                                                                            | 2151          | Barren                                         | 4              | 
| Vacant unlisted                                                                    | 2152          | Barren                                         | 4              | 
| Railroad right of way                                                              | 2153          | Barren                                         | 4              | 
| Paved areas                                                                        | 2154          | Barren                                         | 4              | 
| Airport runways                                                                    | 2156          | Barren                                         | 4              | 
| (Unknown referent)                                                                 | 2161          | No data                                        | 0              | 
| "Vineyards (includes table grapes, wine grapes, and raisins)"                      | 2200          | Vineyards                                      | 15             | 
| Out of area                                                                        | 2600          | No data                                        | 0              | 
| Steel mill                                                                         | 212910        | Urban                                          | 1              | 
| Fruit and Vegetable cannery                                                        | 212911        | Urban                                          | 1              | 
| Miscellaneous high water use                                                       | 212912        | Urban                                          | 1              | 
| Sewage treatment plant                                                             | 212913        | Urban                                          | 1              | 
| Waste accumulation sites                                                           | 212914        | Urban                                          | 1              | 
| Wind farms/solar farms                                                             | 212915        | Urban                                          | 1              | 
