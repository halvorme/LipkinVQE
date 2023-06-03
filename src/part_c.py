from qiskit.quantum_info import SparsePauliOp
from qiskit.algorithms.minimum_eigensolvers import VQE
from qiskit_aer.primitives import Estimator
from qiskit.circuit.library import TwoLocal
from qiskit.algorithms.optimizers import GradientDescent, ADAM, SLSQP

n_qbits = 1

E_1 = 0.
E_2 = 4.
V_11 = 3.
V_12 = .2

V_22 = -V_11
V_21 = V_12

Eps = .5*(E_1+E_2)
Sgm = .5*(E_1-E_2)
c = .5*(V_11+V_22)
omg_z = .5*(V_11-V_22)
omg_x = V_12

H_0 = SparsePauliOp(['I','Z'], coeffs=[Eps,Sgm])
H_I = SparsePauliOp(['I','Z','X'], coeffs=[c, omg_z, omg_x])

print(H_0.to_operator())
print(H_I.to_operator())


def solve_vqe(H, n_qbits):
    estimator = Estimator()
    # optimizer = GradientDescent()
    optimizer = SLSQP(maxiter=1000)
    ansatz = TwoLocal(n_qbits, "ry", "cz")

    vqe = VQE(estimator, ansatz, optimizer)

    result = vqe.compute_minimum_eigenvalue(H)

    return result

H = H_0 + H_I

print(solve_vqe(H, n_qbits))