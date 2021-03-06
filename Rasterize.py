from osgeo import ogr
from osgeo import gdal

def create_road_mask(rasterSrc, vectorSrc, npDistFileName='results.tif', 
                            noDataValue=0, burn_values=1):

    '''
    Create building mask for rasterSrc,
    Similar to labeltools/createNPPixArray() in spacenet utilities
    '''
    
    ## open source vector file that truth data
    
    ## extract data from src Raster File to be emulated
    ## open raster file that is to be emulated
    srcRas_ds = gdal.Open(rasterSrc)
    source_ds = ogr.Open(vectorSrc)
    source_layer = source_ds.GetLayer()

    cols = srcRas_ds.RasterXSize
    rows = srcRas_ds.RasterYSize
    
    ## create First raster memory layer, units are pixels
    # Change output to geotiff instead of memory 
    memdrv = gdal.GetDriverByName('GTiff') 
    dst_ds = memdrv.Create(npDistFileName, cols, rows, 1, gdal.GDT_Byte, 
                           options=['COMPRESS=LZW']
                          )
    gt = srcRas_ds.GetGeoTransform()

    dst_ds.SetGeoTransform(gt)
    dst_ds.SetProjection(srcRas_ds.GetProjection())
    
    band = srcRas_ds.GetRasterBand(1)
    band.SetNoDataValue(noDataValue)    
    gdal.RasterizeLayer(dst_ds, [1], source_layer, None,None, [1],['ALL_TOUCHED=TRUE'])
    dst_ds = 0
    
    return
