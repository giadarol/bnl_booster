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

tw = line_thin.twiss4d()