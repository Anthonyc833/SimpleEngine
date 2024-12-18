import moderngl as mgl
import glm
import numpy as np
#responsible of any imports from regular objs to other 3d objects

# Vertices == points of a object
class BaseModel:#tex_id
    def __init__(self, app, vao_name, tex_id, pos=(0, 0, 0), rot=(0, 0, 0)):
        self.app = app
        self.pos = pos
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.m_model = self.get_model_matrix()
        self.tex_id = tex_id
        self.vao = app.mesh.vao.vaos[vao_name]
        self.program = self.vao.program
        self.camera = self.app.camera


    def update(self):
        m_model = glm.rotate(self.m_model, self.app.time, glm.vec3(0, 1, 0))
        self.shader_program['m_model'].write(m_model)
        self.shader_program['m_view'].write(self.app.camera.m_view)
        self.shader_program['camPos'].write(self.app.camera.position)

    def get_model_matrix(self):
        m_model = glm.mat4()
        m_model = glm.translate(m_model, self.pos)
        #rotations
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        return m_model

    def render(self):
        self.update()
        self.vao.render()

class Cube(BaseModel):#tex_id = 0
    def __init__(self, app, vao_name="cube", tex_id=0, pos=(0, 0, 0), rot=(0, 0, 0)):
        super().__init__(app, vao_name, tex_id, pos, rot)
        self.on_init()

    def update(self):
        #self.texture.use()
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)



    def on_init(self):
        # textures
#        self.texture = self.app.mesh.texture.textures[self.tex_id]
#        self.program['u_texture_0'] = 0
#        self.texture.use()
        #MVP
        self.program['m_proj'].write(self.app.camera.m_proj)
        self.program['m_view'].write(self.app.camera.m_view)
        self.program['m_model'].write(self.m_model)
        # lighting
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)














