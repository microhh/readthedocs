class Table_3col:
    def __init__(self):
        self.rows = []

    def add_row(self, label, default, desc):
        self.rows.append((label, default, desc))

    def print(self):
        # Find max row lengths
        max_label = len('Name')+2
        max_default = len('Default')+2
        max_desc = len('Description and options')+2

        for row in self.rows:
            label = row[0]
            default = row[1]
            desc = row[2]

            max_label = max(max_label, len(label)+6)
            max_default = max(max_default, len(default)+6)
            if isinstance(desc, list):
                for line in desc:
                    max_desc = max(max_desc, len(line)+4)
            else:
                max_desc = max(max_desc, len(desc)+2)

        def print_hline(marker):
            print('+'  + max_label*marker + '+' + max_default*marker + '+' + max_desc*marker + '+')

        # Print header:
        print_hline('-')

        print('| Name'    + (max_label  -5)*' ' + \
              '| Default' + (max_default-8)*' ' + \
              '| Description and options' + (max_desc-24)*' ' + '|')

        print_hline('=')

        # Print rows:
        for row in self.rows:
            label = row[0]
            default = row[1]
            desc = row[2]

            if isinstance(desc, list):
                for i,line in enumerate(desc):
                    if i==0:
                        print('| ``' + label   + '``' + (max_label  -len(label  )-5)*' ' + \
                              '| ``' + default + '``' + (max_default-len(default)-5)*' ' + \
                              '| | ' + desc[0] +        (max_desc   -len(desc[0])-3)*' ' + '|')
                    else:
                        print('|' + max_label  *' ' + \
                              '|' + max_default*' ' + \
                              '| | ' + desc[i] + (max_desc-len(desc[i])-3)* ' ' + '|')
            else:
                print('| ``' + label   + '``' + (max_label  -len(label  )-5)*' ' + \
                      '| ``' + default + '``' + (max_default-len(default)-5)*' ' + \
                      '| '   + desc           + (max_desc   -len(desc   )-1)*' ' + '|')

            print_hline('-')
        print('')


class Table_2col:
    def __init__(self):
        self.rows = []

    def add_row(self, label, desc):
        self.rows.append((label, desc))

    def print(self):
        # Find max row lengths
        max_label = len('Name')+2
        max_desc = len('Description and options')+2

        for row in self.rows:
            if len(row) == 2:
                label = row[0]
                desc = row[1]
            else:
                label = row[0]
                desc = ''

            max_label = max(max_label, len(label)+6)
            if isinstance(desc, list):
                for line in desc:
                    max_desc = max(max_desc, len(line)+4)
            else:
                max_desc = max(max_desc, len(desc)+2)

        def print_hline(marker):
            print('+'  + max_label*marker + '+' + max_desc*marker + '+')

        # Print header:
        print_hline('-')

        print('| Name'    + (max_label  -5)*' ' + \
              '| Description and options' + (max_desc-24)*' ' + '|')

        print_hline('=')

        # Print rows:
        for row in self.rows:
            label = row[0]
            desc = row[1]

            if isinstance(desc, list):
                for i,line in enumerate(desc):
                    if i==0:
                        print('| ``' + label   + '``' + (max_label  -len(label  )-5)*' ' + \
                              '| | ' + desc[0] +        (max_desc   -len(desc[0])-3)*' ' + '|')
                    else:
                        print('|' + max_label  *' ' + \
                              '| | ' + desc[i] + (max_desc-len(desc[i])-3)* ' ' + '|')
            else:
                print('| ``' + label   + '``' + (max_label  -len(label  )-5)*' ' + \
                      '| '   + desc           + (max_desc   -len(desc   )-1)*' ' + '|')

            print_hline('-')
        print('')


"""
AAAAAAAAAAAAAAAAAAAAA
"""

advec = Table_3col()
advec.add_row('swadvec', 'swspatialorder', [
        'Advection scheme',
        '``0``: Disabled',
        '``2``: 2nd-order',
        '``2i4``: 2nd-order with 4th-order interpolations',
        '``2i5``: 2nd-order with 5th-order interpolations',
        '``2i62``: 2nd-order with 6th/2nd-order interpolation',
        '``4``: 4th-order (DNS, high accuracy)',
        '``4m``: 2nd-order (DNS, energy conserving)'])
advec.add_row('cflmax', '1.0', 'Max. CFL for adaptive time stepping')
advec.add_row('fluxlimit_list', 'Empty list', 'Use flux limiter for scalars (2i5 and 2i62 only)')
advec.print()

