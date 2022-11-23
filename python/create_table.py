class Table:
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

"""
AAAAAAAAAAAAAAAAAAAAA
"""
advec = Table()
advec.add_row('swadvec', 'swspatialorder', [
        'Advection scheme',
        '``0``: Disabled',
        '``2``: 2nd-order',
        '``2i4``: 2nd-order (4th-order interpolation)',
        '``2i4``: 2nd-order (4th-order interpolation)',
        '``2i5``: 2nd-order (5th-order interpolation)',
        '``2i53``: 2nd-order (5th/3rd-order interpolation)',
        '``2i62``: 2nd-order (6th/2nd-order interpolation)',
        '``4``: 4th-order (DNS, high accuracy)',
        '``4m``: 2nd-order (DNS, energy conserving)'])
advec.add_row('cflmax', '1.0', 'Max. CFL for adaptive time stepping')
advec.print()

"""
BBBBBBBBBBBBBBBBBBBBB
"""
boundary = Table()
boundary.add_row('swboundary', 'None', [
        'Boundary discretization',
        '``default``: resolved boundaries',
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
        'file (``sbot_thl.0000000``) with 2D slice'])
boundary.add_row('swtimedep_sbot_2d', '0', 'Enable time varying 2D surface fields')
boundary.add_row('sbot_2d_loadtime', 'None', 'Frequency of 2D surface input')
boundary.add_row('z0m', 'None', 'Roughness length of momentum (m)')
boundary.add_row('z0h', 'None', 'Roughness length of heat (m)')
boundary.add_row('ustar', 'None', 'Value of the fixed friction velocity (m s-1)')
boundary.add_row('bulk_cm', 'None', 'Drag coefficient for momentum (-)')
boundary.add_row('bulk_cs', 'None', 'Drag coefficient for scalar (-)')
boundary.print()

budget = Table()
budget.add_row('swbudget', '0', [
        'Switch for the budget statistics',
        '``2``: Budget statistics with second-order accuracy',
        '``4``: Budget statistics with fourth-order accuracy'])
budget.print()

buffer = Table()
buffer.add_row('swbuffer', '0', [
        'Switch for the buffer layer',
        '``0``: Buffer layer disabled',
        '``1``: Buffer layer enabled'])
buffer.add_row('swupdate', '0', [
        'Switch whether to update the buffer with actual mean profiles',
        '``0``: Updating disabled',
        '``1``: Updating enabled'])
buffer.add_row('zstart', 'None', 'Height in domain at which the buffer layer starts (m)')
buffer.add_row('sigma', 'None', 'Damping frequency of buffer layer (rad s-1)')
buffer.add_row('beta', '2', 'Exponent of strength reduction function (-)')
buffer.print()

"""
CCCCCCCCCCCCCCCCCCCCC
"""
cross1 = Table()
cross1.add_row('swcross', '0', 'Switch for cross sections')
cross1.add_row('sampletime', 'None', 'Time between consecutive samples (s)')
cross1.add_row('crosslist', 'None', 'List of cross sections to be made')
cross1.add_row('xy', 'None', 'List of z-levels for xy-cross sections')
cross1.add_row('xz', 'None', 'List of y-levels for xz-cross sections')
cross1.add_row('yz', 'None', 'List of x-levels for yz-cross sections')
cross1.print()

# TO-DO: create option for two column tables.
cross2 = Table()
cross2.add_row('*', '', 'Any prognostic or diagnostic variable')
cross2.add_row('*path', '', 'Density-weighted vertical integral of any prognostic or diagnostic variable')
cross2.add_row('*bot', '', 'Bottom boundary value of any prognostic variable')
cross2.add_row('*top', '', 'Top boundary value of any prognostic variable')
cross2.add_row('*fluxbot', '', 'Bottom boundary flux of any prognostic variable')
cross2.add_row('*fluxtop', '', 'Top boundary flux of any prognostic variable')
cross2.add_row('*lngrad', '', 'Logarithm of the length of the gradient vector for any prognostic variable')
cross2.print()


