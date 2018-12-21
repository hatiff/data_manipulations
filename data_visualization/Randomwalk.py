# -*- coding: utf-8 -*-
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
import sys

def update():
    global x, y, z
    x += np.random.randint(-1, 2)
    y += np.random.randint(-1, 2)
    z += np.random.randint(-1, 2)
    m2 = gl.GLMeshItem(meshdata=md, smooth=True, shader='normalColor', glOptions='opaque')
    m2.translate(x, y, z)
    m2.scale(0.1, 0.1, 0.1)
    w.addItem(m2)

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.show()
w.setWindowTitle('pyqtgraph example: GL Shaders')
w.setCameraPosition(distance=15, azimuth=-90)

md = gl.MeshData.sphere(rows=10, cols=20)
x, y, z = 0, 0, 0
m = gl.GLMeshItem(meshdata=md, smooth=True, color=(1, 0, 0, 0.2), shader='balloon', glOptions='additive')
m.translate(x, y, z)
m.scale(0.1, 0.1, 0.1)
w.addItem(m)

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)


if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()