import arcpy
from arcpy.sa import *

data = arcpy.GetParameterAsText(0)
folder = arcpy.GetParameterAsText(1)

arcpy.env.workspace=folder

rasterList = arcpy.ListRasters("*","TIF")

ExtractMultiValuesToPoints(data, rasterList,"NONE")
    
