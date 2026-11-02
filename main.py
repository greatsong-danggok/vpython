Web VPython 3.2

rocket_body = cylinder(pos=vec(0, 0, 0), axis=vec(3, 0, 0), radius=0.5, color=color.white)
rocket_top = cone(pos=vec(3, 0, 0), axis=vec(1.5, 0, 0), radius=0.5, color=color.red)
rocket_window = sphere(pos=vec(1.5, 0, 0.6), radius=0.3, color=color.blue, opacity=0.6)

rocket = compound([rocket_body, rocket_top, rocket_window])
