import matplotlib
import schemdraw
import schemdraw.flow as flow
schemdraw.config(lblofst=0)

long_arrow = 5
short_arrow = 1.5
box_size = 4

with schemdraw.Drawing() as d:
    d.config(fontsize=6, lw=1)

    # starting question and answers
    start = flow.Start(w=box_size, h=0.5).label("Choose a simulation type")
    flow.Arrow().at(start.E).theta(-45).length(short_arrow)
    les = flow.Box(w=2, h=0.5).anchor('N').label("LES")
    flow.Arrow().at(start.E).theta(45).length(short_arrow)
    dns = flow.Box(w=2, h=0.5).anchor('S').label("DNS")

    ### LES ###
    flow.Line().right(d.unit/2).at(les.E)
    advec = flow.Start(w=5, h=0.5).label("1. Choose an advection scheme").anchor('W')
    flow.Line().down(d.unit/1.5).at(advec.S)
    boundary = flow.Start(w=5, h=0.5).label("2. Choose a surface scheme")
    flow.Line().down(d.unit / 2).at(boundary.S)
    diffusion = flow.Start(w=5, h=0.5).label("3. Choose a diffusion scheme")
    flow.Line().down(d.unit / 2).at(diffusion.S)
    thermo = flow.Start(w=5, h=0.5).label("4. Choose a thermodynamics scheme")
    flow.Line().down(d.unit / 2).at(thermo.S)
    other = flow.Start(w=5, h=0.5).label("5. Additional options?")
    flow.Line().down(d.unit / 2).at(other.S)
    limiter = flow.Start(w=5, h=0.5).label("6. Limit scalars?")

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
    flow.Arrow().length(long_arrow).at(moist.E).theta(60)
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
    incl_radiation = flow.Start(w=box_size, h=0.5).anchor('N').label("choose radiation scheme").at(no_radiation.S)
    flow.Line().at(radiation.E).toy(incl_radiation.W)
    flow.Arrow().right(short_arrow).label('yes', ofst=-0.1)

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
    flow.Arrow().right(short_arrow).at(rrtmgp_radiation.E)
    aerosols = flow.Start(w=box_size, h=0.5).label("include aerosols?").anchor('W')
    flow.Arrow().at(rt_radiation.E).to(aerosols.W)

    flow.Arrow().right(short_arrow).at(aerosols.E).label("no", ofst=-0.1)
    no_aerosols = flow.Box(w=box_size, h=0.5).anchor('W').label("swaerosol=0")
    incl_aerosols = flow.Box(w=box_size, h=0.5).anchor('N').label("swaerosol=1").at(no_aerosols.S)
    flow.Line().at(aerosols.E).toy(incl_aerosols.W)
    flow.Arrow().right(short_arrow).label('yes', ofst=-0.1)

    # other options

    # limiter
    flow.Arrow().right(short_arrow).at(limiter.E).label("yes")
    do_limiter = flow.Box(w=6, h=0.5).anchor('W').label("add necessary scalars to limitlist")

    d.save("source/Tutorials/flowchart.jpeg", dpi=300)
