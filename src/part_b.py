import numpy as np
import matplotlib.pyplot as plt

dl = 200

E_1 = 0.
E_2 = 4.
V_11 = 3.
V_12 = .2

V_22 = -V_11
V_21 = V_12

H_0 = np.diag([E_1, E_2])
H_I = np.array([[V_11, V_12],[V_21, V_22]])

lmbd = np.linspace(0, 1, dl)

H = H_0 + np.einsum('i,jk->ijk',lmbd,H_I)

eigval, eigvec = np.linalg.eig(H)

# np.einsum('i,jk->ijk',eigvec[:,0,0],eigvec[:,:,0])

if __name__ == "__main__":
    # print("Yo")
    # print(H_0)
    # print(H_I)
    # print(lmbd)
    # print(type(H))
    # print(H.shape)
    # print(H)
    # print(eigval)

    fig, ax = plt.subplots()
    ax.plot(lmbd, eigval)
    fig.savefig("eigval.pdf")

    fig2, ax2 = plt.subplots()
    ax2.plot(lmbd, eigvec[:,0,0])
    fig2.savefig("eigvec1.pdf")

    fig3, ax3 = plt.subplots()
    ax3.plot(lmbd, eigvec[:,:,1])
    fig3.savefig("eigvec2.pdf")