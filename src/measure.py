"""measure.py
Testing how measurements work
"""
from qiskit import QuantumCircuit
from qiskit import transpile
from qiskit_aer import AerSimulator

sim = AerSimulator()

circ = QuantumCircuit(1,2)

circ.h(0)
# circ.h(0)
circ.measure(0,0)
circ.x(0)
circ.measure(0,1)

circ = transpile(circ, sim)

job = sim.run(circ)

result = job.result()


print(result.get_counts())
print(circ.draw())