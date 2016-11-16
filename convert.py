#!/usr/bin/python
import subprocess
import glob
import os
from os.path import basename
# Remove old files
files = glob.glob('generated/*.*')
for f in files:
    os.remove(f)

files = glob.glob('generated/favicon/*.*')
for f in files:
    os.remove(f)


source_files = glob.glob('*.svg')
print(source_files)
# Convert form Inkscape SVG to PNG
#inkscape sunpy_logo.svg --export-png=generated/sunpy_logo.png
for f in source_files:
    subprocess.call(["inkscape", f, "--export-png=generated/" + os.path.splitext(f)[0] + ".png"])

# Convert form Inkscape SVG to Plain SVG (for web use)
#inkscape sunpy_logo.svg --export-plain-svg=generated/sunpy_logo_plain.svg
for f in source_files:
    subprocess.call(["inkscape", f, "--export-plain-svg=generated/" + os.path.splitext(f)[0] + ".svg"])

subprocess.call(["webicon.sh", "sunpy_icon.svg"])

# Remove full-res PNGs since these aren't needed
#rm generated/sunpy_logo.png
