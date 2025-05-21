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
    # start = flow.Start(w=box_size, h=0.5).label("Choose a simulation type")
    # flow.Arrow().at(start.S).theta(-45).length(short_arrow)
    # les = flow.Box(w=2, h=0.5).anchor('N').label("LES")
    # flow.Arrow().at(start.S).theta(-135).length(short_arrow)
    # dns = flow.Box(w=2, h=0.5).anchor('N').label("DNS")

    ### LES ###
    # flow.Line().down(short_arrow).at(les.S)
    start = flow.Start(w=box_size, h=0.5).label("Setup your LES")
    flow.Arrow().at(start.S).length(short_arrow)
    dynamics = flow.Start(w=box_size, h=0.5).label("1. Setup the model dynamics").anchor('N')
    flow.Line().down(d.unit / 0.5).at(dynamics.S)
    physics = flow.Start(w=box_size, h=0.5).label("2. Add relevant physics")
    flow.Line().down(d.unit / 0.5).at(physics.S)
    other = flow.Start(w=box_size, h=0.5).label("3. Add scalars")
    flow.Line().down(d.unit / 1.5).at(other.S)
    limiter = flow.Start(w=box_size, h=0.5).label("4. Add Limiter")

    # dynamics
    flow.Arrow().right(short_arrow * 0.5).at(dynamics.E)
    advec = flow.Start(w=box_size, h=0.5).label("1. Choose an advection scheme").anchor('W')
    flow.Line().down(d.unit / 3).at(advec.S)
    diffusion = flow.Start(w=box_size, h=0.5).label("2. Choose a diffusion scheme")
    flow.Line().down(d.unit / 3).at(diffusion.S)
    thermo = flow.Start(w=box_size, h=0.5).label("3. Set up thermodynamics")
    flow.Line().down(d.unit / 5).at(thermo.S)
    buffer = flow.Start(w=box_size, h=0.5).label("4. Set up buffer layer")
    flow.Line().down(d.unit / 5).at(buffer.S)
    random = flow.Start(w=box_size, h=0.5).label("5. Set up initial random perturbations")

    # advection
    flow.Arrow().right(long_arrow).at(advec.E).label("including hyperdiffusion", ofst=-0.1)
    advec2i5 = flow.Box(w=box_size, h=0.5).anchor('W').label("swadvec=2i5")
    advec2 = flow.Box(w=box_size, h=0.5).anchor('S').label("swadvec=2").at(advec2i5.N)
    advec2i62 = flow.Box(w=box_size, h=0.5).anchor('N').label("swadvec=2i62").at(advec2i5.S)
    flow.Line().at(advec.E).toy(advec2.W)
    flow.Arrow().right(long_arrow).label('basic', ofst=-0.1)
    flow.Line().at(advec.E).toy(advec2i62.W)
    flow.Arrow().right(long_arrow).label('higher order accuracy', ofst=-0.1)

    # Diffusion
    flow.Arrow().right(long_arrow).at(diffusion.E).label("standard Smagorinsky", ofst=-0.1)
    dif_smag = flow.Box(w=box_size, h=0.5).anchor('W').label("swdiff=smag2")
    dif_tke = flow.Box(w=box_size, h=0.5).anchor('N').label("swdiff=tke2").at(dif_smag.S)
    flow.Line().at(diffusion.E).toy(dif_tke.W)
    flow.Arrow().right(long_arrow).label('constant TKE', ofst=-0.1)

    # thermodynamics
    flow.Line().right(long_arrow * 1.6).at(thermo.E)
    clouds = flow.Start(w=box_size, h=0.5).label("1. include clouds?").anchor('W')
    flow.Arrow().right(short_arrow).at(clouds.E).label("no", ofst=-0.1)
    dry = flow.Box(w=box_size, h=0.5).anchor('W').label("swthermo=dry")
    moist = flow.Box(w=box_size, h=0.5).anchor('N').label("swthermo=moist").at(dry.S)
    flow.Line().at(clouds.E).toy(moist.W)
    flow.Arrow().right(short_arrow).label('yes', ofst=-0.1)

    flow.Line().down(d.unit / 3).at(clouds.S)
    density = flow.Start(w=box_size, h=0.5).label("2. density = 1 ?").anchor('N')
    flow.Arrow().right(short_arrow).at(density.E).label("no", ofst=-0.1)
    anelastic = flow.Box(w=box_size, h=0.5).anchor('W').label("swbasestae=anelastic")
    boussinesq = flow.Box(w=box_size, h=0.5).anchor('N').label("swbasestae=boussinesq").at(anelastic.S)
    flow.Line().at(density.E).toy(boussinesq.W)
    flow.Arrow().right(short_arrow).label('yes', ofst=-0.1)

    # buffer
    flow.Arrow().right(short_arrow).at(buffer.E)
    flow.Box(w=box_size, h=0.5).anchor('W').label("set strength and height for buffer")

    # random peturbations
    flow.Arrow().right(short_arrow).at(random.E)
    flow.Box(w=box_size, h=0.5).anchor('W').label("set settings for rnd in fields class")

    # physics
    flow.Arrow().length(short_arrow * 0.5).at(physics.E)
    micro = flow.Start(w=box_size, h=0.5).label("1. include microphysics?").anchor('W')
    flow.Line().down(d.unit / 3).at(micro.S)
    radiation = flow.Start(w=box_size, h=0.5).label("2. include radiation?")
    flow.Line().down(d.unit / 2).at(radiation.S)
    surface = flow.Start(w=box_size, h=0.5).label("3. include interactive land surface?")
    flow.Line().down(d.unit / 3).at(surface.S)
    forcings = flow.Start(w=box_size, h=0.5).label("4. include large scale forcings?")

    # microphysics
    flow.Arrow().right(short_arrow).at(micro.E).label("no", ofst=-0.1)
    no_micro = flow.Box(w=box_size, h=0.5).anchor('W').label("swmicro=0")
    incl_micro = flow.Start(w=box_size, h=0.5).anchor('N').label("predict number concentrations?").at(no_micro.S)
    flow.Line().at(micro.E).toy(incl_micro.W)
    flow.Arrow().right(short_arrow).label('yes', ofst=-0.1)

    flow.Arrow().right(short_arrow).at(incl_micro.E).label("yes", ofst=-0.1)
    double = flow.Box(w=box_size, h=0.5).anchor('W').label("swmicro=2mom_warm")
    single = flow.Box(w=box_size, h=0.5).anchor('N').label("swmicro=nsw6").at(double.S)
    flow.Line().at(incl_micro.E).toy(single.W)
    flow.Arrow().right(short_arrow).label('no', ofst=-0.1)

    # radiation
    flow.Arrow().right(short_arrow).at(radiation.E).label("no", ofst=-0.1)
    no_radiation = flow.Box(w=box_size, h=0.5).anchor('W').label("swradiation=0")
    incl_radiation = flow.Start(w=box_size, h=0.5).anchor('N').label("choose radiation scheme").at(no_radiation.S)
    flow.Line().at(radiation.E).toy(incl_radiation.W)
    flow.Arrow().right(short_arrow).label('yes', ofst=-0.1)

    flow.Arrow().right(long_arrow).at(incl_radiation.E).label("prescribed", ofst=-0.1)
    prescribed_radiation = flow.Box(w=box_size, h=0.5).anchor('W').label("swradiation=prescribed")

    rrtmgp_radiation = flow.Box(w=box_size, h=0.5).anchor('N').label("swradiation=rrtmgp").at(prescribed_radiation.S)
    flow.Line().at(incl_radiation.E).toy(rrtmgp_radiation.W)
    flow.Arrow().right(long_arrow).label('RTE-RRTMGP', ofst=-0.1)

    rt_radiation = flow.Box(w=box_size, h=0.5).anchor('N').label("swradiation=rrtmgp_rt").at(rrtmgp_radiation.S)
    flow.Line().at(incl_radiation.E).toy(rt_radiation.W)
    flow.Arrow().right(long_arrow).label('RTE-RRTMGP with raytracer', ofst=-0.1)

    # Aerosols
    flow.Line().at(rt_radiation.E).length(short_arrow * 0.5)
    flow.Line().at(rrtmgp_radiation.E).length(short_arrow * 0.5)
    flow.Arrow().down(short_arrow)
    aerosols = flow.Start(w=box_size, h=0.5).label("include aerosols?").anchor('N')

    flow.Arrow().left(short_arrow).at(aerosols.W).label("no", ofst=-0.1)
    no_aerosols = flow.Box(w=box_size, h=0.5).anchor('E').label("swaerosol=0")
    incl_aerosols = flow.Box(w=box_size, h=0.5).anchor('N').label("swaerosol=1").at(no_aerosols.S)
    flow.Line().at(aerosols.W).toy(incl_aerosols.W)
    flow.Arrow().left(short_arrow).label('yes', ofst=-0.1)

    # surface
    flow.Arrow().right(short_arrow).at(surface.E).label("yes", ofst=-0.1)
    surf_lsm = flow.Box(w=box_size, h=0.5).anchor('W').label("swboundary=surface_lsm")
    surf = flow.Box(w=box_size, h=0.5).anchor('N').label("swboundary=surface").at(surf_lsm.S)
    flow.Line().at(surface.E).toy(surf.W)
    flow.Arrow().right(short_arrow).label('no', ofst=-0.1)

    # large scale forcing
    flow.Arrow().right(short_arrow).at(forcings.E)
    flow.Box(w=box_size, h=0.5).anchor('W').label("set settings in force class")

    # additional options
    flow.Arrow().length(short_arrow * 0.5).at(other.E)
    scalar = flow.Start(w=box_size, h=0.5).label("1. include passive scalars?").anchor('W')
    flow.Arrow().down(short_arrow * 0.5).at(scalar.S)
    flow.Box(w=box_size, h=0.5).anchor('N').label("set slist in fields class")

    flow.Line().right(d.unit / 5).at(scalar.E)
    point = flow.Start(w=box_size, h=0.5).label("2. include point source emissions?").anchor('W')
    flow.Arrow().down(short_arrow * 0.5).at(point.S)
    flow.Box(w=box_size, h=0.5).anchor('N').label("check out options in source class")

    flow.Line().right(d.unit / 5).at(point.E)
    decay = flow.Start(w=box_size, h=0.5).label("3. include exponential decay?").anchor('W')
    flow.Arrow().down(short_arrow * 0.5).at(decay.S)
    flow.Box(w=box_size, h=0.5).anchor('N').label("check out options in decay class")

    # limiter
    flow.Arrow().right(short_arrow*0.5).at(limiter.E)
    do_limiter = flow.Box(w=box_size, h=0.5).anchor('W').label("add necessary scalars to limitlist")

    d.save("figures/flowchart.jpeg", dpi=600)
