# Sinh dữ liệu cho biểu đồ slide. Chỉ dùng quy tắc giao dịch (v14, đoạn 122, 125) và công thức MDE (v15, mục 4.3.9).
from math import sqrt, floor, ceil
def hose_tick(p): return 10 if p<10000 else (50 if p<50000 else 100)
# 1) Bước giá tương đối (%) theo giá
prices=[p for p in range(1000,80001,100)]
with open('buocgia.dat','w') as f:
    f.write('gia hnx hose\n')
    for p in prices: f.write(f'{p/1000:.1f} {100*100/p:.4f} {100*hose_tick(p)/p:.4f}\n')
# 2) Lợi suất tăng tối đa ở biên độ ±7% (HOSE) và ±10% (HNX), giá trần làm tròn xuống theo bước giá
def maxret(p,band,tick): return 100*(floor(p*(1+band)/tick)*tick/p-1)
# Chỉ lấy giá hợp lệ: bội số của bước giá trên từng sàn
with open('tran.dat','w') as f:
    f.write('gia hose\n')
    for p in range(1000,20001,10):
        if p%hose_tick(p)==0: f.write(f'{p/1000:.2f} {maxret(p,0.07,hose_tick(p)):.4f}\n')
with open('tran_hnx.dat','w') as f:
    f.write('gia hnx\n')
    for p in range(1000,20001,100): f.write(f'{p/1000:.2f} {maxret(p,0.10,100):.4f}\n')
print('1140:',maxret(1140,0.07,10))
# 3) MDE theo phi, sigma=0,2, lực 80%, một phía 0,05/3
def vm(phi,n): return 1/n if phi==0 else (1/n)*((1+phi)/(1-phi)-2*phi*(1-phi**n)/(n*(1-phi)**2))
def cov(phi,pre,post,gap): return sum(phi**((pre+gap+j)-i) for i in range(pre) for j in range(post))/(pre*post) if phi else 0
k=2.12805+0.84162
with open('mde.dat','w') as f:
    f.write('phi dai ngan\n')
    for i in range(0,91):
        phi=i/100
        a=k*0.2*sqrt(vm(phi,193)+vm(phi,24)-2*cov(phi,193,24,18))
        b=k*0.2*sqrt(vm(phi,24)+vm(phi,24)-2*cov(phi,24,24,18))
        f.write(f'{phi:.2f} {a:.4f} {b:.4f}\n')
        if i in (0,60,80): print(phi,round(a,3),round(b,3),round(b/a,2))
