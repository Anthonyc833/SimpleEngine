import numpy as np
import moderngl as mgl

#Vertex Buffer Objects
class VBO:
    def __init__(self, ctx):
        self.vbos = {}
        self.vbos['cube'] = CubeVBO(ctx)

    def destroy(self):
        [vbo.destroy() for vbo in self.vbos.values()]

        
class BaseVBO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = self.get_vbo()
        self.format: str = None
        self.attrib : list = None

    def get_vertex_data(self):
            vertices = [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
                        (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, 1, -1), ]

            indices = [(0, 2, 3), (0, 1, 2),
                       (1, 7, 2), (1, 6, 7),
                       (6, 5, 4), (4, 7, 6),
                       (3, 4, 5), (3, 5, 0),
                       (3, 7, 4), (3, 2, 7),
                       (0, 6, 1), (0, 5, 6)]

            vertex_data = self.get_data(vertices, indices)

            tex_coord = [(0, 0), (1, 0), (1, 1), (0, 1)]
            tex_coord_indices = [(0, 2, 3), (0, 1, 2),
                                 (0, 2, 3), (0, 1, 2),
                                 (0, 1, 2), (2, 3, 0),
                                 (2, 3, 0), (2, 0, 1),
                                 (0, 2, 3), (0, 1, 2),
                                 (3, 2, 1), (3, 0, 1), ]

            tex_coord_data = self.get_data(tex_coord, tex_coord_indices)
            # points poiniting away from the cube
            normals = [(0, 0, 1) * 6,
                       (1, 0, 0) * 6,
                       (0, 0, -1) * 6,
                       (-1, 0, 0) * 6,
                       (0, 1, 0) * 6,
                       (0, -1, 0) * 6, ]
            normals = np.array(normals, dtype='f4').reshape(36, 3)

            vertex_data = np.hstack([normals, vertex_data])
            vertex_data = np.hstack([tex_coord_data, vertex_data])

            # vertex_data = np.array(vertex_data, dtype='f4')

            return vertex_data

    # sends to gpu
    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo

    def destroy(self):
        self.vbo.release()

class CubeVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attrib = ['in_texcoord_0', 'in_normal', 'in_position']

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vertex_data(self):
        vertices = [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, 1, -1), ]

        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]

        vertex_data = self.get_data(vertices, indices)

        tex_coord = [(0, 0), (1, 0), (1, 1), (0, 1)]
        tex_coord_indices = [(0, 2, 3), (0, 1, 2),
                             (0, 2, 3), (0, 1, 2),
                             (0, 1, 2), (2, 3, 0),
                             (2, 3, 0), (2, 0, 1),
                             (0, 2, 3), (0, 1, 2),
                             (3, 2, 1), (3, 0, 1), ]

        tex_coord_data = self.get_data(tex_coord, tex_coord_indices)
        # points poiniting away from the cube
        normals = [(0, 0, 1) * 6,
                   (1, 0, 0) * 6,
                   (0, 0, -1) * 6,
                   (-1, 0, 0) * 6,
                   (0, 1, 0) * 6,
                   (0, -1, 0) * 6, ]
        normals = np.array(normals, dtype='f4').reshape(36, 3)

        vertex_data = np.hstack([normals, vertex_data])
        vertex_data = np.hstack([tex_coord_data, vertex_data])

        # vertex_data = np.array(vertex_data, dtype='f4')

        return vertex_data