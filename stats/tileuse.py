#!/usr/bin/python
#
# Calculation of tile caches for The Netherlands RD with Geonovum/PDOK tiling scheme  and Web Mercator
#

# Average tile size in GB (35.0 kB)
JPG_TILESZ_GB = (16.0 / (1024.0 * 1024.0))

# Geonovum/PDOK tiling res
RD_GRID_COVERAGE = [-285401.920, 22598.080, 595401.920, 903401.920]
RD_RESOS = [3440.64, 1720.32, 860.16, 430.08, 215.04, 107.52, 53.76, 26.88, 13.44, 6.72, 3.36, 1.68, 0.84, 0.42, 0.21,
            0.105, 0.0525]

# Tiling area to seed (subarea of grid, otherwise too much sea).
# bbox NL: [10000.000,299995.559,279997.956,625000.000]
RD_SEED_COVERAGE = [10000.000, 299995.559, 279997.956, 625000.000]
RD_SEED_AREA_UR_M = {'x': 279997.956, 'y': 625000.000}
RD_SEED_AREA_LL_M = {'x': 10000.000, 'y': 299995.559}
RD_SEED_AREA_W_M = float(RD_SEED_AREA_UR_M['x'] - RD_SEED_AREA_LL_M['x'])
RD_SEED_AREA_H_M = float(RD_SEED_AREA_UR_M['y'] - RD_SEED_AREA_LL_M['y'])
RD_SEED_AREA_M2 = float(RD_SEED_AREA_W_M * RD_SEED_AREA_H_M)

# Web Mercator tiling res
# http://www.maptiler.org/google-maps-coordinates-tile-bounds-projection/
# http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Zoom_levels
WM_GRID_COVERAGE = [-20037508.342789244, -20037508.342789244, 20037508.342789244, 20037508.342789244]
WM_RESOS = [156543.03, 78271.52, 39135.76, 19567.88, 9783.94, 4891.97, 2445.98, 1222.99, 611.49, 305.75, 152.874057,
            76.4370283, 38.2185141, 19.1092571, 9.55462853, 4.77731427, 2.38865713, 1.19432857, 0.5972, 0.2986, 0.1493]


# Tiling area to seed (subarea of grid, otherwise too much sea).
# bbox NL: [10000.000,299995.559,279997.956,625000.000]
# in WGS84 3.336019,50.671759  7.275173,53.596201
WM_SEED_COVERAGE = [371363.93, 6563435.794, 809868.554, 7094049.501]
WM_SEED_AREA_UR_M = {'x': 809868.554, 'y': 7094049.501}
WM_SEED_AREA_LL_M = {'x': 371363.93, 'y': 6563435.794}
WM_SEED_AREA_W_M = float(WM_SEED_AREA_UR_M['x'] - WM_SEED_AREA_LL_M['x'])
WM_SEED_AREA_H_M = float(WM_SEED_AREA_UR_M['y'] - WM_SEED_AREA_LL_M['y'])
WM_SEED_AREA_M2 = float(WM_SEED_AREA_W_M * WM_SEED_AREA_H_M)


def p(s):
    print s

def calc_tiles(grid_coverage, resos, seed_coverage, seed_area_width, seed_area_height, tile_sz_gb):
    p('Grid coverage  %s' % str(grid_coverage))
    p('Tile coverage  %s' % str(seed_coverage))
    p('Based on average tilesize %s kB (JPEG)' % str(JPG_TILESZ_GB*1024*1024))
    p('Seed area (m): len=%5.2f breed=%5.2f oppervlak=%5.2f' % (seed_area_width, seed_area_height, float(seed_area_width * seed_area_height)
    ))
    p('Kentallen en opslag')

    storage_total = 0.0
    zoom = 0
    p('zoom;res(m/px);tiles;tiles (wxh);storage @zoom (GB);storage total (GB)')
    for res in resos:
        pixels_x = seed_area_width / res
        pixels_y = seed_area_height / res

        tiles_count_x = (pixels_x / 256.0)
        tiles_count_y = (pixels_y / 256.0)
        tiles_count = tiles_count_x * tiles_count_y + 1.0

        storage_level = tile_sz_gb * float(tiles_count)
        storage_total += storage_level
        p('%d;%5.2f;%d;%s;%5.2f;%5.2f' % (
            zoom, res, tiles_count, str(int(round(tiles_count_x))) + 'x' + str(int(round(tiles_count_y))), storage_level, storage_total))
        zoom += 1

if __name__ == '__main__':
    p('TILES Dutch RD - EPSG:28992')
    # def calc_tiles(grid_coverage, resos, seed_coverage, seed_area_width, seed_area_height, tile_sz_gb):
    calc_tiles(RD_GRID_COVERAGE, RD_RESOS, RD_SEED_COVERAGE, RD_SEED_AREA_W_M, RD_SEED_AREA_H_M, JPG_TILESZ_GB)
    p('')
    p('TILES Web Mercator (Google/OSM) - EPSG:900913')
    calc_tiles(WM_GRID_COVERAGE, WM_RESOS, WM_SEED_COVERAGE, WM_SEED_AREA_W_M, WM_SEED_AREA_H_M, JPG_TILESZ_GB)
