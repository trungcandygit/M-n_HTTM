# Sinh chuỗi MINH HỌA cho hinh/did.tex (hàm tất định, không phải dữ liệu)
import math
def noise(k,s): return 0.016*math.sin(1.31*k+s)+0.011*math.sin(0.47*k+2.1*s)+0.007*math.sin(2.93*k+0.7*s)
T=[2024+k/12 for k in range(61)]
with open('did.dat','w') as f, open('did_sau.dat','w') as g:
    f.write('t chuyen doichung\n'); g.write('t chuyen\n')
    for k,t in enumerate(T):
        c=0.55-0.02*(t-2024)+noise(k,1.9)
        if t<=2027: f.write(f'{t:.4f} {1.05-0.02*(t-2024)+noise(k,0.3):.4f} {c:.4f}\n')
        else: f.write(f'{t:.4f} nan {c:.4f}\n')
        if t>=2027: g.write(f'{t:.4f} {0.75-0.02*(t-2024)+noise(k,0.3):.4f}\n')