aerosol = Table_3col()
aerosol.add_row('swaerosol', 'false', 'Switch for aerosols in radiation')
aerosol.add_row('swtimedep', 'false', 'Switch for time dependent aerosols')
aerosol.add_row('tdep_aermr{01-11}', 'swtimedep', 'Aerosol individual time depenence switches')
aerosol.print()

"""
BBBBBBBBBBBBBBBBBBBBB
"""

boundary = Table_3col()
boundary.add_row('swboundary', 'None', [
        'Boundary discretization',
        '``default``: Resolved boundaries',
        '``surface``: MOST-based surface model',
        '``surface_lsm``: MOST-based surface model with HTESSEL LSM',
        '``surface_bulk``: Surface model with prescribed drag coefficients'])
boundary.add_row('mbcbot', 'None', [
        'Bottom boundary type for momentum variables',
        '``no-slip``: Dirichlet BC with ``u = v = 0``',
        '``free-slip``: Neumann BC with ``dudz = dvdz = 0``',
        '``ustar``: Fixed ustar at bottom'])
boundary.add_row('mbctop', 'None', [
        'Top boundary type for momentum variables',
        '``no-slip``: Dirichlet BC with ``u = v = 0``',
        '``free-slip``: Neumann BC with ``dudz = dvdz = 0``'])
boundary.add_row('sbcbot', 'None', [
        'Bottom boundary type for scalar variables.',
        'Types can be specified per scalar (``sbot[thl]=flux``)',
        '``dirichlet``: Dirichlet BC',
        '``neumann``: Neumann BC',
        '``flux``: Flux BC'])
boundary.add_row('sbctop', 'None', [
        'Top boundary type for scalar variables.',
        'Types can be specified per scalar (``stop[qt]=neumann``)',
        '``dirichlet``: Dirichlet BC',
        '``neumann``: Neumann BC',
        '``flux``: Flux BC'])
boundary.add_row('ubot', '0', 'Bottom boundary value for east-west velocity (m s-1)')
boundary.add_row('utop', '0', 'Top boundary value for east-west velocity (m s-1)')
boundary.add_row('vbot', '0', 'Bottom boundary value for north-south velocity (m s-1)')
boundary.add_row('vtop', '0', 'Top boundary value for north-south velocity (m s-1)')
boundary.add_row('sbot', 'None', [
        'Bottom boundary value for scalar variables',
        'Values can be specified per scalar: ``sbot[thl]=0.1``.'])
boundary.add_row('stop', 'None', [
        'Top boundary value for scalar variables',
        'Values can be specified per scalar: ``stop[qt]=0``.'])
boundary.add_row('sbot_2d_list', 'Empty list', [
        'Comma-separate list of scalars that provide a binary',
        'file (``sbot_thl_in.0000000``) with 2D slice'])
boundary.add_row('z0m', 'None', 'Roughness length of momentum (m)')
boundary.add_row('z0h', 'None', 'Roughness length of heat (m)')
boundary.add_row('swconstantz0', 'true', [
        'Switch for spatially homogeneous z0m/z0h',
        '``true``: Homogeneous z0m/z0h, from ``.ini`` file',
        '``false``: Heterogeneous z0m/z0h from ``z0m.0000000``/``z0h.0000000``'])
boundary.add_row('swcharnock', 'false', 'Switch for Charnock parameterization (``boundary_surface`` only)')
boundary.add_row('alpha_m', 'None', 'Parameter Charnock parameterization')
boundary.add_row('alpha_ch', 'None', 'Parameter Charnock parameterization')
boundary.add_row('alpha_h', 'None', 'Parameter Charnock parameterization')
boundary.add_row('ustar', 'None', 'Value of the fixed friction velocity (m s-1)')
boundary.add_row('bulk_cm', 'None', 'Drag coefficient for momentum (-)')
boundary.add_row('bulk_cs', 'None', 'Drag coefficient for scalar (-)')
boundary.add_row('swtimedep', 'false', 'Switch for time varying surface BCs')
boundary.add_row('timedeplist', 'Empty list', 'List of scalars with time varying BCs')
boundary.add_row('swtimedep_sbot_2d', 'false', 'Switch for time varying 2D surface BCs')
boundary.add_row('sbot_2d_loadtime', 'None', 'Frequency of 2D surface BC input')
boundary.add_row('scalar_outflow', 'Empty list', 'List of scalars with non-periodic lateral BCs')
boundary.add_row('flow_direction', 'None', [
        'Flow direction used for ``scalar_outflow`` at each lateral edge',
        '``inflow``: Inflow (Dirichlet BC)',
        '``outflow``: Outflow (Neumann BC)'])
