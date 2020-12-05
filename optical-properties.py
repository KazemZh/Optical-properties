import numpy as np

def get_para_perp(data):
    return data[:, 1:3].mean(axis=1), data[:, 3]

def calc_n_kapa_R_alpha(energy, er, ei):
    kapa = (1/np.sqrt(2)) * np.sqrt(-er + np.sqrt((er)**2 + (ei)**2))
    conversion = 0.000123984198405504
    alpha = 4*np.pi*kapa / (conversion/energy)
    n = (1/np.sqrt(2)) * np.sqrt(er + np.sqrt((er)**2 + (ei)**2))
    R = ((n-1)**2 + kapa**2) / ((n+1)**2 + kapa**2)
    return n, kapa, R, alpha

er = np.loadtxt('epsr_pwscf.dat')
ei = np.loadtxt('epsi_pwscf.dat')
eels = np.loadtxt('eels_pwscf.dat')

energy = er[:,0]

data = np.empty((15, len(energy)))
data[0] = energy
data[1:3] = get_para_perp(er)
data[3:5] = get_para_perp(ei)
data[5:7] = get_para_perp(eels)
data[7::2] = calc_n_kapa_R_alpha(energy, data[1], data[3])
data[8::2] = calc_n_kapa_R_alpha(energy, data[2], data[4])

header = '  '.join([
    '1:Energy(eV)', '2:er_para(a.u.)', '3:er_perp(a.u)', '4:ei_para(a.u)',
    '5:ei_perp(a.u.)', '6:eels_para(a.u.)', '7:eels_perp(a.u.)',
    '8:n_para(a.u.)', '9:n_perp(a.u.)', '10:kapa_para(a.u.)',
    '11:kapa_perp(a.u.)', '12:R_para(a.u.)', '13:R_perp(a.u.)',
    '14:alpha_para(cm^(-1))', '15:alpha_perp(cm^(-1))'
    ])

np.savetxt('optical_properties.dat', data.T, header=header, delimiter=" ", fmt="%17.5f")
