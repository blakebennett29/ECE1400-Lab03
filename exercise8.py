import numpy as np
x = np.linspace(-2, 2, 100)
y = 1/(np.sqrt(2*np.pi)) * (np.exp(-x**2/(2*1**2)))
P = np.trapz(y, x)

print(P)