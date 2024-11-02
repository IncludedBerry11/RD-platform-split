# RD-platform-split
Split the merged shaderCodes for MCBE RenderDragon 
为基岩版渲染龙拆分独立的代码 

Experimental. Just a repo. 
仅供测试。不保证稳定性 

version ranges 版本范围 
---

  **1.19.60**: doesn't exist ok? （这个版本还未加入延迟渲染） 

  **1.20.30**: `1.20.20.20`, `1.20.30`, `1.20.40`, `1.20.50`, `1.20.60.23` 

  **1.20.73**: `1.20.60.24`, `1.20.60`, `1.20.70`, `1.20.80.21` 

  **1.20.81**: `1.20.80.22`, `1.20.80`, `1.21.0`, `1.21.2`, `1.21.20.21` 

  **1.21.30**: `1.21.20.22`, `1.21.20`, `1.21.30`, `1.21.40`, `1.21.50`, `???` 

Incorrect version may bring your terrain invisible, or even crash your minecraft. 
错误的版本会导致画面变成虚空，或导致闪退。 

---
`ESSL_stutter_fix`: these are minified and optimized essl_100 materials. 
may working better on SnapDragon(Adreno GPU) devices. 
骁龙手机推荐使用【修复卡顿包】以减少间歇卡顿 

`ESSL_unoptimized`: these are essl_310 materials which were just pre-process. 
may working better on MediaTek(Mali GPU) devices. 
联发科手机推荐使用【增加卡顿包】以减少间歇卡顿 

`ESSL_backup`: removed those useless comments to reduce filesize. 
just for vanilla backup. 
与原版渲染器应该不会有任何区别。【啥也没改包】仅仅降低了文件体积 

`SM50_recude`: dx11 dxil materials which deferred unsupported. 
reduce filesize for those who don't use deferred or rtx. also a vanilla backup 
为Win10用户降低文件体积，同时可作为原版备份 

***
Discord: Mrwang2408
bilibili 王2408
QQ: 3308116191
