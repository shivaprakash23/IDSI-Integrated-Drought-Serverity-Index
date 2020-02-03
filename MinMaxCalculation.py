import arcpy
from arcpy.sa import *
try : 
    data = arcpy.GetParameterAsText(0)

except Exception as e:
    arcpy.AddError(e.args[0])
    arcpy.AddMessage("Input has problem")



try: 
    mcolumn = arcpy.ListFields(data)
    
    
except Exception as e:
    arcpy.AddError(e.args[0])
    arcpy.AddMessage("Field Listing problem")

try:
    ncolumn=[]

    for column in mcolumn:
        if (column.name!='OBJECTID' and  column.name!='Shape' and column.name!='grid_code' and column.name != 'POINT_X' and column.name!='pointid' and column.name != 'POINT_Y'):
            ncolumn.append(column.name)
    ncolumn.append("Minimum")
    ncolumn.append("Maximum")

except Exception as e:
    arcpy.AddError(e.args[0])
    arcpy.AddMessage("Column Filtering problem")

try : 

    arcpy.AddField_management(data,"Minimum", "DOUBLE")
    arcpy.AddField_management(data,"Maximum", "DOUBLE")

    minimum = 99999
    maximum = 0


    with arcpy.da.UpdateCursor(data, ncolumn) as cursor:
        for row in cursor:
            for eachrow in row:
                current = eachrow
                if ((current < minimum) and (current != "") and (current != None)):
                    minimum = current
                if ((current > maximum) and (current != "") and (current != None)):
                    maximum = current
            row[-2]=minimum
            row[-1]=maximum
            cursor.updateRow(row)
            minimum = 99999
            maximum = 0

except Exception as e:
    arcpy.AddError(e.args[0])
    arcpy.AddMessage("Problem in calculating Min and Max")
