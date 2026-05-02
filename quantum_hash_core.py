import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import Aer  # Aer artık buradan geliyor
from qiskit.visualization import plot_histogram

def create_spin_chaos_block(input_data):
    n_qubits = 4
    # 4 kübit ve 4 klasik bitlik devre
    qc = QuantumCircuit(n_qubits, n_qubits)

    # 1. Süperpozisyon (Geçmişle bağını kopar)
    for i in range(n_qubits):
        qc.h(i)

    # 2. Spin Açıları
    angle = (input_data % 256) * (np.pi / 128)
    for i in range(n_qubits):
        qc.ry(angle, i)

    # 3. Dolanıklık (Kaos Katmanı)
    for i in range(n_qubits - 1):
        qc.cx(i, i + 1)
    qc.cx(n_qubits - 1, 0)

    # 4. Ölçüm
    qc.measure(range(n_qubits), range(n_qubits))
    
    return qc

# Test Edelim
test_data = 155 
circuit = create_spin_chaos_block(test_data)

# Yeni Qiskit 1.0+ yöntemiyle simülasyon
backend = Aer.get_backend('qasm_simulator')
# 'execute' yerine 'backend.run' kullanıyoruz
job = backend.run(circuit, shots=1) 
result = job.result().get_counts()

print(f"Girdi: {test_data} -> Kuantum Hash Çıktısı (Binary): {list(result.keys())[0]}")
print("\nKuantum Devre Şeması:")
print(circuit.draw(output='text'))
