import arcpy
from arcpy.sa import *
try : 
    CurrentData = arcpy.GetParameterAsText(0)
    Minimum= arcpy.GetParameterAsText(1)
    Maximum= arcpy.GetParameterAsText(2)
    TCIGDB = arcpy.GetParameterAsText(3)
except Exception as e:
    
    arcpy.AddError(e.args[0])
    arcpy.AddMessage("Problem data input")


try :
    MinimumRaster = Raster(Minimum)
    MaximumRaster = Raster(Maximum)
    CurrentDataRaster = Raster(CurrentData)
    TCI= ((MaximumRaster-CurrentDataRaster)/(MaximumRaster-MinimumRaster))*100
    TCI.save(TCIGDB+"\\"+"TCI"+CurrentData.split(".")[0].split("\\")[-1])
    


except Exception as e:
    
    arcpy.AddError(e.args[0])
    arcpy.AddMessage("Problem data input")

