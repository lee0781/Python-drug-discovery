import numpy as np

np.random.seed(42)

#kinase inhibitor screen
plate=np.vstack([np.random.uniform(15,35,size=(1,6)),np.random.uniform(25,50,size=(1,6)),np.random.uniform(55,80,size=(1,6)),np.random.uniform(90,100,size=(1,6)),np.random.uniform(1,8,size=(1,6)),np.random.uniform(95,102,size=(1,6))])
row_names=['EGFRi-1','EGFRi-2','EGFRi-3','DMSO','Stauro','Media']

#calculate row means using axis
row_means=np.mean(plate,axis=1)

#calculate row stds using axis
row_stds=np.std(plate,axis=1,ddof=1)

#print header
print(f"{'Compound':<12}{'Mean':>12}{'SD':>12}{'Flag':>12}")

#loop
for i in range(6):
    mean_val=row_means[i]
    std_val=row_stds[i]
    if mean_val>80:
        flag="ctrl_neg"
    elif mean_val<15:
        flag="ctrl_pos"
    elif mean_val<50:
        flag="HIT"
    else:
        flag="---"
    print(f"{row_names[i]:<12}{mean_val:>12.1f}%{std_val:>12.1f}{flag:>12}")


