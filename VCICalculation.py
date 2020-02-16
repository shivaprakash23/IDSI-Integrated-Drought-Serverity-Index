import arcpy
from arcpy.sa import *
try : 
    CurrentData = arcpy.GetParameterAsText(0)
    Minimum= arcpy.GetParameterAsText(1)
    Maximum= arcpy.GetParameterAsText(2)
    VCIGDB = arcpy.GetParameterAsText(3)
except Exception as e:
    
    arcpy.AddError(e.args[0])
    arcpy.AddMessage("Problem data input")


try :
    MinimumRaster = Raster(Minimum)
    MaximumRaster = Raster(Maximum)
    CurrentDataRaster = Raster(CurrentData)
    VCI= ((CurrentDataRaster-MinimumRaster)/(MaximumRaster-MinimumRaster))*100
    VCI.save(VCIGDB+"\\"+"VCI"+CurrentData.split(".")[0].split("\\")[-1])
    


except Exception as e:
    
    arcpy.AddError(e.args[0])
    arcpy.AddMessage("Problem data input")

