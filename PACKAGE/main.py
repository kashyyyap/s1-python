from graphics.reactangle import area as ra, perimeter as rp
from graphics.circle import area as ca, circumference as cp
from graphics.graphics_3d.cuboid import surface_area as cua, volume as cup
from graphics.graphics_3d.sphere import surface_area as sa, volume as sp

print("Rectangle area:", ra(10, 5))
print("Rectangle perimeter:", rp(10, 5))

print("\nCircle area:", ca(7))
print("Circle perimeter:", cp(7))

print("\nCuboid area:", cua(2, 3, 4))
print("Cuboid perimeter:", cup(2, 3, 4))

print("\nSphere area:", sa(5))
print("Sphere perimeter:", sp(5))