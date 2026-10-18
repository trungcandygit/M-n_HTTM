# Sinh chuỗi MINH HỌA cho hinh/did.tex (hàm tất định, không phải dữ liệu)
import math
def noise(k,seed): return 0.035*math.sin(1.7*k+seed)+0.02*math.sin(0.63*k+2*seed)
T=[2024+k/12 for k in range(61)]
def tr(t,k): return (1.05 if t<2027 else 0.75)-0.02*(t-2024)+noise(k,0.3)
def co(t,k): return 0.55-0.02*(t-2024)+noise(k,1.9)
with open('did.dat','w') as f:
    f.write('t chuyen doichung\n')
    for k,t in enumerate(T): f.write(f'{t:.4f} {tr(t,k):.4f} {co(t,k):.4f}\n')