boundary.add_row('swtimedep_outflow', 'false', 'Switch for time varying scalar outflow')
boundary.print()

lsm1 = Table_3col()
lsm1.add_row('swhomogeneous', 'true', 'Use spatially homogeneous land-surface properties')
lsm1.add_row('swfreedrainage', 'true', 'Free drainage BC at bottom of soil column')
lsm1.add_row('swwater', 'false', 'Switch for allowing open water')
lsm1.add_row('swtilestats', 'false', 'Output individual tile statistics')
lsm1.add_row('swtilestats_column', 'false', 'Output individual tile column statistics')
lsm1.add_row('emis_sfc', 'None', 'Surface emissivity')
lsm1.print()

lsm2 = Table_3col()
lsm2.add_row('gD', 'None', 'gD coefficient in VDP reduction canopy resistance (?)')
lsm2.add_row('c_veg', 'None', 'Sub-grid vegetation fraction (0-1)')
lsm2.add_row('lai', 'None', 'Leaf area index (m2 m-2)')
lsm2.add_row('rs_veg_min', 'None', 'Minium canopy resistance (s m-1)')
lsm2.add_row('rs_soil_min', 'None', 'Minium soil resistance (s m-1)')
lsm2.add_row('lambda_stable', 'None', 'Skin conductivity stable conditions (W m-2 K-1)')
lsm2.add_row('lambda_unstable', 'None', 'Skin conductivity unstable conditions (W m-2 K-1)')
lsm2.add_row('cs_veg', 'None', 'Heat capacity skin layer (J K-1)')
lsm2.print()

budget = Table_3col()
budget.add_row('swbudget', '0', [
        'Switch for the budget statistics',
        '``2``: Budget statistics with second-order accuracy',
        '``4``: Budget statistics with fourth-order accuracy'])
budget.print()

buffer = Table_3col()
buffer.add_row('swbuffer', 'false', 'Switch for the buffer layer')
buffer.add_row('swupdate', 'false', 'Switch whether to update the buffer with actual mean profiles')
buffer.add_row('zstart', 'None', 'Height in domain at which the buffer layer starts (m)')
buffer.add_row('sigma', 'None', 'Damping frequency of buffer layer (rad s-1)')
buffer.add_row('beta', '2', 'Exponent of strength reduction function (-)')
buffer.print()

"""
CCCCCCCCCCCCCCCCCCCCC
"""

column = Table_3col()
column.add_row('swcolumn', 'false', 'Switch for column statistics')
column.add_row('sampletime', 'None', 'Time between consecutive samples (s)')
column.add_row('coordinates[x]', 'Empty list', 'List with x-coordinates column (m)')
column.add_row('coordinates[y]', 'Empty list', 'List with y-coordinates column (m)')
column.print()


cross = Table_3col()
cross.add_row('swcross', 'false', 'Switch for cross sections')
cross.add_row('sampletime', 'None', 'Time between consecutive samples (s)')
cross.add_row('crosslist', '[]', 'List of cross sections to be made')
cross.add_row('xy', 'None', 'List of z-levels for xy-cross sections')
cross.add_row('xz', 'None', 'List of y-levels for xz-cross sections')
cross.add_row('yz', 'None', 'List of x-levels for yz-cross sections')
cross.print()

# TO-DO: create option for two column tables.
cross = Table_2col()
cross.add_row('*_path', 'Density-weighted vertical integral of any prognostic or diagnostic variable')
cross.add_row('*_bot', 'Bottom boundary value of any prognostic variable')
cross.add_row('*_top', 'Top boundary value of any prognostic variable')
cross.add_row('*_fluxbot', 'Bottom boundary flux of any prognostic variable')
cross.add_row('*_fluxtop', 'Top boundary flux of any prognostic variable')
cross.add_row('*_lngrad', 'Logarithm of the length of the gradient vector for any prognostic variable')
cross.print()

cross = Table_2col()
cross.add_row('ustar', 'Friction velocity (m s-1)')
cross.add_row('obuk', 'Obukhov length (m)')
cross.print()

cross = Table_2col()
cross.add_row('*_fluxbot_ib', 'Bottom boundary flux of any prognostic variable at DEM surface')
cross.print()

