import taichi as tc
import colorsys
import random

def create_scene():
  camera = tc.Camera(
      'pinhole',
      res=(960, 540),
      fov=20,
      origin=(0, 0, 30),
      look_at=(0, 0, 0),
      up=(0, 1, 0))

  scene = tc.Scene()

  with scene:
    scene.set_camera(camera)

    texture = (tc.Texture('perlin') + 1).fract()

    mesh = tc.Mesh(
        'plane',
        tc.SurfaceMaterial('diffuse', color_map=texture),
        translate=(0, 0, -0.05),
        scale=10,
        rotation=(90, 0, 0))
    scene.add_mesh(mesh)

    mesh = tc.Mesh(
        'plane',
        tc.SurfaceMaterial('diffuse', color=(0.1, 0.08, 0.08)),
        translate=(-10, 0, 0),
        scale=10,
        rotation=(0, 0, 90))
    scene.add_mesh(mesh)

    mesh = tc.Mesh(
        'plane',
        tc.SurfaceMaterial('emissive', color=(1, 1, 1)),
        translate=(10, 0, 1),
        scale=0.3,
        rotation=(0, 0, 90))
    scene.add_mesh(mesh)

    for i in range(30):
      s = 4
      scale = random.random() * 0.03 + 0.1
      rgb = colorsys.hls_to_rgb(random.random(), 0.6, 0.8)
      x, y = random.random() - 0.5, random.random() - 0.5
      mesh = tc.Mesh(
          'sphere',
          tc.SurfaceMaterial('pbr', diffuse=rgb, specular=rgb, glossiness=4),
          translate=(x * s, y * s, 0),
          scale=scale)
      scene.add_mesh(mesh)

  return scene


if __name__ == '__main__':
  renderer = tc.Renderer(scene=create_scene())
  renderer.render()
  
