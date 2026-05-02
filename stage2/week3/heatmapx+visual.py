import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(suppress=True)

#1. create combination matrix:
dox_doses = np.array([0.1, 1.0, 10.0, 100.0])   # nM
ttp_doses = np.array([0.1, 1.0, 10.0, 100.0]) 

combo_matix=np.array([[95,88,62,41],
                    [87,74,48,28],
                    [61,49,22,11],
                    [38,24,8,3]],dtype=float) 

print("Combo matrix shape:",combo_matix.shape)
print(combo_matix)

#2.draw heatmap
plt.figure(figsize=(7,6))
img=plt.imshow(combo_matix,cmap='RdYlGn',aspect='auto',vmin=0,vmax=100)
plt.colorbar(img,label='Cell Viability (%)')
plt.xticks(range(4),[f"{d}nM" for d in ttp_doses])
plt.yticks(range(4),[f"{d}nM"for d in dox_doses])

plt.xlabel('TTP488 Concentration',fontsize=12)
plt.ylabel('Doxorubicin Concentration',fontsize=12)
plt.title('Combination Viability Matrix Dox+TTP488 in 4T1 TNBC Cells',fontsize=13)
plt.tight_layout()
plt.savefig('combo_heatmap.png',dpi=150)


#3. add. text label
for i in range(4):
    for j in range(4):
        plt.text(j,i,f'{combo_matix[i,j]:.0f}%',ha='center',va='center',fontsize=10,fontweight='bold',color='black')

plt.show()
        