import gdal
import sys
import numpy as np

tif = '/home/workspace/airpollution/sdata/02_Environment&NaturalResourcesFactors/02-Topography/01_DEM.tif'

def GetExtent(gt,cols,rows):
    ''' Return list of corner coordinates from a geotransform

        @type gt:   C{tuple/list}
        @param gt: geotransform
        @type cols:   C{int}
        @param cols: number of columns in the dataset
        @type rows:   C{int}
        @param rows: number of rows in the dataset
        @rtype:    C{[float,...,float]}
        @return:   coordinates of each corner
    '''
    ext = []
    xarr =[0, cols]
    yarr = [0, rows]

    for px in xarr:
        for py in yarr:
            x=gt[0]+(px*gt[1])+(py*gt[2])
            y=gt[3]+(px*gt[4])+(py*gt[5])
            ext.append([x,y])
        yarr.reverse()
    return ext

def read_raster(tif):
    raster = gdal.OpenShared(tif)
    if raster is None:
        print("Failed to open file:" + tif)
        sys.exit()
    cols = raster.RasterXSize
    rows = raster.RasterYSize
    print "the tif size is cols: %s, rows: %s" % (cols, rows)
    gt = raster.GetGeoTransform()
    extent = GetExtent(gt, cols, rows)
    print 'the extent of the coordinates of the image is %s' % extent
    return raster

# read a buffer values that are in the neighborhood of coordinates x_c, y_c, the buffer size is window_x, window_y
def read_buffer_fcoord(raster, x_c,y_c, window_x, window_y):
    gt = raster.GetGeoTransform()
    col,row = coord2loc(gt, x_c, y_c)
    winx = window_x/2
    winy = window_y/2
    new_col = col-winx
    new_row = row-winy
    values_neighbor = raster.ReadAsArray(new_col, new_row,window_x, window_y)
    print "the values around location %s and %s with neighborhood (%s, %s )are: \n %s" %(col, row, window_x, window_y,values_neighbor)
    return values_neighbor

# read one value at the defined coordinates x_c, y_c
def read_value_fcoord(raster, x_c, y_c):
    gt = raster.GetGeoTransform()
    col, row = coord2loc(gt, x_c, y_c)
    #the value at location col and row is the left-top corner value.
    value = raster.ReadAsArray(col, row, 1,1)
    print "the value at location col and row is: \n %s" %value
    return value

def coord2loc(gt, x_c, y_c):
    col = int((x_c-gt[0])/gt[1])
    row = int((y_c-gt[3])/gt[5])
    print "location of coordinates x: %s, y:%s is %s, %s"%(x_c,y_c,col, row)
    return col,row

def main():
    raster = read_raster(tif)
    value = read_value_fcoord(raster, 48897.0, 3000500.0)
    values = read_buffer_fcoord(raster, 48897.0, 3000500.0,5,5)

if __name__ == "__main__":
    main()




#
# def reclassify(rasterfile, dst_file):
#     dataset = gdal.OpenShared(rasterfile)
#     if dataset is None:
#         print("Failed to open file: " + rasterfile)
#         sys.exit(1)
#     band = dataset.GetRasterBand(1)
#     xsize = dataset.RasterXSize
#     ysize = dataset.RasterYSize
#     proj = dataset.GetProjection()
#     geotrans = dataset.GetGeoTransform()
#     noDataValue = band.GetNoDataValue()
#
#     print "Output file %s size:" % rasterfile, xsize, ysize
#     rastervalue = band.ReadAsArray(xoff=0, yoff=0, win_xsize=xsize, win_ysize=ysize)
#
#     #mask0 = rastervalue==noDataValue
#     #rastervalue[mask0] = np.nan
#
#     mask1_1 = rastervalue<10
#     mask1_2 = rastervalue>0
#     mask1 = np.logical_and(mask1_1, mask1_2)
#     rastervalue[mask1] = 1
#
#     mask2_1 = rastervalue >= 10
#     mask2_2 = rastervalue<15
#     mask2 = np.logical_and(mask2_1, mask2_2)
#     rastervalue[mask2] = 2
#
#     mask3_1 = rastervalue>=15
#     mask3_2 = rastervalue<25
#     mask3=np.logical_and(mask3_1,mask3_2)
#     rastervalue[mask3]=3
#
#     mask4_1 = rastervalue >= 25
#     mask4_2 = rastervalue < 35
#     mask4 = np.logical_and(mask4_1, mask4_2)
#     rastervalue[mask4] = 4
#
#
#     #mask5_1 = rastervalue >= 35
#     #mask5_2 = rastervalue < 100
#     #mask5 = np.logical_and(mask5_1, mask5_2)
#     #rastervalue[mask5] = 5
#
#     rastervalue[rastervalue >= 35 & rastervalue < 100] = 5
#
#     mask6 = rastervalue >= 100
#     rastervalue[mask6] = 6
#
#     # output the array in geotiff format
#     dst_format = 'GTiff'
#     dst_datatype = gdal.GDT_UInt32
#     dst_nbands = 1
#
#     driver = gdal.GetDriverByName(dst_format)
#     dst_ds = driver.Create(dst_file, xsize, ysize,dst_nbands,dst_datatype)
#
#     dst_ds.SetGeoTransform(geotrans)
#     dst_ds.SetProjection(proj)
#     dst_ds.GetRasterBand(1).SetNoDataValue(noDataValue)
#     dst_ds.GetRasterBand(1).WriteArray(rastervalue)
#
#     return dst_file