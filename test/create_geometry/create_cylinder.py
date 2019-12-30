#!/usr/bin/env python

##Copyright 2009-2014 Jelle Feringa (jelleferinga@gmail.com)
##
##This file is part of pythonOCC.
##
##pythonOCC is free software: you can redistribute it and/or modify
##it under the terms of the GNU Lesser General Public License as published by
##the Free Software Foundation, either version 3 of the License, or
##(at your option) any later version.
##
##pythonOCC is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU Lesser General Public License for more details.
##
##You should have received a copy of the GNU Lesser General Public License
##along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function

from OCC.Core.gp import gp_Pnt2d,gp_Pnt, gp_Ax1,gp_Dir,gp_Ax2,gp_Circ
from OCC.Core.Geom import Geom_Circle,Geom_SurfaceOfLinearExtrusion,Geom_BezierCurve
from OCC.Core.TColgp import TColgp_Array1OfPnt
from OCC.Display.SimpleGui import init_display
display, start_display, add_menu, add_function_to_menu = init_display()


def beziercurve():

    # the first bezier curve
    array = TColgp_Array1OfPnt(1, 5)
    array.SetValue(1, gp_Pnt(0, 0,-5))
    array.SetValue(2, gp_Pnt(1, 2,1))
    array.SetValue(3, gp_Pnt(2, 3,2))
    array.SetValue(4, gp_Pnt(4, 3,-2))
    array.SetValue(5, gp_Pnt(5, 5,-2))
    circle = Geom_Circle(gp_Ax2(),100.0)
    surface=Geom_SurfaceOfLinearExtrusion(circle,gp_Dir(0.0,0.0,1.0))
    print(surface.Bounds())
    display.DisplayShape(surface,update=True, color='Blue')
if __name__ == '__main__':
    beziercurve()
    start_display()
