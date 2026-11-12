from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController()
Sky()

boxes = []

def Boden(position):
    boxes.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.5,
            color=color.green,
            position=position,
            texture='grass'
        )
    )

def Bauen(position):
    boxes.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.5,
            color=color.brown,
            position=position,
            texture='brick'
        )
    )

for x in range(30):
    for z in range(30):
        Boden((x, 0, z))

 # KEYBINDDES
def input(key):
    global selected_block
    for box in boxes:
        if box.hovered:
            if key == "right mouse down":
                Bauen(box.position + mouse.normal)
            if key == "left mouse down":
                boxes.remove(box)
                destroy(box)

    if key == 'scroll up':
        selected_block = (selected_block + 1) % len(block_types)
        update_hotbar()

    if key == 'scroll down':
        selected_block = (selected_block - 1) % len(block_types)
        update_hotbar()


# HOTBAR

block_types = [
    color.green,
    color.gray,
    color.brown
]

selected_block = 0
hotbar = []

for i, block_color in enumerate(block_types):
    slot = Entity(
        parent=camera.ui,
        model='quad',
        color=color.dark_gray,
        scale=(0.08, 0.08),
        position=(-0.09 + i * 0.09, -0.42)
    )

    Entity(
        parent=slot,
        model='quad',
        color=block_color,
        scale=0.7,
        z=-0.1
    )

    hotbar.append(slot)


def update_hotbar():
    for i, slot in enumerate(hotbar):
        if i == selected_block:
            slot.color = color.yellow
        else:
            slot.color = color.dark_gray







update_hotbar()























app.run()