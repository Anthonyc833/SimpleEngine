import pygame as pg
import moderngl as mgl
import sys
from model import *
from camera import Camera
from light import Light
from mesh import Mesh
from scene import Scene
#main graphics engine
class GraphicsEngine:
    def __init__(self, win_size=(1600, 900)):
        # init pygame
        pg.init()
        #set the windows size
        self.win_size = win_size
        # lighting
        self.light = Light()
        #sets open gl's attributes
        #setter
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        #creates a opengl Context
        pg.display.set_mode(self.win_size, flags=pg.OPENGL | pg.DOUBLEBUF)
        # provides two complete buffers for drawing both of them switch with the
        # one the was viewing with the one that was drawing
        self.ctx = mgl.create_context()
        # camera object
        self.camera = Camera(self)
        # mesh
        self.mesh = Mesh(self)


        #mouse to not run away
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        #shows proper depth
        #self.ctx.front_face = 'cw'
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        #creates a object to track frame rate
        self.clock = pg.time.Clock()
        self.delta_time = 0

        #creates scene
        self.scene = Scene(self)

        self.time = 0



    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        #clears buffer
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        #renders scene
        self.scene.render()
        #swaps buffers
        pg.display.flip()


    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(60)

if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()


