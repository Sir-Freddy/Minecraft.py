from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# grass_texture = load_texture('assets/grass_block.png')

window.fps_counter.enabled = False
window.exit_button.visible = False

class Voxel(Button):
    def __init__(self, position = (0,0,0)): # -> def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            # model = 'assets/block',    -> put a texture of a block made with blender to have the UV map
            origin_y = 0.5,
            texture = 'white_cube', # -> texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.light_gray,
            # scale = 0.5,    -> change this when texture is loaded
        )
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal)
            if key == 'right mouse down':
                destroy(self)

for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x,0,z))


player = FirstPersonController()

app.run()
