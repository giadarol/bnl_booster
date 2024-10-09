import xtrack as xt

line = xt.Line.from_json('booster.json')

# Table, twiss and survey
tt = line.get_table(attr=True)
tw = line.twiss4d(strengths=True)
sv = line.survey()

import matplotlib.pyplot as plt
plt.close('all')
tw.plot()
sv.plot()
plt.show()





import xtrack as xt

line = xt.Line.from_json('booster.json')

line_thin = line.select() # Make a shallow copy

line_thin.slice_thick_elements(
    slicing_strategies=[
        # Slicing with thin elements
        xt.Strategy(slicing=None),
        xt.Strategy(slicing=xt.Teapot(5), element_type=xt.Bend),
        xt.Strategy(slicing=xt.Teapot(5), element_type=xt.Quadrupole),
])