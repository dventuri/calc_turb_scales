import numpy as np

# Calcula o Reynolds com base no comprimento característico da geometria
def Reynolds(nu, U, L):

    Re_L = U*L/nu

    return Re_L

# Calcula o comprimento característico de Kolmogorov
def comp_caract_Kolmogorov(nu, U, L):

    eta = np.power(U/nu,-3.0/4.0)*np.power(L,1.0/4.0)

    return eta

# Calcula a microescala de Taylor
def Taylor(nu, U, L):

    eta = comp_caract_Kolmogorov(nu, U, L)
    Re_L = Reynolds(nu, U, L)
    gamma = eta*7.0*np.power(Re_L, 1.0/4.0)

    return gamma


if __name__ == "__main__":

    nu_air = 1.8448e-5/1.1843
    nu_water = 8.9002e-4/997.05

    L = 0.55
    L_air = L*0.75
    L_water = L - L_air

    U = 20.14
    U_air = U*(L**2)/(L_air**2)
    U_water = U_air/3

    # "Para se ter uma banda inercial bem definida, é necessário que
    #  L/eta > 1000. Então o microcomprimento de Taylor deve ser pelo
    #  menos 70 vezes o comprimento de Kolmogorov. Assim, o microcomprimento
    #  de Taylor estará sempre no interior da banda inercial, acima do
    #  comprimento característico de Kolmogorov e abaixo do comprimento
    #  integral."

    ### AIR
    Re = Reynolds(nu_air, U_air, L_air)
    print("Re = ", Re)

    #Kolmogorov
    eta = comp_caract_Kolmogorov(nu_air, U_air, L_air)
    print("eta = ", eta)

    #escala de Taylor
    gamma = Taylor(nu_air, U_air, L_air)
    print("gamma = ", gamma)

    print("L/eta = ", L_air/eta)
    print("gamma/eta = ", gamma/eta)
    print("")

    ### WATER
    Re = Reynolds(nu_water, U_water, L_water)
    print("Re = ", Re)

    #Kolmogorov
    eta = comp_caract_Kolmogorov(nu_water, U_water, L_water)
    print("eta = ", eta)

    #escala de Taylor
    gamma = Taylor(nu_water, U_water, L_water)
    print("gamma = ", gamma)

    print("L/eta = ", L_air/eta)
    print("gamma/eta = ", gamma/eta)
