import bpy
my_countries = ['Japan', 'Angola', 'Italy', 'Andorra', 'Spain' , 'Australia', 'Sweden', 'Germany', 'Colombia', 'Chile', 'China', 'Taiwan', 'Singapore', 'Peru', 'Kuwait', 'Norway', 'Albania', 'Russia', 'Korea', 'Vietnam', 'Iran', 'Pakistan', 'SouthAfrica', 'Canada', 'Thailand', 'Malaysia', 'Afghanistan', 'Netherlands', 'Mexico', 'Turkey', 'Algeria', 'Bahrain', 'France', 'UK', 'Nepal', 'Switzerland', 'Argentina', 'US', 'Brazil', 'Belgium', 'India']

C = bpy.context
src_obj = bpy.context.active_object
newFlags = []
for i in my_countries:
    new_obj = src_obj.copy()
    new_obj.data = src_obj.data.copy()
    new_obj.animation_data_clear()
    new_obj.name = str(i) + "Flag"
    newFlags.append(new_obj)
    

for newObj in newFlags:
    bpy.context.scene.collection.objects.link(newObj)