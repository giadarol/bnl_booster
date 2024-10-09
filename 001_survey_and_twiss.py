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
