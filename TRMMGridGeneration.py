import arcpy
from arcpy.sa import *

data = arcpy.GetParameterAsText(0)
#GDB = arcpy.GetParameterAsText(1)
folder = arcpy.GetParameterAsText(1)
try :
    
    inputPointFeature = data
    #year= inputPointFeature.split("\\")[-1]
    
    
    cellSize= 0.01
    power=2
    
    arcpy.MakeFeatureLayer_management (inputPointFeature, "lyr")
    arcpy.SelectLayerByAttribute_management ("lyr", "NEW_SELECTION")
    ListFields=arcpy.ListFields("lyr")
    for field in ListFields:
        if (field.name!='OBJECTID' and  field.name!='Shape' and field.name!='grid_code' and field.name != 'POINT_X' and field.name!='pointid' and field.name != 'POINT_Y'):
    
            outIDW = Idw("lyr", field.name, cellSize, power)
            outIDW.save(folder+"\\"+field.name+".tif")

    
    #arcpy.IDW_ga(data,zField1,"\\LST"+zField1,GDB+"\\LST"+zField1)
    
    #arcpy.IDW_ga(data,zField2,"\\LST"+zField2,GDB+"\\LST"+zField2)

except Exception as e:
    arcpy.AddError(e.args[0])
    arcpy.AddMessage("Problem in executing IDW")
