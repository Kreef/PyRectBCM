from numpy import pi

name = "WaddenSea"

# Ocean Parameters
tideamp = 0.75
tidefreq = 2 * pi / 44712
oceandepth = 20
wavenumber = 8.2e-6

# Basin Parameters
basinwidth = 100e3
basinlength = 10e3
basindepth = 5
cd = 2.5e-3

# Inlet Parameters
inletlength = 5e3
inletdepth = 5
inletwidth = 1e3
inletshape = 0.005
numinlets = 40
ueq = 1
sedimport = 1e6

# General Parameters
timestep = 1
end = 1e3
