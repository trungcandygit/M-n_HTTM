import re, json
A=open('/home/user/M-n_HTTM/reports/r12-review-A.md',encoding='utf-8').read()
B=open('/home/user/M-n_HTTM/reports/r12-review-B.md',encoding='utf-8').read()
E=[]; seen=set()
def add(i,o,n):
    o=o.strip(); n=n.strip()
    if o in seen: return
    seen.add(o)
    if '[XUỐNG ĐOẠN]' in n:
        parts=n.split('[XUỐNG ĐOẠN]')
        E.append({"id":i,"op":"replace","old":o,"new":"".join(p.rstrip() if k<len(parts)-1 else p for k,p in enumerate(parts)).replace('  ',' ')})
        # split trước mỗi phần sau
        for p in parts[1:]:
            E.append({"id":i+"-sp","op":"split_before","anchor":p.strip()[:50]})
    else:
        E.append({"id":i,"op":"replace","old":o,"new":n})
meth=A.split('## (4)')[1].split('## (5)')[0]
for k,(o,n) in enumerate(re.findall(r'CHUỖI GỐC:?\s*`([^`]+)`\s*\n\s*→ CHUỖI THAY THẾ:?\s*`([^`]+)`',meth)):
    add(f"A12-M{k}",o,n)
sty=A.split('## (5)')[1].split('## (6)')[0]
for row in sty.splitlines():
    m=re.match(r'^\| (V\d+\w*) \|.*?\| `([^`]+)` \| `([^`]+)` \|\s*$',row)
    if m: add("A12-"+m.group(1),m.group(2),m.group(3))
nA=len(E)
bm=B.split('### MAJOR')[1].split('### MINOR')[0]
for o,n in re.findall(r'"(nếu cổ phiếu UPCoM được chuyển sang HOSE cùng đợt[^"]+|nên ước lượng với nhóm đối chứng UPCoM được trình bày như một cận khác\.)" → "([^"]+)"',bm):
    add("B12-MJ",o,n)
mi=B.split('### MINOR')[1].split('**Kiểm tra nhất quán')[0]
for row in mi.splitlines():
    if not row.startswith('| m'): continue
    code=row.split('|')[1].strip()
    for o,n in re.findall(r'"([^"]+)" → "([^"]+)"',row):
        add("B12-"+code,o,n)
# thuật ngữ thống nhất
for o,n in [("kiểm tra độ bền","kiểm tra độ vững"),("biến chỉ ","biến giả ")]:
    E.append({"id":"T-"+o,"op":"replace_all","old":o,"new":n})
json.dump(E,open('../r12/edits-r12.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('A',nA,'total',len(E))
