import bpy
import re

for i in bpy.data.objects:
    if re.match(".*Flag.*", i.name):
        bpy.context.view_layer.objects.active = i
        print(i)
        bpy.context.object.modifiers["Cloth"].settings.quality = 1
        bpy.context.object.modifiers["Cloth"].collision_settings.use_self_collision = True
        bpy.context.object.modifiers["Cloth"].settings.time_scale = 0.1
        bpy.context.object.modifiers["Cloth"].settings.tension_stiffness = 150
        bpy.context.object.modifiers["Cloth"].settings.compression_stiffness = 150
        bpy.context.object.modifiers["Cloth"].settings.effector_weights.gravity = 0
        bpy.context.object.modifiers["Cloth"].settings.vertex_group_mass = "Group"
        bpy.context.object.modifiers["Cloth"].collision_settings.use_self_collision = True
        bpy.context.object.modifiers["Cloth"].collision_settings.distance_min = 0.001
        bpy.context.object.modifiers["Cloth"].collision_settings.collision_quality = 1
        bpy.context.object.modifiers["Cloth"].collision_settings.self_distance_min = 0.001
        bpy.context.object.modifiers["Cloth"].point_cache.frame_end = 4000
        bpy.context.active_object.animation_data_clear()

#        bpy.ops.object.editmode_toggle()
#        bpy.ops.mesh.subdivide()
#        bpy.ops.object.editmode_toggle()
        bpy.ops.object.shade_smooth()

        bpy.ops.object.modifier_add(type='SMOOTH')
       



