import bpy
import numpy as np
import csv

#========== Defining Functions ===========================================
def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.2f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])


def deleteMe(aText):
  for obj in bpy.context.selected_objects:
      obj.select_set(False)
  for i in bpy.data.objects:
    if aText in i.name:
        i.select_set(True)
        bpy.ops.object.delete()

def calculate_axis_ticks(max_value, max_ticks = 10, min_ticks = 5, axis_length = 50):


    def floor(number, bound=1):
        return bound * np.floor(number / bound)

    def nearest_floor_round(number):
        return floor(number, 10 ** (len(str(number))-1))

    n_ticks = nearest_floor_round(max_value) /  (10 ** (len(str(max_value)) -1 ))
    for i in range(10):
        if n_ticks < min_ticks:
            n_ticks *= 2
        else:
            break
    for i in range(10):
        if n_ticks > max_ticks:
            n_ticks /= 2
            n_ticks = int(n_ticks)
        else:
            break

    axis_ticks = np.arange(0, max_value + 1, nearest_floor_round(max_value) / n_ticks, dtype = int) # add one to include endpoint 
    #axis_ticks_str = [str(t) for t in axis_ticks]
    #if np.sum([len(str(t)) for t in axis_ticks]) > axis_length:
        #print("Warning: axis length exceeded by tick numbers")

    
    return axis_ticks

def listYPositions(i):
    if i < 10:
        return 1 - 0.2*i
    else:
        return -5 - 0.2*i

def initTicks(frameI,max_value, zHeight):
    for obj in bpy.context.selected_objects:
        obj.select_set(False)
    materialVisible = bpy.data.materials.get("VisibleTicks")
    materialImvisible = bpy.data.materials.get("Invisible")
    
    ticks = calculate_axis_ticks(int(max_value), max_ticks = 5, min_ticks = 3, axis_length = 100)
    formerTicks = []
    for i,j in enumerate(ticks):
        formerTicks.append(str(int(j)))
        bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(-1 + (j/max_value)*3, 0, zHeight-0.01))
        bpy.context.active_object.scale = (0.005, 1, 0.02)
        bpy.context.active_object.data.materials.append(materialVisible)
        bpy.context.active_object.name = str(int(j)) + "TickBar" 
        #print(i, j, bpy.context.active_object.name )
        font_curve = bpy.data.curves.new(type="FONT",name="Ticks")
#        font_curve.body = str(int(j))
        if int(j) > 999:
          font_curve.body = human_format(int(j))
        else:
          font_curve.body = str(int(j))
        font_obj = bpy.data.objects.new("Font Object", font_curve)
        font_obj.name =str(int(j)) + "Ticks"
        bpy.context.scene.collection.objects.link(font_obj)
        print(j)
        if int(j)==0:
          font_obj.location = (-0.98 + (j/max_value)*3-0.1,-1.1 , zHeight)
        else:
          font_obj.location = (-0.98 + (j/max_value)*3-0.1,-1.1 , zHeight)
        font_obj.scale = (0.1,0.1,0.1)
        font_obj.data.materials.append(materialVisible)
    return formerTicks

def addTicks(max_value, zHeight, formerTicks):
    for obj in bpy.context.selected_objects:
        obj.select_set(False)
