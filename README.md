# RD-platform-split
Split the merged shaderCodes for MCBE RenderDragon  
为基岩版渲染龙拆分独立的代码

Experimental usage. Do Not release.  
仅供测试。不保证稳定性

version ranges 版本范围
---

  **1.19.60**: doesn't exist ok? （这个版本还未加入延迟渲染）

  **1.20.30**: `1.20.20.20`, `1.20.30`, `1.20.40`, `1.20.50`, `1.20.60.23`

  **1.20.73**: `1.20.60.24`, `1.20.60`, `1.20.70`, `1.20.80.21`

  **1.20.81**: `1.20.80.22`, `1.20.80`, `1.21.0`, `1.21.2`, `1.21.20.21` 

  **1.21.30**: `1.21.20.22`, `1.21.20`, `1.21.30`, `1.21.40`, `???`

错误的版本会导致画面变成虚空。

---
`essl-100`: may working better on SnapDragon devices  
或许在骁龙(Adreno GPU)手机上更流畅

`essl-310`: may working better on MediaTek devices  
或许在联发科(Mali GPU)手机上更流畅

`essl-300`: this stuff is new. will it be better or not?
这是个新玩意，实际效果有待验证(似乎挺流畅)

`essl-all`: Nothing changed. just vanilla  
啥也没改，只是删除了无效注释行


***
Bilibili 王2408