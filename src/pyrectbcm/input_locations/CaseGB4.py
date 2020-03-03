from numpy import pi

name = "GeorgiaBight"

# Ocean Parameters
tideamp = 1.25
tidefreq = 2 * pi / 44712
oceandepth = 30
wavenumber = 0

# Basin Parameters
basinwidth = 100e3
basinlength = 2e3
basindepth = 2
cd = 2.5e-3

# Inlet Parameters
inletlength = 1e3
inletdepth = 2
inletwidth = 0.4e3
inletshape = 0.005
numinlets = 40
ueq = 1
sedimport = 1e5

# General Parameters
timestep = 0.5
end = 1e3
