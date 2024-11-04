from vao import VAO
#from texture import Texture
#responsibility of meshes
class Mesh:
    def __init__(self, app):
        self.app = app
        self.vao = VAO(app.ctx)
   #     self.texture = Texture(app.ctx)

    def destroy(self):
        self.vao.destroy()
    #    self.texture.destroy()