import arcpy
import glob
import os
 
arcpy.CheckOutExtension('Spatial')
 
#指定先前拼接后的遥感影像所在目录
inws = r"G:\Bachelor_Degree_Thesis\DATA\LUCC_30m\Mosaic_Result"
 
#指定裁剪后的影响存放目录
outws = r"G:\Bachelor_Degree_Thesis\DATA\LUCC_30m\Extracted"
 
#指定shp范围边界文件，即目标区域的边界
mask = r"G:\Bachelor_Degree_Thesis\DATA\Boundary\boundary.shp"
 
#利用glob包，将inws下的所有tif文件读存放到rasters中
rasters = glob.glob(os.path.join(inws, "*.tif"))
 
#循环rasters中的所有影像，进行按掩模提取操作
for ras in rasters:
    outname = os.path.join(outws, os.path.basename(ras).split(".")[0] + "_clip.tif")  #指定输出文件的命名方式（以被裁剪文件名+_clip.tif命名）
    out_extract = arcpy.sa.ExtractByMask(ras, mask)  #执行按掩模提取操作
    out_extract.save(outname)  #保存数据
    
#基于Python 2.7和Arcpy环境，需要ArcGIS Desktop 10.2 
#文件生成自 VS 2019 的项目（project）