# Get material
    materialVisible = bpy.data.materials.get("VisibleTicks")
    materialImvisible = bpy.data.materials.get("Invisible")
    for i,j in enumerate(formerTicks):

        #for i in bpy.data.objects:
            #print(i.name)
        bpy.data.objects[str(int(j))+"TickBar"].select_set(True)
        bpy.ops.object.delete(use_global=False, confirm=True)

        bpy.data.objects[str(int(j))+"Ticks"].select_set(True)
        bpy.ops.object.delete(use_global=False, confirm=True)
    
    ticks = calculate_axis_ticks(int(max_value), max_ticks = 5, min_ticks = 3, axis_length = 100)
    formerTicks = []
    for i,j in enumerate(ticks):
        formerTicks.append(str(int(j)))
        bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(-1 + (j/max_value)*3, 0, zHeight-0.01))
        bpy.context.active_object.scale = (0.005, 1, 0.1)
        bpy.context.active_object.data.materials.append(materialVisible)
        bpy.context.active_object.name = str(int(j)) + "TickBar" 

        font_curve = bpy.data.curves.new(type="FONT",name="Ticks")
        # font_curve.body = str(int(j))
        if int(j) > 999:
          font_curve.body = human_format(int(j))
        else:
          font_curve.body = str(int(j))

        #print(human_format(int(j)))
        font_obj = bpy.data.objects.new("Font Object", font_curve)
        font_obj.name =str(int(j)) + "Ticks"
        bpy.context.scene.collection.objects.link(font_obj)

        if int(j)==0:
          font_obj.location = (-0.98 + (j/max_value)*3-0.1,-1.1 , zHeight)
        else:
          font_obj.location = (-0.98 + (j/max_value)*3-0.1,-1.1 , zHeight)

        font_obj.scale = (0.1,0.1,0.1)
        font_obj.data.materials.append(materialVisible)
    return formerTicks

def addBar(myNames,xLeft, zHeight):
    for obj in bpy.context.selected_objects:
        obj.select_set(False)
    for i,j in  enumerate(myNames):
        bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, align='WORLD', location=(xLeft+1, listYPositions(i), zHeight))
        bpy.context.active_object.name=j
        bpy.context.active_object.scale = (1, 0.18, 0.01)

def initValues(frameI,myCountries,myValue, zHeight):
    deleteMe("Value")
    whiteGlow = bpy.data.materials.get("whiteGlow")
    for obj in bpy.context.selected_objects:
        obj.select_set(False)
    formerValues = []
    for i,j in  enumerate(myCountries):
        formerValues.append(j)
        font_curve = bpy.data.curves.new(type="FONT",name=j + str(int(myValue[i])))
        font_curve.body = str(int(myValue[i]))
        font_obj = bpy.data.objects.new("Font Object", font_curve)
        font_obj.name = j + "Value"
        font_obj.data.materials.append(whiteGlow)
        bpy.context.scene.collection.objects.link(font_obj)
        font_obj.location = ((myValue[i])/max(myValue) * 3 - 0.90, listYPositions(i)-0.03,zHeight)
        font_obj.scale = (0.1, 0.1, 0.1)

def initDate():
    deleteMe("dateObj")
    whiteGlow = bpy.data.materials.get("whiteGlow")
    font_curve = bpy.data.curves.new(type="FONT",name="dateNow")
    font_curve.body = "2020-01-01"
    font_obj = bpy.data.objects.new("Font Object", font_curve)
    font_obj.name = "dateObj"
    font_obj.data.materials.append(whiteGlow)
    bpy.context.scene.collection.objects.link(font_obj)
    font_obj.location = (1.301,1.2276, 0.01)
    font_obj.scale = (0.25, 0.25, 0.1)


def updateDate(currentDate):
    font_obj = bpy.data.objects["dateObj"].data.body =currentDate

def updateValuePositions(frameI,myCountries,myValue, zHeight):
    for i,j in  enumerate(myCountries):
        font_obj = bpy.data.objects[j+"Value"]  
        font_obj.location = ((myValue[i])/max(myValue)*3 - 0.90, listYPositions(i)-0.03,zHeight)
        font_obj.keyframe_insert('location', frame=frameI)

def updateValues(myCountries, myValue):
    for i,j in enumerate(myCountries):
#        bpy.data.objects[j+"Value"].data.body = str(int(myValue[i]))
        bpy.data.objects[j+"Value"].data.body = "{:,}".format(int(myValue[i]))

