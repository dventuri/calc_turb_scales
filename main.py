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

    rho_gas = 2.1314776275527
    mu_gas = 9.71207824840234E-6
    nu_gas = mu_gas/rho_gas

    D_pipe = 0.320675*2
    L = D_pipe

    U = 20.14

    # "Para se ter uma banda inercial bem definida, é necessário que
    #  L/eta > 1000. Então o microcomprimento de Taylor deve ser pelo
    #  menos 70 vezes o comprimento de Kolmogorov. Assim, o microcomprimento
    #  de Taylor estará sempre no interior da banda inercial, acima do
    #  comprimento característico de Kolmogorov e abaixo do comprimento
    #  integral."

    ### Gas Cantera HCs
    Re = Reynolds(nu_gas, U, L)
    print("Re = ", Re)

    #Kolmogorov
    eta = comp_caract_Kolmogorov(nu_gas, U, L)
    print("eta = ", eta)

    #escala de Taylor
    gamma = Taylor(nu_gas, U, L)
    print("gamma = ", gamma)

    print("L/eta = ", L/eta)
    print("gamma/eta = ", gamma/eta)
    print("")
