import sys 
import arcpy
import os 
project_folder = r"C:\Users\admin\Documents\ArcGIS\Projects\python_ex3"
input_folder = r"C:\Users\admin\Documents\ArcGIS\Projects\python_ex3\DATA"
roads = os.path.join(input_folder,"ROADS.shp")
boundary = os.path.join(input_folder,"BOUNDARY.shp")
buildings = os.path.join(input_folder,"BUILDINGS.shp")
pofw = os.path.join(input_folder,"POFW.shp")
waterbodies = os.path.join(input_folder,"WATERBODIES.shp")
railways = os.path.join(input_folder,"RAILWAYS.shp")

#description = arcpy.Describe(roads)
#print("Name:",description.name)

arcpy.env.workspace = input_folder
arcpy.env.overwriteOutput = True
output = r"C:\Users\admin\Documents\ArcGIS\Projects\python_ex3\output"
#arcpy.env.overwriteOutput = True

#arcpy.analysis.Buffer(
    #in_features=pofw,
    #out_feature_class=os.path.join(output,"pofwbuffer"),
    #buffer_distance_or_field="100 meters",
    #dissolve_option="ALL"
    #)

#os.path.join to declare the path of the output 
#dissolve option to merge overlapping buffers of adjacent features
#print("POFW buffer completed successfully")


#arcpy.env.overwriteOutput = False

#pofw_100 = os.path.join(output, "pofwbuffer.shp")
#arcpy.analysis.Clip(
#   in_features=roads,
#   clip_features=pofw_100, 
#   out_feature_class=os.path.join(output,"roads_100")
#   )

#pofw_100 = os.path.join(output, "pofwbuffer.shp")
#arcpy.analysis.Clip(
#   in_features=buildings,
#   clip_features=pofw_100, 
#   out_feature_class=os.path.join(output,"buildings_100")
#   )

#pofw_100 = os.path.join(output, "pofwbuffer.shp")
#arcpy.analysis.Clip(
#   in_features=waterbodies,
#   clip_features=pofw_100, 
#   out_feature_class=os.path.join(output,"water_100")
#   )

#print("clipped")

#pofw_200 = os.path.join(output, "200_pofwbuffer.shp")
#arcpy.analysis.Buffer(
#   in_features=pofw,
#   out_feature_class=os.path.join(output,"200_pofwbuffer"),
#   buffer_distance_or_field="200 meters",
#   dissolve_option="ALL"
#   ) 

#arcpy.analysis.Clip(
#   in_features=roads,
#   clip_features=pofw_200, 
#   out_feature_class=os.path.join(output,"roads_200")
#   )

#arcpy.analysis.Clip(
#   in_features=buildings,
#   clip_features=pofw_200, 
#   out_feature_class=os.path.join(output,"buildings_200")
#   )
 
#arcpy.analysis.Clip(
#   in_features=waterbodies,
#   clip_features=pofw_200, 
#   out_feature_class=os.path.join(output,"waterbodies_200")
#   )


#arcpy.analysis.Buffer(
#   in_features=pofw,
#   out_feature_class=os.path.join(output,"500_pofwbuffer"),
#   buffer_distance_or_field="500 meters",
#   dissolve_option="ALL"
#   )

#pofw_500 = os.path.join(output, "500_pofwbuffer.shp")

#arcpy.analysis.Clip(
#   in_features=roads,
#   clip_features=pofw_500, 
#   out_feature_class=os.path.join(output,"roads_500")
#   )

#arcpy.analysis.Clip(
#   in_features=buildings,
#   clip_features=pofw_500, 
#   out_feature_class=os.path.join(output,"buildings_500")
#   )

#arcpy.analysis.Clip(
#   in_features=waterbodies,
#   clip_features=pofw_500, 
#   out_feature_class=os.path.join(output,"waterbodies_500")
#   )

#print("clipped")

print("Within 100m of places of worship:")
roads_100 = os.path.join(output,"roads_100.shp")
print("Road count:",arcpy.GetCount_management(roads_100))

buildings_100 = os.path.join(output,"buildings_100.shp")
print("Building count:",arcpy.GetCount_management(buildings_100))

waterbodies_100 = os.path.join(output,"water_100.shp")
print("Number of waterbodies:",arcpy.GetCount_management(waterbodies_100))


print("Within 200m of places of worship:")
roads_200 = os.path.join(output,"roads_200.shp")
print("Road count:",arcpy.GetCount_management(roads_200))

buildings_200 = os.path.join(output,"buildings_200.shp")
print("Building count:",arcpy.GetCount_management(buildings_200))

waterbodies_200 = os.path.join(output,"waterbodies_200.shp")
print("Number of waterbodies:",arcpy.GetCount_management(waterbodies_200))


print("Within 500m of places of worship:")
roads_500 = os.path.join(output,"roads_500.shp")
print("Road count:",arcpy.GetCount_management(roads_500))

buildings_500 = os.path.join(output,"buildings_500.shp")
print("Building count:",arcpy.GetCount_management(buildings_500))

waterbodies_500 = os.path.join(output,"waterbodies_500.shp")
print("Number of waterbodies:",arcpy.GetCount_management(waterbodies_500))















 