def addName(myCountries, zHeight):
    for i,j in  enumerate(myCountries):
        font_curve = bpy.data.curves.new(type="FONT",name=j + "Name")
        font_curve.body = j 
        font_obj = bpy.data.objects.new("Font Object", font_curve)
        font_obj.name = j + "Name"
        bpy.context.scene.collection.objects.link(font_obj)
        font_obj.location = (x_left,listYPositions(i) - 0.03, zHeight)
        font_obj.scale = (0.1,0.1,0.1)

def updateNamePosition(frameI,myCountries):
    for i,j in  enumerate(myCountries):
        bpy.data.objects[j+"Name"].location[1] = listYPositions(i) - 0.03
        bpy.data.objects[j+"Name"].keyframe_insert('location', frame=frameI)

def getValuesForEachCountry(myIndex, fd, countries):
    values_for_each_country = []
    for i,j in enumerate(countries):
      for k,l in enumerate(fd):
        if j == l[1]: 
          if l[2] == str(myIndex):
              values_for_each_country.append(float(l[4]))
              currentDate = l[3]
    return(values_for_each_country, currentDate)

def updateBarSize(my_countries, valuesForEachCountry):
    for i,j in enumerate(my_countries):
        bpy.data.objects[j].data.vertices[1].co.x = (valuesForEachCountry[i])/max(valuesForEachCountry)*3
        bpy.data.objects[j].data.vertices[3].co.x = (valuesForEachCountry[i])/max(valuesForEachCountry)*3
        bpy.data.objects[j].data.vertices[0].co.x = -0.05
        bpy.data.objects[j].data.vertices[2].co.x = -0.05
        bpy.data.objects[j].location[2] = 0.03
    
def updateBarPosition(frameI,my_countries):
    for i,j in enumerate(my_countries):
        bpy.data.objects[j].location[1] = listYPositions(i)
        bpy.data.objects[j].keyframe_insert('location', frame=frameI)
        bpy.data.objects[j].location[2] = 0.02 + i*0.0001
        
def updateFlagPosition(frameI,my_countries):
    for i,j in enumerate(my_countries):
        bpy.data.objects[j+"Flag"].location = (-1.2,listYPositions(i), 0.01)
        bpy.data.objects[j+"Flag"].keyframe_insert('location', frame=frameI)
def interpolateNpArray(x,x1,x2,y1,y2):
    return (np.array(y1) + (x - x1)*(np.array(y2) - np.array(y1))/(x2 - x1)).tolist()