cross = Table_2col()
cross.add_row('rr_bot', 'Surface rain rate (kg s-1) ')
cross.print()

cross = Table_2col()
cross.add_row('rg_bot', 'Surface graupel rate (kg s-1) ')
cross.add_row('rs_bot', 'Surface snow rate (kg s-1) ')
cross.print()

cross = Table_2col()
cross.add_row('sw_flux_dn', 'Downwelling shortwave radiation flux (W m-2)')
cross.add_row('sw_flux_up', 'Upwelling shortwave radiation flux (W m-2)')
cross.add_row('sw_flux_dn_dir', 'Downwelling direct shortwave radiation flux (W m-2)')
cross.add_row('lw_flux_dn', 'Downwelling longwave radiation flux (W m-2)')
cross.add_row('lw_flux_up', 'Upwelling longwave radiation flux (W m-2)')
cross.print()

cross = Table_2col()
cross.add_row('sw_flux_sfc_dir_rt', 'Surface downwellling direct shortwave radiation flux (W m-2)')
cross.add_row('sw_flux_sfc_dif_rt', 'Surface downwellling diffuse shortwave radiation flux (W m-2)')
cross.add_row('sw_flux_sfc_up_rt', 'Surface upwelling shortwave radiation flux (W m-2)')
cross.add_row('sw_flux_tod_dn_rt', 'Top of domain downwellling shortwave radiation flux (W m-2)')
cross.add_row('sw_flux_tod_up_rt', 'Top of domain upwelling shortwave radiation flux (W m-2)')
cross.print()

cross = Table_2col()
cross.add_row('sw_flux_dn_clear', 'Clear-sky downwelling shortwave radiation flux (W m-2)')
cross.add_row('sw_flux_up_clear', 'Clear-sky upwelling shortwave radiation flux (W m-2)')
cross.add_row('sw_flux_dn_dir_clear', 'Clear-sky downwelling direct shortwave radiation flux (W m-2)')
cross.add_row('lw_flux_dn_clear', 'Clear-sky downwelling longwave radiation flux (W m-2)')
cross.add_row('lw_flux_up_clear', 'Clear-sky upwelling longwave radiation flux (W m-2)')
cross.print()

cross = Table_2col()
cross.add_row('ql', 'Cloud liquid water (kg kg-1)')
cross.add_row('qi', 'Cloud ice (kg kg-1)')
cross.add_row('qlqi', 'Cloud liquid water + ice (kg kg-1)')
cross.add_row('ql_base', 'Cloud base height (m)')
cross.add_row('ql_top', 'Cloud top height (m)')
cross.add_row('ql_path', 'Density-weighted vertical integral of cloud liquid water (kg m-2)')
cross.add_row('qi_path', 'Density-weighted vertical integral of cloud ice (kg m-2)')
cross.add_row('qlqi_base', 'Cloud (water+ice) base height (m)')
cross.add_row('qlqi_top', 'Cloud (water+ice) top height (m)')
cross.add_row('qlqi_path', 'Density-weighted vertical integral of cloud water+ice (kg m-2)')
cross.add_row('qsat_path', 'Density-weighted vertical integral of saturated specific humidity (kg m-2)')
cross.add_row('w500hpa', 'Vertical velocity at the 500 hPa level (m s-1)')
cross.print()

"""
DDDDDDDDDDDDDDDDDDDDDDDDDD
"""

decay = Table_3col()
decay.add_row('swdecay', '0', [
        'Decay type:',
        '``0``: No decay',
        '``exponential``: Exponential decay',
        'Set per scalar, e.g. ``decay[s1]=0``, ``decay[s2]=exponential``'])
decay.add_row('timescale', 'None', 'Exponential decay rate (s)')
decay.add_row('nstd_couvreux', '1', 'Number of standard deviations above the horizontal mean for conditional sampling')
decay.print()

diff = Table_3col()
diff.add_row('swdiff', '0', [
        'Switch for diffusion type',
        '``0``: Disabled',
        '``2``: 2nd-order DNS',
        '``4``: 4th-order DNS',
        '``smag2``: 2nd-order Smagorinsky for LES',
        '``tke2``: 2nd-order Deardorff TKE scheme for LES',])
diff.add_row('dnmax', '0.4', 'Max. diffusion number for adaptive time stepping')
diff.print()

diff = Table_3col()
diff.add_row('cs', '0.23', 'Smagorinsky constant')
diff.add_row('tPr', '1/3', 'Turbulent Prandtl number')
diff.add_row('swmason', 'true', 'Switch for Mason wall damping')
diff.print()

