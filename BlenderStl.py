import bpy
import os
import math
import requests
import sys  

def main(URI):
    r = requests.get("https://scannables.scdn.co/uri/plain/svg/ffffff/black/640/" + URI, stream=True)

    with open("SpotifyCodeDownload.svg", 'wb') as f:
        for chunk in r.iter_content(1024): 
            f.write(chunk)
        
    
    filepath = bpy.data.filepath
    directory = os.path.dirname(filepath)
    path_svg = os.path.join( directory , "SpotifyCodeDownload.svg")

    bpy.context.scene.unit_settings.scale_length = 100



    for o in bpy.context.scene.objects:
        o.select_set(True)

    bpy.ops.object.delete()

    bpy.ops.object.select_all(action='DESELECT')


    bpy.ops.import_curve.svg(filepath="SpotifyCodeDownload.svg", filter_glob="*.svg")

    for obje in bpy.data.objects:
        obje.select_set(False)

    bpy.data.objects['Curve'].select_set(True)
    bpy.ops.object.delete()

    bpy.ops.object.select_all(action='DESELECT')

    for obj in bpy.data.collections['SpotifyCodeDownload.svg'].all_objects:
        obj.select_set(True)


    bpy.context.view_layer.objects.active = bpy.data.objects["Curve.001"]

    bpy.ops.object.join()

    bpy.ops.object.convert(target='MESH')

    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')

    curve = bpy.data.objects["Curve.001"]



    bpy.context.object.rotation_euler[2] = 1.5708
    bpy.ops.transform.resize(value=(0.277968, 0.277968, 0.277968))


    bpy.ops.transform.translate(value=(-0.0734364, -0.0216113, 0.0009043))



    bpy.ops.object.editmode_toggle()

    bpy.ops.mesh.select_all(action='SELECT')

    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 0.000875622), "orient_type":'NORMAL', "orient_matrix":((-0.538016, -0.842934, 0), (0.842934, -0.538016, 0), (0, 0, 1)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})

    bpy.ops.object.editmode_toggle()







    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, align='WORLD', location=(0, 0, 0))
    bpy.context.object.scale = (0.005, 0.03, 0.001)

    bpy.ops.mesh.primitive_cylinder_add(radius=0.003, depth=0.005, enter_editmode=False, align='WORLD', location=(0, -0.024, 0))

    cube = bpy.data.objects['Cube']
    cylinder = bpy.data.objects['Cylinder']

    bool = cube.modifiers.new(type="BOOLEAN", name="bool")
    bool.object = cylinder
    bool.operation = 'DIFFERENCE'
    bpy.context.view_layer.objects.active = cube
    bpy.ops.object.modifier_apply(modifier="bool")

    bpy.ops.object.select_all(action='DESELECT')
    cylinder.select_set(True)
    bpy.ops.object.delete() 

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.export_mesh.stl(filepath="out.stl", use_selection=True, global_scale=1000)


if (len(sys.argv)>1):
    argv = sys.argv
    URI = argv[argv.index("--") + 1]
    main(URI)
    
else:
    print("Usage: python Spotifcode.py <URI>")

    

