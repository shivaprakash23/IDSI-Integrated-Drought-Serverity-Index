import arcpy
from arcpy.sa import *
try : 
    CurrentData = arcpy.GetParameterAsText(0)
    Minimum= arcpy.GetParameterAsText(1)
    Maximum= arcpy.GetParameterAsText(2)
    TRMMGDB = arcpy.GetParameterAsText(3)
except Exception as e:
    
    arcpy.AddError(e.args[0])
    arcpy.AddMessage("Problem data input")


try :
    MinimumRaster = Raster(Minimum)
    MaximumRaster = Raster(Maximum)
    CurrentDataRaster = Raster(CurrentData)
    TRMM= ((CurrentDataRaster-MinimumRaster)/(MaximumRaster-MinimumRaster))*100
    TRMM.save(TRMMGDB+"\\"+"PCI"+CurrentData.split(".")[0].split("\\")[-1])
    


except Exception as e:
    
    arcpy.AddError(e.args[0])
    arcpy.AddMessage("Problem data input")

