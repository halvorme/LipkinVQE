"""tut01
Tutorial 01
"""
from qiskit import QuantumCircuit
from qiskit import transpile
from qiskit.quantum_info import Statevector, Operator
from qiskit.visualization import array_to_latex
from qiskit_aer import AerSimulator
from qiskit_aer import Aer

sim = AerSimulator()
circ = QuantumCircuit(3)

circ.h(0)
circ.cx(0,1)
circ.cx(0,2)

# circ.measure_all()

# circ = transpile(circ, sim)

# job = sim.run(circ)
# result = job.result()

# print(circ.draw())
# print(result.get_counts())

state = Statevector.from_int(0, 2**3)
state = state.evolve(circ)

# print(state.draw())
img = state.draw("qsphere")
img.savefig("sphere.pdf")

U = Operator(circ)
print(U.data)

print(Aer.backends())