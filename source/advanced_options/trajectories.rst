Virtual trajectories
====================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


MicroHH has the option to sample statistics along a pre-defined trajectory. This can be useful for comparing the model to e.g. aircraft, car, or balloon observations.

To enable the trajectories, add a :code:`[trajectory]` block to the :code:`case.ini` file:

.. code-block:: shell

    [trajectory]
    swtrajectory=1
    names=airplane,car
    sampletime=10
    variables=thl,qt,u,v,w,co2,no2

For each of the trajectories in :code:`names`, you need to provide coordinates (in meters) as a function of time (seconds since the start of the experiment). These are specified in the :code:`case_input.nc` file, with a different NetCDF group named :code:`trajectory_{name}` for each trajectory. For example:

.. code-block:: python

    import netCDF4 as nc
    nc_file = nc.Dataset('yourcase_input.nc', mode='w', datamodel='NETCDF4')

    # Initial profiles and other input...

    def add_trajectory(time, x, y, z, name):
    
        nc_group = nc_file.createGroup('trajectory_{}'.format(name));
        nc_group.createDimension('time', time.size)
    
        nc_t = nc_group.createVariable('time', float_type, ('time'))
        nc_x = nc_group.createVariable('x', float_type, ('time'))
        nc_y = nc_group.createVariable('y', float_type, ('time'))
        nc_z = nc_group.createVariable('z', float_type, ('time'))
        
        nc_t[:] = time
        nc_x[:] = x
        nc_y[:] = y
        nc_z[:] = z

    time_traj = np.array([0, 3600])
    x_traj = np.array([100, 3000])
    y_traj = np.array([200, 2000])
    z_traj = np.array([300, 1200])

    add_trajectory(time_traj, x_traj, y_traj, z_traj, 'airplane')
    
    time_traj = np.array([1800, 3600, 7200])
    x_traj = np.array([200, 3000, 6400])
    y_traj = np.array([100, 2000, 3200])
    z_traj = np.array([2,   2,    2])
    
    add_trajectory(time_traj, x_traj, y_traj, z_traj, 'car')
    
    nc_file.close()

As you can see from the second example (`car`), trajectories can start (or end) at random times in the simulation. In addition, the trajectory coordinates are allowed to be outside of the domain. In both cases, the statistics output will be set to the NetCDF fill value.

For each of the trajectories, a NetCDF file named :code:`case.trajectory_{name}.{start_time}.nc` will be produced.
