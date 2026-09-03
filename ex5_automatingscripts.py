import sys 
import arcpy
import os 
project_folder = r"C:\Users\admin\Documents\ArcGIS\Projects\pygis_ex05"
input = r"C:\Users\admin\Documents\ArcGIS\Projects\pygis_ex05\ex5_input\DATA"
output = r"C:\Users\admin\Documents\ArcGIS\Projects\pygis_ex05\ex5_output"
roads = os.path.join(input,"ROADS.shp")
boundary = os.path.join(input,"BOUNDARY.shp")
buildings = os.path.join(input,"BUILDINGS.shp")
pofw = os.path.join(input,"POFW.shp")
waterbodies = os.path.join(input,"WATERBODIES.shp")
railways = os.path.join(input,"RAILWAYS.shp")
arcpy.env.workspace = input
arcpy.env.overwriteOutput = True
arcpy.env.extent = None #will let you create/work on shapefiles outside the current map extent of the arcgis project

distances = [100, 200, 500]
clip_layers = [
    "roads", "buildings", "waterbodies", "railways"
]

#outer loop: what should be performed first 
#inner loop: what should be performed second 

arcpy.env.overwriteOutput = True
#outer loop
for distances in distances:
    buffer_output = os.path.join(output, f"pofwbuffer_{distances}m.shp") 
    #f allows you to automate whatever is present inside a variable. pofwbufffer_{distances}m.shp is a sample name. all the buffers created through this loop will have this name with diff values from {distances}
    arcpy.analysis.Buffer(
        in_features=pofw, 
        out_feature_class=buffer_output, 
        buffer_distance_or_field=f"{distances} meters", 
        dissolve_option="ALL", 
        method="GEODESIC"
    )

    #inner loop
    for layer in clip_layers: 
        input_layer = os.path.join(input, layer)
        clip_output = os.path.join(output, f"{layer}_pofw_{distances}m.shp")
        arcpy.analysis.Clip(
            in_features=input_layer,
            clip_features=buffer_output,
            out_feature_class=clip_output
            )

print("\nAnalysis completed successfully")
print(f"\nAll the output files are saved inside {output}")

