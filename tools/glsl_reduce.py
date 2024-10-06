
import os  
import re  
  
# 定义正则表达式  
regex1 = re.compile(r'(?<=[(){}<>=+\-*/|&?:;,])\s+|\s+(?=[(){}<>=+\-*/|&?:;,])')  
replace1 = ''  

regex2 = re.compile(r'tmpvar_')  
replace2 = '_'  

regex3 = re.compile(r'diffuse_')  
replace3 = 'd_'  

regex4 = re.compile(r'albedo_')  
replace4 = 'al_'  

#定义json规则
regex_j1 = re.compile(r'\"DepthOnly(\"|Opaque\")(,\s*|\s*)')

regex_j2 = re.compile(r',(?=\s*[}\]])')



# 定义要遍历的目录路径  
directory= 'src'  # 请将此路径替换为实际的目录路径  

# 初始化累计替换次数  
total_count1 = 0  
total_count2 = 0  
total_count3 = 0  

# 遍历目录及其子目录中的所有.glsl文件  
for root, dirs, files in os.walk(directory):  
    for file in files:  
        if file.endswith('.glsl'):  
            file_path = os.path.join(root, file)  
              
            # 读取文件内容  
            with open(file_path, 'r', encoding='utf-8') as f:  
                content = f.read()  
              
            # 使用正则表达式去除符号两侧的空格  
            content, count1 = regex1.subn(replace1, content)  
            total_count1 += count1  
              
            content, count2 = regex2.subn(replace2, content)  
            total_count2 += (6 * count2)  
              
            if file.endswith('.Fragment.glsl'):  
                content, count3 = regex3.subn(replace3, content) 
                content, count4 = regex4.subn(replace4, content) 
                total_count2 += (6 * count3) + (4 * count4)  
              
            # 将格式化后的内容写回文件  
            with open(file_path, 'w', encoding='utf-8') as f:  
                f.write(content) 
          
          
        if file.endswith('.json'):  
            file_path = os.path.join(root, file)  
              
            # 读取文件内容  
            with open(file_path, 'r', encoding='utf-8') as f:  
                content = f.read()  
                
            content, count_j = regex_j1.subn('', content)  
            if count_j > 0:  
                print('DepthOnly has removed')  
            
            content = regex_j2.sub('', content)  
            
            with open(file_path, 'w', encoding='utf-8') as f:  
                f.write(content) 
          
          
          
total_count3 += (total_count1 + total_count2) / 1024  
print(f"{total_count1} spaces, {total_count2} tmpvar Renamed, Saved {total_count3:.2f} KB")








