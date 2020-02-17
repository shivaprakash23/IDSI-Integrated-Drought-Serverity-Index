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
    ncolumn.append("DroughtMonths")
    ncolumn.append("NonDroughtMonths")
    ncolumn.append("ExtremeDrought")
    ncolumn.append("SevereDrought")
    ncolumn.append("ModerateDrought")
    ncolumn.append("Stress")
    ncolumn.append("Watch")
    ncolumn.append("Normal")
    ncolumn.append("Healthy")
    ncolumn.append("Frequency")
    ncolumn.append("Intensity")
    
    

except Exception as e:
    arcpy.AddError(e.args[0])
    arcpy.AddMessage("Column Filtering problem")

try : 
    arcpy.AddField_management(data,"NoofNull", "DOUBLE")
    arcpy.AddField_management(data,"DroughtMonths", "DOUBLE")
    arcpy.AddField_management(data,"NonDroughtMonths", "DOUBLE")
    arcpy.AddField_management(data,"ExtremeDrought", "DOUBLE")
    arcpy.AddField_management(data,"SevereDrought", "DOUBLE")
    arcpy.AddField_management(data,"ModerateDrought", "DOUBLE")
    arcpy.AddField_management(data,"Stress", "DOUBLE")
    arcpy.AddField_management(data,"Watch", "DOUBLE")
    arcpy.AddField_management(data,"Normal", "DOUBLE")
    arcpy.AddField_management(data,"Healthy", "DOUBLE")
    arcpy.AddField_management(data,"Frequency", "DOUBLE")
    arcpy.AddField_management(data,"Intensity", "DOUBLE")
    

    Drought = 0
    NoDrought = 0
    ExtremeDrought =0
    SevereDrought =0
    ModerateDrought=0
    Stress=0
    Watch=0
    Normal=0
    Healthy=0
    Frequency=0
    Intensity =0
    NoofNull=0
    
    with arcpy.da.UpdateCursor(data, ncolumn) as cursor:
        for row in cursor:
            for eachrow in row:
                current = eachrow
                if ((current <= 4) and (current != "") and (current != None)):
                    NoDrought = NoDrought+1
                if ((current > 4) and (current != "") and (current != None)):
                    Drought = Drought+1
                if ((current == 7) and (current != "") and (current != None)):
                    ExtremeDrought = ExtremeDrought+1
                if ((current == 6) and (current != "") and (current != None)):
                    SevereDrought = SevereDrought+1
                if ((current ==5) and (current != "") and (current != None)):
                    ModerateDrought = ModerateDrought+1
                if ((current == 4) and (current != "") and (current != None)):
                    Stress = Stress+1
                if ((current == 3) and (current != "") and (current != None)):
                    Watch = Watch+1
                if ((current == 2) and (current != "") and (current != None)):
                    Normal = Normal+1
                if ((current == 1) and (current != "") and (current != None)):
                    Healthy = Healthy+1
                if ((current != "") and (current != None)):
                    NoofNull = NoofNull+1

                    
            if(NoofNull!=77):
                
                Intensity = ((ExtremeDrought*7)+ (SevereDrought *6)+(ModerateDrought *5)+(Stress *4)+(Watch*3)+(Normal *2)+(Healthy*1))/(77-NoofNull)
                Frequency = (Drought/(77-NoofNull))*100

            
            row[-1]=Intensity
            row[-2]=Frequency
            row[-3]=Healthy
            row[-4]=Normal
            row[-5]=Watch
            row[-6]=Stress
            row[-7]=ModerateDrought
            row[-8]=SevereDrought
            row[-9]=ExtremeDrought
            row[-10]=NoDrought
            row[-11]=Drought
            row[-12]=NoofNull
            
            cursor.updateRow(row)
            
            Drought = 0
            NoDrought = 0
            ExtremeDrought =0
            SevereDrought =0
            ModerateDrought=0
            Stress=0
            Watch=0
            Normal=0
            Healthy=0
            Frequency=0
            Intensity =0
            NoofNull=0

except Exception as e:
    arcpy.AddError(e.args[0])
    arcpy.AddMessage("Problem in calculating Min and Max")
