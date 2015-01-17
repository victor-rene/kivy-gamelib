import copy
import math
import os

from kivy.uix.widget import Widget
from kivy.graphics import Mesh
from kivy.properties import NumericProperty


class FooBar(Widget):
    """ I got pissed off while making this widget, hence the name. """
    
    force = NumericProperty()
    
    def __init__(self, **kwargs):
        super(FooBar, self).__init__(**kwargs)
        with self.canvas:
            self.mesh = Mesh(mode='triangles', source='img/bar.png')
            self.face = Mesh(mode='triangles', source='img/foo.png')
        self.build_mesh()
        self.build_face(self.vertices)
        
    def build_face(self, mesh_vertices):
        i = 16
        self.face_vertices = []
        self.face_vertices.extend([mesh_vertices[i],    mesh_vertices[i+1],  0., 0.])
        self.face_vertices.extend([mesh_vertices[i+4],  mesh_vertices[i+5],  1., 0.])
        self.face_vertices.extend([mesh_vertices[i+16], mesh_vertices[i+17], 0., 1.])
        self.face_vertices.extend([mesh_vertices[i+20], mesh_vertices[i+21], 1., 1.])
        self.face.vertices = self.face_vertices
        self.face.indices = [0, 1, 2, 3, 2, 1]

    def build_mesh(self):
        self.vertices = []
        curr_dir = os.path.dirname(os.path.realpath(__file__))
        mesh_file = os.path.join(curr_dir, 'foobar.mesh')
        with open(mesh_file) as f:
            for line in f:
                coords = line.split(',')
                self.vertices.extend([
                    self.pos[0] + float(coords[0]) * self.width,
                    self.pos[1] + float(coords[1]) * self.height,
                    float(coords[0]), float(coords[1]) ])
                self.vertices.extend([
                    self.pos[0] + float(coords[2]) * self.width,
                    self.pos[1] + float(coords[3]) * self.height,
                    float(coords[2]), float(coords[3]) ])
                    
        self.indices = []
        for i in range(0, 19, 2):
            #1st triangle
            self.indices.append(i)
            self.indices.append(i+1)
            self.indices.append(i+2)
            # 2nd triangle
            self.indices.append(i+3)
            self.indices.append(i+2)
            self.indices.append(i+1)
            
        self.mesh.vertices = self.vertices
        self.mesh.indices = self.indices
             
    def on_force(self, *args):
        self.deformed = copy.deepcopy(self.vertices)
        n = len(self.vertices)
        for i in range(0, n, 4):
            ry = (self.vertices[i+1] - self.pos[1]) / self.height
            deform_x = math.sin(ry * math.pi)
            dx = self.force * deform_x
            deform_y = math.cos(ry * math.pi)
            dy = self.force / 2. * deform_y
            self.deformed[i] = self.vertices[i] + dx
            if (i % 8 == 0):
                if self.force > 0:
                    self.deformed[i+1] = self.vertices[i+1] + dy
                else: self.deformed[i+1] = self.vertices[i+1] + dy
            if (i % 8 == 4):
                if self.force > 0:
                    self.deformed[i+1] = self.vertices[i+1] - dy
                else: self.deformed[i+1] = self.vertices[i+1] - dy
                
        self.mesh.vertices = self.deformed
        self.build_face(self.deformed)

        