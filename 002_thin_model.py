import xtrack as xt

line = xt.Line.from_json('booster.json')

line_thin = line.select() # Make a shallow copy

line_thin.slice_thick_elements(
    slicing_strategies=[
        # Slicing with thin elements
        xt.Strategy(slicing=None),
        xt.Strategy(slicing=xt.Teapot(10), element_type=xt.Bend),
        xt.Strategy(slicing=xt.Teapot(10), element_type=xt.Quadrupole),
])

line['dhcc8'].knl[0] = 1e-4 # Add a horizontal kick
line['dhcc8'].ksl[0] = 1e-4 # Add a vertical kick

tw = line_thin.twiss4d()

# To get the refernce trajectory rotation angle
tt = line.get_table(attr=True)
tt.cols['angle_rad']

import matplotlib.pyplot as plt
plt.close('all')
plt.figure()
plt.plot(tw.s, tw.x, label='x')
plt.plot(tw.s, tw.y, label='y')

plt.show()