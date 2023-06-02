"""Test of qiskit"""
import numpy as np
from qiskit import QuantumCircuit
from qiskit import transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator


sim = AerSimulator()
# sim = AerSimulator(method="statevector")


circ = QuantumCircuit(2,2)

circ.h(0)
circ.cx(0,1)

circ.measure([0,1],[0,1])
# circ.measure_all(add_bits=False)

comp_circ = transpile(circ, sim)

job = sim.run(comp_circ)

result = job.result()
counts = result.get_counts()

print(counts)
print(comp_circ.draw())

plot_histogram(counts).savefig("test_hist.pdf")