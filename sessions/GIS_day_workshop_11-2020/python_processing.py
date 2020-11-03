
from laspy.file import File
import argparse
import numpy as np

import os

name = "colorized"
if not os.path.isfile(f"{name}.las"):
   os.system(f"pdal translate {name}.laz {name}.las")


inFile = File(f"{name}.las",mode="r")

inFile.red
colors = np.column_stack((inFile.red,inFile.green,inFile.blue))
maxs = colors.max(axis=0)
normColors = colors/maxs*255
colors = 0
df = pd.DataFrame(normColors)
df.describe()

final = np.column_stack((inFile.X,inFile.Y,inFile.Z,normColors))

np.savetxt(f"{name}.txt",final,delimiter=",",fmt=["%i","%i","%i","%i","%i","%i"])






