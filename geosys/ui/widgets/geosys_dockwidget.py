# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeosysPluginDockWidget
                                 A QGIS plugin
 Discover, request and use aggregate imagery products based on landsat-8,
 Sentinel 2 and other sensors from within QGIS, using the GEOSYS API.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-03-11
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Kartoza (Pty) Ltd
        email                : andre@kartoza.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

from geosys.utilities.resources import get_ui_class

FORM_CLASS = get_ui_class('geosys_dockwidget_base.ui')


class GeosysPluginDockWidget(QtWidgets.QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        """Constructor."""
        super(GeosysPluginDockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://doc.qt.io/qt-5/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()