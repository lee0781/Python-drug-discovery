import numpy as np
np.random.seed(42)

#practice


row_names=['A','B','C','D']
plate=np.vstack([np.random.uniform(5,30,size=(1,4)),np.random.uniform(31,50,size=(1,4)),np.random.uniform(51,80,size=(1,4)),np.random.uniform(80,100,size=(1,4))])

row_mean=np.mean(plate,axis=1)
row_std=np.std(plate,axis=1,ddof=1)

print(f"{'Group Name':<9}{'Mean':>10}{'STD':>12}{'FLAG':>12}")

for i in range(4):
    mean_val=row_mean[i]
    std_val=row_std[i]
    if mean_val>80:
        flag='HIGH'
    elif mean_val<20:
        flag='LOW'
    else:
        flag='MID'
    print(f"{row_names[i]:<12}{mean_val:>12.1f}{std_val:>12.1f}{flag:>12}")
    
