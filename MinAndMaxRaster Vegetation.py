import arcpy
from arcpy.sa import *

data = arcpy.GetParameterAsText(0)
#GDB = arcpy.GetParameterAsText(1)
folder = arcpy.GetParameterAsText(1)
try :
    
    inputPointFeature = data
    year= inputPointFeature.split("\\")[-1]
    zField1= "Minimum"
    zField2= "Maximum"
    cellSize= 0.01
    power=2
    arcpy.MakeFeatureLayer_management (inputPointFeature, "lyr")
    arcpy.SelectLayerByAttribute_management ("lyr", "NEW_SELECTION", '"Minimum" <> 99999')
    
    outIDW = Idw("lyr", zField1, cellSize, power)
    outIDW.save(folder+"\\LST"+zField1+year+".tif")

    arcpy.SelectLayerByAttribute_management ("lyr", "NEW_SELECTION", '"Maximum" <> 99999')
    outIDW = Idw("lyr", zField2, cellSize, power)
    outIDW.save(folder+"\\LST"+zField2+year+".tif")

    
    #arcpy.IDW_ga(data,zField1,"\\LST"+zField1,GDB+"\\LST"+zField1)
    
    #arcpy.IDW_ga(data,zField2,"\\LST"+zField2,GDB+"\\LST"+zField2)

except Exception as e:
    arcpy.AddError(e.args[0])
    arcpy.AddMessage("Problem in executing IDW")
