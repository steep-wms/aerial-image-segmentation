# Segment aerial images tutorial

This is the source code accompanying the Steep tutorial on segmenting aerial images:

https://steep-wms.github.io/docs/segment-aerial-images/

## Contents

### `data/`

Contains an aerial image that can be used as input for the workflow from this tutorial.

The image has been downloaded from https://gds.hessen.de. The data is provided by the [Hessische Verwaltung für Bodenmanagement und Geoinformation](https://hvbg.hessen.de/). It is free and can be used for any purpose.

### `segment-service/`

An image segmentation service based on [Segment Anything](https://segment-anything.com/) and [segment-geospatial](https://samgeo.gishub.org/samgeo/).

Usage:

    python3 segment.py <input_image> <output_image>

### `steep/`

Configuration files needed to run the image segmentation workflow.

### `tile-service/`

A tiling service that splits an image into smaller tiles.

Usage:

    node tile.js <input_image> <output_directory> <number_of_cols>

`<number_of_cols>` specifies the number of columns and rows to split the image into. A value of 5 means the image will be split into 5x5 tiles.

### `workflow/`

The image segmentation workflow.
