# Optical-properties
Python code for calculating the optical properties based on density functional theory generated from quantum espresso software.

This code calculate the following optical properties from the real and imaginary dielectric functions generate by eels.x program in qunatum espresso:
  Parallel and perpendicular polarization of real dielectric function.
  Parallel and perpendicular polarization of imaginary dielectric function.
  Parallel and perpendicular polarization of imaginary electron energy loss spectroscopy.
  Parallel and perpendicular polarization of refractive index.
  Parallel and perpendicular polarization of extinction coeficient.
  Parallel and perpendicular polarization of reflectivity coeficient.
  Parallel and perpendicular polarization of adsorption coeficient.

The files need for runig this code are:
  'epsr_pwscf.dat',
  'epsi_pwscf.dat',
  'eels_pwscf.dat',
All these files are generated from the eels.x program.

The file generated from these calculation is named 'optical_properties.dat', and the column in this file are in the follwing order
  1:Energy(eV)
  2:Parallel real dielectric function 'er_para' in (a.u.), 
  3:Perpendicular real dielectric function 'er_perp' in (a.u.),
  4:Parallel imaginary dielectric function 'ei_para' in (a.u.),
  5:Perpendicular imaginary dielectric function 'ei_perp' in (a.u.),
  6:Parallel electron energy loss spectroscopy 'eels_para' in (a.u.),
  7:Perpendicular electron energy loss spectroscopy 'eels_perp' in (a.u.),
  8:Parallel refractive index 'n_para' in (a.u.),
  9:Perpendicular refractive index 'n_perp' in (a.u.),
  10:Parallel extinction coeficient 'kapa_para' in (a.u.),
  11:Perpendicular extinction coeficient 'kapa_perp' in (a.u.),
  12:Parallel reflectivity coeficient 'R_para' in (a.u.),
  13:Perpendicular reflectivity coeficient 'R_perp' in (a.u.),
  14:Parallel adsorption coeficient 'alpha_para' in (cm^(-1)),
  15:Perpendicular adsorption coeficient 'alpha_perp' in (cm^(-1)),
