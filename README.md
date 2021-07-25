# auto_png2gif_converter
A small python script to convert a series of png files to gif files

## Prerequisites
- [Python 3.8.0 or higher](https://www.python.org/downloads/)
- [imageio](https://pypi.org/project/imageio/)
- [natsort](https://pypi.org/project/natsort/)
- [Pillow](https://pypi.org/project/Pillow/)

## Usage
- Convert png files in a current directory into gif files.
- The script can auto match the animation together, even if the png files are not the same size.

## Guidelines
- png files naming order needs to follow [natural sort order](https://en.wikipedia.org/wiki/Natural_sort_order).
- png files size must be less than 54x54 pixels.
- png files of the same animation needs to be next to each other, based on above naming order.
- The converted gif might be broken in some special cases.

## Build and Run
- Put your png files into this project folder.
- Run ```python main.py```.

## Example
- png files: https://imgur.com/a/BwHAzhf
- Result file: https://imgur.com/a/7XLYBsR
- Note: those images are from [Otherworld Legends](https://play.google.com/store/apps/details?id=com.chillyroom.zhmr.gp)