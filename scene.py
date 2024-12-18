from model import *
#importing objs
class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        n, s = 80, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))
        #add(Cube(app))
        #add(Cube(app, tex_id=1, pos=(-2.5, 0, 0), rot=(45, 0, 0)))
        #add(Cube(app, tex_id=2, pos=(2.5, 0, 0), rot=(0, 0, 45)))

    def render(self):
        for obj in self.objects:
            obj.render()