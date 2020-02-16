import arcpy
from arcpy.sa import *
try : 
    folder = arcpy.GetParameterAsText(0)
    Minimum= arcpy.GetParameterAsText(1)
    Maximum= arcpy.GetParameterAsText(2)
    TCIFolder = arcpy.GetParameterAsText(3)

    arcpy.env.workspace=folder
    rasterList = arcpy.ListRasters("*","TIF")
    
except Exception as e:
    
    arcpy.AddError(e.args[0])
    arcpy.AddMessage("Problem data input")


try :
    MinimumRaster = Raster(Minimum)
    MaximumRaster = Raster(Maximum)
    for raster in rasterList:
        CurrentDataRaster = Raster(raster)
        TCI= ((MaximumRaster-CurrentDataRaster)/(MaximumRaster-MinimumRaster))*100
        TCI.save(TCIFolder+"\\"+"TCI"+raster)
    


except Exception as e:
    
    arcpy.AddError(e.args[0])
    arcpy.AddMessage("Problem data input")

