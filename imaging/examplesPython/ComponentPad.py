#!/usr/local/bin/python
import os
try:
  VTK_DATA = os.environ['VTK_DATA']
except KeyError:
  VTK_DATA = '../../../vtkdata/'


from vtkpython import *
from WindowLevelInterface import *

# Make an image larger by repeating the data.  Tile.

# Image pipeline

reader = vtkImageReader()
reader.SetDataByteOrderToLittleEndian()
reader.SetDataExtent(0,255,0,255,1,93)
reader.SetFilePrefix(VTK_DATA + "/fullHead/headsq")
reader.SetDataMask(0x7fff)
#reader.ReleaseDataFlagOff()
#reader.DebugOn()

pad = vtkImageConstantPad()
pad.SetInput(reader.GetOutput())
pad.SetOutputNumberOfScalarComponents(3)
pad.SetConstant(800)
pad.ReleaseDataFlagOff()


viewer = vtkImageViewer()
viewer.SetInput(pad.GetOutput())
viewer.SetZSlice(22)
viewer.SetColorWindow(1600)
viewer.SetColorLevel(700)


# make interface
WindowLevelInterface(viewer)
