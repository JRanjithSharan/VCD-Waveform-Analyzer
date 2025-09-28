from vcdvcd import VCDVCD
import matplotlib.pyplot as plt

vcd = VCDVCD(r"C:\\Users\\RANJITH\\Documents\\Vivado\\8_bit_ALU\\alu_8bit.vcd")

print(vcd)
print("Signals found in VCD:")
for sig in vcd.signals:
    print(f" - {sig}")

# === Step 2: Choose signals to plot ===
# Adjust these names depending on what you saw above
signals_to_plot = ["alu_8bit_tb.A[7:0]","alu_8bit_tb.B[7:0]","alu_8bit_tb.ALU_sel[3:0]","alu_8bit_tb.ALU_result[7:0]"]

# === Step 3: Plot waveforms ===
plt.figure(figsize=(12, 8))

for i, sig in enumerate(signals_to_plot):
    times = [t for t, _ in vcd[sig].tv]  # time points
    values = []
    for _, v in vcd[sig].tv:
        if v in ("x", "z"):   # unknown/high-impedance
            values.append(0)
        else:
            # Convert binary string to integer if needed
            values.append(int(v, 2) if isinstance(v, str) else int(v))

    # Offset each signal vertically so they don’t overlap
    offset = i * (max(values) + 2)
    plt.step(times, [val + offset for val in values],
             where="post", label=sig)

plt.xlabel("Time (ns)")
plt.ylabel("Signal values (with offsets)")
plt.title("8-bit ALU Waveform Analysis")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()