import matplotlib
import schemdraw
import schemdraw.flow as flow
schemdraw.config(lblofst=0)

long_arrow = 4
short_arrow = 1.5
box_size = 4
large_box_size = 6

with schemdraw.Drawing() as d:
    d.config(fontsize=6, lw=1)

    # starting question and answers
    start = flow.Start(w=box_size, h=0.5).label("Choose a simulation type")
    flow.Arrow().at(start.S).theta(-45).length(short_arrow)
    les = flow.Box(w=2, h=0.5).anchor('N').label("LES")
    flow.Arrow().at(start.N).theta(45).length(short_arrow)
    dns = flow.Box(w=2, h=0.5).anchor('S').label("DNS")

    ### LES ###
    flow.Line().down(short_arrow).at(les.S)
    advec = flow.Start(w=box_size, h=0.5).label("1. Choose an advection scheme").anchor('W')
    flow.Line().down(d.unit/1.5).at(advec.S)
    boundary = flow.Start(w=box_size, h=0.5).label("2. Choose a surface scheme")
    flow.Line().down(d.unit / 2).at(boundary.S)
    diffusion = flow.Start(w=box_size, h=0.5).label("3. Choose a diffusion scheme")
    flow.Line().down(d.unit / 2).at(diffusion.S)
    thermo = flow.Start(w=box_size, h=0.5).label("4. Choose a thermodynamics scheme")
    flow.Line().down(d.unit / 2).at(thermo.S)
    other = flow.Start(w=box_size, h=0.5).label("5. Additional options?")
    flow.Line().down(d.unit * 3.5).at(other.S)
    limiter = flow.Start(w=box_size, h=0.5).label("6. Limit scalars?")

    # advection
    flow.Arrow().right(long_arrow).at(advec.E).label("4th order interpolations", ofst=-0.1)
    advec2i4 = flow.Box(w=box_size, h=0.5).anchor('W').label("swadvec=2i4")
    advec2 = flow.Box(w=box_size, h=0.5).anchor('S').label("swadvec=2").at(advec2i4.N)
    advec2i5 = flow.Box(w=box_size, h=0.5).anchor('N').label("swadvec=2i5").at(advec2i4.S)
    advec2i62 = flow.Box(w=box_size, h=0.5).anchor('N').label("swadvec=2i62").at(advec2i5.S)

    flow.Line().at(advec.E).toy(advec2.W)
    flow.Arrow().right(long_arrow).label('basic', ofst=-0.1)
    flow.Line().at(advec.E).toy(advec2i5.W)
    flow.Arrow().right(long_arrow).label('smooth, 5th order interpolations', ofst=-0.1)
    flow.Line().at(advec.E).toy(advec2i62.W)
    flow.Arrow().right(long_arrow).label('6th/2nd order interpolations', ofst=-0.1)

    # surface
    flow.Arrow().right(long_arrow).at(boundary.E).label("interactive land surface", ofst=-0.1)
    surf_lsm = flow.Box(w=box_size, h=0.5).anchor('W').label("swboundary=surface_lsm")
    # note: surface_lsm only works with sw_thermo=moist
    surf = flow.Box(w=box_size, h=0.5).anchor('S').label("swboundary=surface").at(surf_lsm.N)
    surf_bulk = flow.Box(w=box_size, h=0.5).anchor('N').label("swboundary=surface_bulk").at(surf_lsm.S)

    flow.Line().at(boundary.E).toy(surf.W)
    flow.Arrow().right(long_arrow).label('basic', ofst=-0.1)
    flow.Line().at(boundary.E).toy(surf_bulk.W)
    flow.Arrow().right(long_arrow).label('prescribed drag coefficients', ofst=-0.1)

    # Diffusion
    flow.Arrow().right(long_arrow).at(diffusion.E).label("standard Smagorinsky", ofst=-0.1)
    dif_smag = flow.Box(w=box_size, h=0.5).anchor('W').label("swdiff=smag2")
    dif_tke = flow.Box(w=box_size, h=0.5).anchor('N').label("swdiff=tke2").at(dif_smag.S)

    flow.Line().at(diffusion.E).toy(dif_tke.W)
    flow.Arrow().right(long_arrow).label('constant TKE', ofst=-0.1)

    # thermodynamics
    flow.Arrow().right(long_arrow).at(thermo.E).label("no clouds", ofst=-0.1)
    dry = flow.Box(w=box_size, h=0.5).anchor('W').label("swthermo=dry")
    moist = flow.Box(w=box_size, h=0.5).anchor('N').label("swthermo=moist").at(dry.S)

    flow.Line().at(thermo.E).toy(moist.W)
    flow.Arrow().right(long_arrow).label('include clouds', ofst=-0.1)

    # microphysics
    flow.Arrow().length(long_arrow*1.5).at(moist.E).theta(70)
    micro = flow.Start(w=box_size, h=0.5).anchor('W').label('1. include microphysics?')

    flow.Arrow().right(short_arrow).at(micro.E).label("no", ofst=-0.1)
    no_micro = flow.Box(w=box_size, h=0.5).anchor('W').label("swmicro=0")
    incl_micro = flow.Start(w=box_size, h=0.5).anchor('N').label("include ice?").at(no_micro.S)
    flow.Line().at(micro.E).toy(incl_micro.W)
    flow.Arrow().right(short_arrow).label('yes', ofst=-0.1)

    flow.Arrow().right(short_arrow).at(incl_micro.E).label("no", ofst=-0.1)
    no_ice = flow.Box(w=box_size, h=0.5).anchor('W').label("swmicro=2mom_warm")
    incl_ice = flow.Box(w=box_size, h=0.5).anchor('N').label("swmicro=nsw6").at(no_ice.S)
    flow.Line().at(incl_micro.E).toy(incl_ice.W)
    flow.Arrow().right(short_arrow).label('yes', ofst=-0.1)

    # radiation
    flow.Line().down(d.unit / 1.5).at(micro.S)
    radiation = flow.Start(w=box_size, h=0.5).label("2. include radiation?")

    flow.Arrow().right(short_arrow).at(radiation.E).label("no", ofst=-0.1)
    no_radiation = flow.Box(w=box_size, h=0.5).anchor('W').label("swradiation=0")

    flow.Arrow().down(short_arrow).label('yes', ofst=-0.1).at(radiation.S)
    incl_radiation = flow.Start(w=box_size, h=0.5).anchor('N').label("choose radiation scheme")
    # flow.Line().at(radiation.E).toy(incl_radiation.W)

    flow.Arrow().right(long_arrow).at(incl_radiation.E).label("prescribed", ofst=-0.1)
    prescribed_radiation = flow.Box(w=box_size, h=0.5).anchor('W').label("swradiation=prescribed")
    # NOTE: technically prescribed radiation is also possible if swthermo=dry
    GCSS_radiation = flow.Box(w=box_size, h=0.5).anchor('N').label("swradiation=gcss").at(prescribed_radiation.S)
    flow.Line().at(incl_radiation.E).toy(GCSS_radiation.W)
    flow.Arrow().right(long_arrow).label('GCSS', ofst=-0.1)

    rrtmgp_radiation = flow.Box(w=box_size, h=0.5).anchor('N').label("swradiation=rrtmgp").at(GCSS_radiation.S)
    flow.Line().at(incl_radiation.E).toy(rrtmgp_radiation.W)
    flow.Arrow().right(long_arrow).label('RTE-RRTMGP', ofst=-0.1)

    rt_radiation = flow.Box(w=box_size, h=0.5).anchor('N').label("swradiation=rrtmgp_rt").at(rrtmgp_radiation.S)
    flow.Line().at(incl_radiation.E).toy(rt_radiation.W)
    flow.Arrow().right(long_arrow).label('RTE-RRTMGP with raytracer', ofst=-0.1)

    # Aerosols
    flow.Line().at(rt_radiation.E).length(short_arrow)
    flow.Line().at(rrtmgp_radiation.E).length(short_arrow)
    flow.Arrow().down(short_arrow)
    # flow.Arrow().right(short_arrow).at(rrtmgp_radiation.E)
    aerosols = flow.Start(w=box_size, h=0.5).label("include aerosols?").anchor('N')
    # flow.Arrow().at(rt_radiation.E).to(aerosols.W)

    flow.Arrow().left(short_arrow).at(aerosols.W).label("no", ofst=-0.1)
    no_aerosols = flow.Box(w=box_size, h=0.5).anchor('E').label("swaerosol=0")
    incl_aerosols = flow.Box(w=box_size, h=0.5).anchor('N').label("swaerosol=1").at(no_aerosols.S)
    flow.Line().at(aerosols.W).toy(incl_aerosols.E)
    flow.Arrow().left(short_arrow).label('yes', ofst=-0.1)

    # other options
    # Do all of these belong here or do some only belong on the DNS side of the scheme?
    flow.Line().right(short_arrow).at(other.E)
    buffer = flow.Start(w=box_size, h=0.5).label("1. include buffer layer?").anchor('W')
    flow.Arrow().right(short_arrow).at(buffer.E)
    flow.Box(w=box_size, h=0.5).anchor('W').label("set settings for buffer class")

    flow.Line().down(d.unit / 3).at(buffer.S)
    rnd = flow.Start(w=box_size, h=0.5).label("2. include initial random perturbations?").anchor('N')
    flow.Arrow().right(short_arrow).at(rnd.E)
    flow.Box(w=box_size, h=0.5).anchor('W').label("set settings for rnd in fields class")

    flow.Line().down(d.unit / 3).at(rnd.S)
    scalar = flow.Start(w=box_size, h=0.5).label("3. include passive scalars?").anchor('N')
    flow.Arrow().right(short_arrow).at(scalar.E)
    flow.Box(w=box_size, h=0.5).anchor('W').label("set slist in fields class")

    flow.Line().down(d.unit / 3).at(scalar.S)
    point = flow.Start(w=box_size, h=0.5).label("4. include point source emissions?").anchor('N')
    flow.Arrow().right(short_arrow).at(point.E)
    flow.Box(w=box_size, h=0.5).anchor('W').label("set settings in source class")

    flow.Line().down(d.unit / 3).at(point.S)
    decay = flow.Start(w=box_size, h=0.5).label("5. include exponential decay?").anchor('N')
    flow.Arrow().right(short_arrow).at(decay.E)
    flow.Box(w=box_size, h=0.5).anchor('W').label("set settings in decay class")

    flow.Line().down(d.unit / 3).at(decay.S)
    force = flow.Start(w=box_size, h=0.5).label("6. include large scale forcings?").anchor('N')
    flow.Arrow().right(short_arrow).at(force.E)
    flow.Box(w=box_size, h=0.5).anchor('W').label("set settings in force class")

    flow.Line().down(d.unit / 3).at(force.S)
    ib = flow.Start(w=box_size, h=0.5).label("7. include immersed boundaries?").anchor('N')
    flow.Arrow().right(short_arrow).at(ib.E)
    flow.Box(w=box_size, h=0.5).anchor('W').label("set settings in immersed boundaries class")

    # limiter
    flow.Arrow().right(short_arrow).at(limiter.E)
    do_limiter = flow.Box(w=box_size, h=0.5).anchor('W').label("add necessary scalars to limitlist")

    d.save("source/Tutorials/flowchart.jpeg", dpi=600)
