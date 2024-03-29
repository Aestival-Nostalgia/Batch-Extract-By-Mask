# -- coding:UTF-8 --

import arcpy
import glob
import os
 
arcpy.CheckOutExtension('Spatial')
 
#指定先前拼接后的遥感影像所在目录
inws = r"D:\F\DATA"
 
#指定裁剪后的影响存放目录
outws = r"D:\F\DATA_Clip"
 
#指定shp范围边界文件，即目标区域的边界
mask = r"D:\F\Boundary.shp"
 
#利用glob包，将inws下的所有tif文件读存放到rasters中
rasters = glob.glob(os.path.join(inws, "*.tif"))
 
#循环rasters中的所有影像，进行按掩模提取操作
for ras in rasters:
    outname = os.path.join(outws, os.path.basename(ras).split(".")[0] + "_clip.tif")  #指定输出文件的命名方式（以被裁剪文件名+_clip.tif命名）
    out_extract = arcpy.sa.ExtractByMask(ras, mask)  #执行按掩模提取操作B
    out_extract.save(outname)  #保存数据
    
print("Over!") #用来指明代码已经运行结束

#第一行用来定义UTF编码，如果没有第一行的话，使用VScode运行代码时可能会无法识别文件路径
#基于Python 2.7和Arcpy环境，需要ArcGIS Desktop 10.2 
#初版本文件生成自 VS 2019 的项目（project）
#不要忘记配置Py 2.7 32位环境，以及VS的旧版本Py调试器，代码效率很高
#好用好用！