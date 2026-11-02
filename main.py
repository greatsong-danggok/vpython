Web VPython 3.2
rocket_body = cylinder(pos=vec(0, 0, 0), axis=vec(3, 0, 0), radius=0.5, color=color.white)
rocket_top = cone(pos=vec(3, 0, 0), axis=vec(1.5, 0, 0), radius=0.5, color=color.red)
rocket_window = sphere(pos=vec(1.5, 0, 0.6), radius=0.3, color=color.blue, opacity=0.6)

fuel_tank1 = cylinder(pos=vec(-1, 0.7, 0), axis=vec(1, 0, 0), radius=0.3, color=vec(0.6,0.6,0.6))
fuel_tank2 = cylinder(pos=vec(-1, -0.7, 0), axis=vec(1, 0, 0), radius=0.3, color=vec(0.6,0.6,0.6))

wing_left = box(pos=vec(1, 0.8, 0), size=vec(1.5, 0.1, 0.6), color=color.red)
wing_right = box(pos=vec(1, -0.8, 0), size=vec(1.5, 0.1, 0.6), color=color.red)
wing_back = box(pos=vec(1, 0, -0.8), size=vec(1.5, 0.6, 0.1), color=color.red)

rocket_bottom = sphere(pos=vec(-0.5, 0, 0), radius=0.5, color=color.orange, emissive=True)
fire = cone(pos=vec(-0.5, 0, 0), axis=vec(-1.5, 0, 0), radius=0.5, color=color.red, emissive=False)

rocket = compound([rocket_body, rocket_top, rocket_window, fuel_tank1, fuel_tank2, wing_left, wing_right, wing_back, rocket_bottom, fire])
