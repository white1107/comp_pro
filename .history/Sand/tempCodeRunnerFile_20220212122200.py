# %matplotlib inline

matplotlib.font_manager._rebuild() # 問題の原因になることが多いフォントキャッシュを再構築しておきます
plt.rcParams['font.family'] = 'IPAexGothic'

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

matplotlib._version.get_versions()['version']
# 2.2.0
# 1. 凡例を消す legend=False
# 2. バーの間を詰める width=0.8
fig, ax = plt.subplots(figsize=(6, 3))
combatpower.plot.barh(legend=False, ax=ax, width=0.8)

# 3. y軸の順番を逆に
ax.invert_yaxis()

# 4. 四方の枠(spines)を消す
[spine.set_visible(False) for spine in ax.spines.values()]
# 以下でも可能
# sides = ['left', 'right', 'top', 'bottom']
# [ax.spines[side].set_visible(False) for side in sides] 

# 5. y軸x軸のtickを消す
# 6. x軸のtick label(10000など)を消す
ax.tick_params(bottom=False, left=False, labelbottom=False)

# 7. y軸のラベルサイズを大きく
ax.tick_params(axis='y', labelsize='x-large')

# 8. バーの右側に実際の値を表示
vmax = combatpower['戦闘力'].max()
for i, value in enumerate(combatpower['戦闘力']):
    ax.text(value+vmax*0.02, i, f'{value:,}', fontsize='x-large', va='center', color='C0')