import bpy

#Refresh everything
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False, confirm=False)


#Setup Light
bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(-10, 10, 10), scale=(1, 1, 1))
bpy.context.object.data.energy = 50000

#Setup Camera
bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, 0 , 5), rotation=(0, -0, 0), scale=(1, 1, 1))
bpy.context.object.data.type = 'ORTHO'

#Add background mesh and add color white
bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0 ), scale=(10, 10, 0))

ob = bpy.context.active_object
mat = bpy.data.materials.get("Material")
if mat is None:
    mat = bpy.data.materials.new(name="Material")

if ob.data.materials:
    ob.data.materials[0] = mat
else:
    ob.data.materials.append(mat)
bpy.context.object.active_material.diffuse_color = (1, 1, 1, 1) 