diff = Table_3col()
diff.add_row('ap', '0.4', 'Contant TKE scheme (TO-DO)')
diff.add_row('cf', '2.5', 'Contant TKE scheme (TO-DO)')
diff.add_row('ce1', '0.19', 'Contant TKE scheme (TO-DO)')
diff.add_row('ce2', '0.51', 'Contant TKE scheme (TO-DO)')
diff.add_row('cm', '0.12', 'Contant TKE scheme (TO-DO)')
diff.add_row('ch1', '1', 'Contant TKE scheme (TO-DO)')
diff.add_row('ch2', '2', 'Contant TKE scheme (TO-DO)')
diff.add_row('cn', '0.76', 'Contant TKE scheme (TO-DO)')
diff.add_row('swmason', 'true', 'Switch for Mason wall damping')
diff.print()


dump = Table_3col()
dump.add_row('swdump', 'false', 'Switch for 3D field dumps')
dump.add_row('swdoubledump', 'false', 'Switch for dump at two consecutive model iterations')
dump.add_row('sampletime', 'None', 'Time between consecutive samples (s)')
dump.add_row('dumplist', 'Empty list', 'List of 3D dumps to be made')
dump.print()

dump = Table_2col()
dump.add_row('ql', 'Cloud liquid water (kg kg-1)')
dump.add_row('qi', 'Cloud ice (kg kg-1)')
dump.add_row('T', 'Absolute temperature (K)')
dump.print()

"""
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
"""

fields = Table_3col()
fields.add_row('slist', 'Empty list', 'List of passive scalars to be initialized')
fields.add_row('visc', 'None', 'Kinematic viscosity (m2 s-1)')
fields.add_row('svisc', 'None', 'Diffusivity of scalars (m2 s-1)')
fields.add_row('rndseed', '0', 'Seed of random number generator (-)')
fields.add_row('rndamp', '0', [
    'Amplitude of perturbations. Value can be specified per',
    'prognostic variable, for instance ``rndamp[s] = 0.1``'])
fields.add_row('rndz', '0', 'Height until which perturbations applied (m)')
fields.add_row('rndexp', '0', 'Decay of perturbation amplitude with height')
fields.add_row('vortexnpair', '0', 'Number of pairs of counter rotating vortices (-)')
fields.add_row('vortexamp', '0', 'Maximum vortex velocity (m s-1)')
fields.add_row('vortexaxis', 'y', [
        'Orientation of axis vortices',
        '``x``: Rotation of vortices in xz-plane',
        '``y``: Rotation of vortices in yz-plane'])
fields.print()


force = Table_3col()
force.add_row('swlspres', '0', [
        'Switch for large-scale pressure force',
        '``geo``: Fixed pressure gradient in x-direction',
        '``dpdx``: Rotation of vortices in yz-plane',
        '``uflux``: ixed volume flux through domain'])

force.add_row('fc', 'None', 'Coriolis parameter (s-1) (if ``swlspres=geo``)')
force.add_row('dpdx', 'None', 'Fixed pressure gradient in x (Pa m-1) (if ``swlspres=dpdx``)')
force.add_row('uflux', 'None', 'Fixed volume-mean velocity (m s-1) (if ``swlspres=uflux``)')
force.add_row('swtimedep_geo', 'false', 'Switch for time dependent geostrophic wind')

force.add_row('swls', 'false', 'Switch for large-scale advective tendencies')
force.add_row('lslist', 'Empty list', 'List of variables for which advective tendencies are given')
force.add_row('swtimedep_ls', 'false', 'Switch for time-dependent advective tendencies')
force.add_row('timedeplist_ls', 'Empty list', 'List of scalars with time-dependent advective tendencies')

force.add_row('swwls', 'false', 'Switch for large-scale subsidence (scalars)')
force.add_row('swwls_mom', 'false', 'Switch for large-scale subsidence (momentum)')
force.add_row('swtimedep_wls', 'false', 'Switch for time dependent subsidence')

force.add_row('swnudge', 'false', 'Switch for nudging')
force.add_row('nudgelist', 'Empty list', 'List of variables to which nudging is applied')
force.add_row('scalednudgelist', 'Empty list', 'List of variables to which a nudging scale is applied')
force.add_row('swtimedep_nudge', 'false', 'Switch for time-dependent nudging')
force.add_row('timedeplist_nudge', 'Empty list', 'List of variables with time-dependent nudging')
force.print()




