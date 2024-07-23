import yaml

with open('./profile.txt', 'r') as f:
    data = [round(int(d.split(',')[0])*8/30000,4) for d in f.readlines()]
print(data)
with open('./yolov7-e6e.yaml') as f:
    e6e = yaml.load(f, Loader=yaml.FullLoader)

save_layer = [[] for _ in range(len(e6e['backbone']+e6e['head']))]
for i, args in enumerate(e6e['backbone']+e6e['head']):
    mf = [args[0]] if isinstance(args[0], int) else args[0]
    for f in mf:
        save_layer[i+f].append(i) if f < 0 and i > 0 else save_layer[f].append(i)

#expand
for i, sl in enumerate(save_layer):
    for sp in sl:
        for from_i_to_target in save_layer[i:sp]:
            if not (sp in from_i_to_target): 
                # print(f'{i} {sp}: append')
                from_i_to_target.append(sp)
    sl = sl.sort()

#Check
# for i, args in enumerate(e6e['backbone']+e6e['head']):
#     mf = [args[0]] if isinstance(args[0], int) else args[0]
#     print("%-3s: %-50s  mf: %-16s"%(i,save_layer[i],mf))
tr_sum = [None for _ in range(len(e6e['backbone']+e6e['head']))]
for i, sl in enumerate(save_layer):
    
    
    