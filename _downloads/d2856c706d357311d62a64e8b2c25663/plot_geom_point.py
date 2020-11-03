# -*- coding: utf-8 -*-
"""
Geometry geom_point()
=====================

An example of the geom_point() geometry.
"""

import numpy as np
from lets_plot import *; LetsPlot.setup_html()
# sphinx_gallery_thumbnail_path = '_static/gallery/thumbnails/plot_geom_point.png'

x = np.random.uniform(-1, 1, size=100)
y = np.random.normal(size=100)

ggplot() + geom_point(aes(x='x', y='y'), data=dict(x=x, y=25*x**2+y))