import arcpy
from arcpy.sa import *
try : 
    VCIFolder = arcpy.GetParameterAsText(0)
    PCIFolder = arcpy.GetParameterAsText(1)
    TCIFolder = arcpy.GetParameterAsText(2)
    IDSIFolder = arcpy.GetParameterAsText(3)
except Exception as e:
    
    arcpy.AddError(e.args[0])
    arcpy.AddMessage("Problem data input")


try :
    arcpy.env.workspace=VCIFolder
    VCIList = arcpy.ListRasters("*","TIF")
    arcpy.env.workspace=PCIFolder
    PCIList = arcpy.ListRasters("*","TIF")
    arcpy.env.workspace=TCIFolder
    TCIList = arcpy.ListRasters("*","TIF")
    i=0
    for raster in VCIList:

        VCIRaster = Raster(VCIFolder+"\\"+VCIList[i])
        arcpy.AddMessage("VCI LIST")
        PCIRaster = Raster(PCIFolder+"\\"+PCIList[i])
        arcpy.AddMessage("PCI LIST")
        TCIRaster = Raster(TCIFolder+"\\"+TCIList[i])
        arcpy.AddMessage("TCI LIST")
        IDSI = (0.33*VCIRaster)*(((TCIRaster+PCIRaster)/(0.33*(TCIRaster+PCIRaster+VCIRaster+1)))+1)
        IDSI.save(IDSIFolder+"\\"+"IDSI"+PCIList[i].split(".")[0][7:]+".tif")

        IDSIClass = Con((IDSI >= 0)  &  (IDSI  <= 14),7,
        Con((IDSI > 14)  &  (IDSI  <= 28),6,
        Con((IDSI > 28)  &  (IDSI  <= 42),5,
        Con((IDSI > 42)  &  (IDSI  <= 58),4,
        Con((IDSI > 58)  &  (IDSI  <= 70),3,
        Con((IDSI > 70)  &  (IDSI  <= 84),2,
        Con((IDSI > 84)  &  (IDSI  <= 100),1,
        0)))))))

        IDSIClass.save(IDSIFolder+"\\"+"IDSIClassified"+PCIList[i].split(".")[0][7:]+".tif")
        i=i+1
    


except Exception as e:
    
    arcpy.AddError(e.args[0])
    arcpy.AddMessage("Problem data input")

