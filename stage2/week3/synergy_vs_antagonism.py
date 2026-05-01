import numpy as np

ic50_dox = 9.24
ic50_ttp = 29.41

effect_levels=np.array([20,40,50,60,80])
print("Effect levels to analyze:",effect_levels)

#2. calculte CI at each level:
combo_fraction=0.3
ci_values=np.zeros(len(effect_levels))

for i, effect in enumerate(effect_levels):
    scale=effect/50
    dose_dox_alone=ic50_dox*scale
    dose_ttp_alone=ic50_ttp*scale

    dose_dox_combo=dose_dox_alone*combo_fraction*0.5
    dose_ttp_combo = dose_ttp_alone * combo_fraction * 0.5

    ci_values[i]=(dose_dox_combo/dose_dox_alone)+(dose_ttp_combo / dose_ttp_alone)

print(f"{'Effect':>8} {'CI':>8} {'Classification':>20}")
print("-" * 40)
for effect, ci in zip(effect_levels, ci_values):
    if ci < 0.3:
        label = "Strong Synergy"
    elif ci < 0.7:
        label = "Synergy"
    elif ci < 0.9:
        label = "Slight Synergy"
    elif ci <= 1.1:
        label = "Additive"
    else:
        label = "Antagonism"
    print(f"{effect:>7}%  {ci:>8.3f}  {label:>20}")