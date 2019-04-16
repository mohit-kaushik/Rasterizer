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