if __name__ == '__main__':
    #=========== Start Operations =================================================

    #====Parameters=============

    start_data = 0
    end_data = 438
    start_bake = start_data
    end_bake = end_data
    framesPerDataPoint = 15
    offset = 310

    my_countries = ['Japan', 'Angola', 'Italy', 'Andorra', 'Spain', 'Australia', 'Sweden', 'Germany', 'Colombia', 'Chile', 'China', 'Taiwan', 'Singapore', 'Peru', 'Kuwait', 'Norway', 'Albania', 'Russia', 'Korea', 'Vietnam', 'Iran', 'Pakistan', 'SouthAfrica', 'Canada', 'Thailand', 'Malaysia', 'Afghanistan', 'Netherlands', 'Mexico', 'Turkey', 'Algeria', 'Bahrain', 'France', 'UK', 'Nepal', 'Switzerland', 'Argentina', 'US', 'Brazil', 'Belgium', 'India']
    fp = "/home/aki/animation_projects/data/final.csv"
    #fp = "/home/aki/BlenderProjects/animated-plotengine/data/enhanced_global_covid_data.csv"


    # layout parameters
    z_height = 0.015
    x_left = -2


    renderFilepath = '/home/aki/'
    renderFilePrefix = 'test'
    #====Startup function
    deleteMe("Bar")
    deleteMe("Tick")

    #====initiate lists=========

    timeOrderedDataList = []
    #countries = []
    #listOfTopCountries = []

    # reading
    #===========================
    with open( fp ) as csvfile:
        rdr = csv.reader(csvfile)
        nameBefore = ""
        #countries.append(nameBefore)
        for i, row in enumerate(rdr): 
            if i == 0:
                nameBefore = row[1]
                continue # Skip column titles
            timeOrderedDataList.append(row)
            # if row[1]!=nameBefore: ## Add countries if not defined
                # my_countries.append(row[1])
            nameBefore = row[1]


    mat = bpy.data.materials.get("Material")
    if mat is None:
        mat = bpy.data.materials.new(name="Material")



    valuesForEachCountry, currentDate = getValuesForEachCountry(0, timeOrderedDataList, my_countries)
    formerTicks = initTicks(0,max(valuesForEachCountry), z_height)

    initValues(0,my_countries,valuesForEachCountry, z_height)
    bpy.context.scene.render.image_settings.file_format='JPEG'

    for i in bpy.data.objects:
        i.animation_data_clear()

    #Bake key frames
    for dataFrame in range(start_bake,end_bake): # pre Key Frames
    #    if dataFrame % framesPerDataPoint  == 0:
        valuesForEachCountry, currentDate = getValuesForEachCountry(dataFrame, timeOrderedDataList, my_countries)

        sortedIndices = sorted(range(len(valuesForEachCountry)), key=lambda k: -valuesForEachCountry[k])
        sorted_values = [valuesForEachCountry[i] for i in sortedIndices]
        sorted_countries = [my_countries[i] for i in sortedIndices]
        #listOfTopCountries.append(sorted_countries[0:11])

        updateNamePosition(dataFrame*framesPerDataPoint,sorted_countries)
        updateBarPosition(dataFrame*framesPerDataPoint,sorted_countries)
        updateValuePositions(dataFrame*framesPerDataPoint, sorted_countries, sorted_values, z_height)
        updateFlagPosition(dataFrame*framesPerDataPoint, sorted_countries)

        print("frame: ", dataFrame, " baked...")

    #listOfTopCountries = [item for sublist in listOfTopCountries for item in sublist]


    #Start each interpolated and key frames
    frameNumber = offset*framesPerDataPoint - 1
    initDate()

    for dataFrame in range(start_data+offset,end_data): # for each frame

        y2, currentDate = getValuesForEachCountry(dataFrame + 1, timeOrderedDataList, my_countries)
        y1, currentDate = getValuesForEachCountry(dataFrame , timeOrderedDataList, my_countries)
        updateDate(currentDate)

        for frameI in range(0, framesPerDataPoint ):
            print("frame: ", frameNumber, "Start")
            bpy.context.scene.render.filepath = renderFilepath + renderFilePrefix + "_" + "{:05d}".format(frameNumber) 
            bpy.data.scenes['Scene'].frame_set(frameNumber)

            valuesForEachCountry = interpolateNpArray(frameI, 0, framesPerDataPoint,y1,y2)

            formerTicks = addTicks(max(valuesForEachCountry), z_height, formerTicks )
            bpy.data.objects['0Ticks'].location[0] += 0.05
            #updating non-keyframable objects only
            updateValues(my_countries, valuesForEachCountry)
            updateBarSize(my_countries, valuesForEachCountry)
            bpy.ops.render.render(use_viewport=True, write_still=True)
            frameNumber += 1
            print("frame: ", frameNumber, "Done")


#
#brr = BarRaceRenderer()
#brr.initialize(fp, ...)
#brr.set_layout()
#brr.addKeyFramesInterpolated([updateNamePosition, updateBarPosition], framesPerDataPoint)
#brr.addExtraObjectsEveryFrame([updateValues, updateBarSize])
#
#brr.addKeyFrameNamePosition(framesPerDataPoint)
#brr.addKeyFrameBarPosition(10)
#
#
#class BarRaceRenderer():
#    
#def __init__(self, filePath):
#self.filePath = filePath
#self.data = csvreader(filePath)
#
#self._a = 5
#return
#
#def _doCrazyStuff(self, a,b,v):
#print("crazy")
#return
#
#def __str__(self):
#return "yor"
#
##
#
#renderBarChartRace(fp, Material, ..........., z_height=-2, )
#
#
