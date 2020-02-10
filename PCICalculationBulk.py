import arcpy
from arcpy.sa import *
try : 
    folder = arcpy.GetParameterAsText(0)
    Minimum= arcpy.GetParameterAsText(1)
    Maximum= arcpy.GetParameterAsText(2)
    TRMMFolder = arcpy.GetParameterAsText(3)

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
        TRMM= ((CurrentDataRaster-MinimumRaster)/(MaximumRaster-MinimumRaster))*100
        TRMM.save(TRMMFolder+"\\"+"PCI"+raster.split('.')[0]+".tif")
    


except Exception as e:
    
    arcpy.AddError(e.args[0])
    arcpy.AddMessage("Problem data input")

