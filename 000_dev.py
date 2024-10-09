from cpymad.madx import Madx
import xtrack as xt

mad = Madx()
mad.call('booster.run')

line = xt.Line.from_madx_sequence(mad.sequence.booster, deferred_expressions=True)
line.particle_ref = xt.Particles(mass0=xt.PROTON_MASS_EV,
                                 gamma0=mad.sequence.booster.beam.gamma)

line.to_json('booster.json')