from lsst.fgcmcal import Sedterm, Sedboundaryterm

# Mapping from bands to SED boundary term names used is sedterms.
config.sedboundaryterms.data = {'gr': Sedboundaryterm(primary='g', secondary='r'),
                                'ri': Sedboundaryterm(primary='r', secondary='i'),
                                'iz': Sedboundaryterm(primary='i', secondary='z'),
                                'zy': Sedboundaryterm(primary='z', secondary='y'),
                                'N921z': Sedboundaryterm(primary='N921', secondary='z')}
# Mapping from terms to bands for fgcm linear SED approximations.
config.sedterms.data = {'g': Sedterm(primaryTerm='gr', secondaryTerm='ri', constant=1.6),
                        'r': Sedterm(primaryTerm='gr', secondaryTerm='ri', constant=0.9),
                        'i': Sedterm(primaryTerm='ri', secondaryTerm='iz', constant=1.0),
                        'z': Sedterm(primaryTerm='iz', secondaryTerm='zy', constant=1.0),
                        'y': Sedterm(primaryTerm='zy', secondaryTerm='iz', constant=0.25,
                                     extrapolated=True, primaryBand='y', secondaryBand='z',
                                     tertiaryBand='i'),
                        'N921': Sedterm(primaryTerm='N921z', constant=0.5)}
