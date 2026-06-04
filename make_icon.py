from PIL import Image
import os

# 设置输入输出
input_file = "images/favicon-512x512.png" 
output_file = "images/favicon.ico"
sizes = [16, 32, 48, 64, 128, 256]

if os.path.exists(input_file):
    img = Image.open(input_file)
    # 强制转换为 RGBA 以确保透明度
    img = img.convert("RGBA")
    
    icon_layers = []
    for s in sizes:
        # Image.NEAREST 就是最近邻插值
        resized_img = img.resize((s, s), resample=Image.NEAREST)
        icon_layers.append(resized_img)
    
    icon_layers[0].save(output_file, format='ICO', sizes=[(s, s) for s in sizes])
    print(f"成功！已生成 {output_file}")
else:
    print(f"找不到文件: {input_file}")