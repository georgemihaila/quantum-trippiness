import numpy as np
import math
import open3d as o3d
import dlib
from IPython.display import clear_output

data = np.load('circle_n0_small.npy')
print("Shape: {}".format(data.shape))
print(data[0][0])
#data = numpy.zeros(6, dtype=mesh.Mesh.dtype)

def mapFromTo(x,a,b,c,d):
   y=(x-a)/(b-a)*(d-c)+c
   return y

def num_to_rgb(val, max_val=3):
    i = (val * 255 / max_val);
    r = round(math.sin(0.024 * i + 0) * 127 + 128);
    g = round(math.sin(0.024 * i + 2) * 127 + 128);
    b = round(math.sin(0.024 * i + 4) * 127 + 128);
    return (r / 255,g / 255,b / 255)

def generate_vectors(data, layers):
    points = []
    colors = []
    print('Running...')
    for t in range(0, layers):
    
        clear_output(wait=True)
        if len(points) > 0:
            print('{}%'.format(t * 100 / layers))
        
        for x in range(0, len(data[1])):
            for y in range(0, len(data[2])):
                if data[t][x][y] != 0:
                    points.append((x, y, t * 10))
                    
                    prob = data[t][x][y]
                    #colors.append((mapFromTo(prob, min_color, max_color, 0, 255), 0, 0))
                    #colors.append((0, 255, 255))
                    colors.append(num_to_rgb(prob))
    
    return points, colors

pcd = o3d.geometry.PointCloud()
p, c = generate_vectors(data, 5)
print('Points: {}'.format(len(p)))
pcd.points = o3d.utility.Vector3dVector(p)
pcd.colors = o3d.utility.Vector3dVector(c)
o3d.visualization.draw_geometries([pcd])