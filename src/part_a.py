import numpy as np
from qiskit import QuantumCircuit
from qiskit import transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator


n_qbits = 2

# operations = [['h', 0], ['cnot', 0, 1], ['z',1]]

sim = AerSimulator()
circ = QuantumCircuit(n_qbits)

bell = []
for i in range(4):
    bell.append(QuantumCircuit(2))

for i in range(4):
    bell[i].h(0)
    bell[i].cnot(0,1)

bell[1].x(0)
bell[2].y(0)
bell[3].z(0)

for i in range(4):
    bell[i].measure_all()

print(bell[1].draw())

for i in range(4):
    comp = transpile(bell[i], sim)
    job = sim.run(comp)
    result = job.result()
    counts = result.get_counts()
    print(i, ": ", counts)

# for op in operations:
#     if op[0] == 'h':
#         circ.h(op[1])
#     elif op[0] == 'x':
#         circ.x(op[1])
#     elif op[0] == 'y':
#         circ.y(op[1])
#     elif op[0] == 'z':
#         circ.z(op[1])
#     elif op[0] == 'cnot':
#         circ.cnot(op[1],op[2])


# print(circ.draw())

# circ.measure_all()

# print(circ.draw())

# comp_circ = transpile(circ, sim)

# job = sim.run(comp_circ)

# result = job.result()
# counts = result.get_counts()

# print(counts)
# print(comp_circ.draw())

# plot_histogram(counts).savefig("part_a.pdf")