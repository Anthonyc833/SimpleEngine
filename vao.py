from vbo import VBO
from shader_program import ShaderProgram

#vertex abstract objects
class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        #cube vao
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo= self.vbo.vbos['cube'])

    # vertex array object
    def get_vao(self, program, vbo):  # addressed with buffer format first that attributes lastly
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attrib)])
        return vao

    # no garbage collection in OpenGL
    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()