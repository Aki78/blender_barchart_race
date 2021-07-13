import bpy

my_countries = ['Japan', 'Angola', 'Italy', 'Andorra', 'Spain', 'Australia', 'Sweden', 'Germany', 'Colombia', 'Chile', 'China', 'Taiwan', 'Singapore', 'Peru', 'Kuwait', 'Norway', 'Albania', 'Russia', 'Korea', 'Vietnam', 'Iran', 'Pakistan', 'SouthAfrica', 'Canada', 'Thailand', 'Malaysia', 'Afghanistan', 'Netherlands', 'Mexico', 'Turkey', 'Algeria', 'Bahrain', 'France', 'UK', 'Nepal', 'Switzerland', 'Argentina', 'US', 'Brazil', 'Belgium', 'India']

for i in my_countries:
    ob = bpy.data.objects[i]
    # Get material
    mat = bpy.data.materials.get(i + "Material")
    if mat is None:
    # create material
        mat = bpy.data.materials.new(name=i+"Material")

# Assign it to object
    if ob.data.materials:
    # assign to 1st material slot
        ob.data.materials[0] = mat
    else:
    # no slots
        ob.data.materials.append(mat)