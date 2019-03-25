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

