# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from core import map
from core.localisation import _


class itemDialog(QtGui.QDialog):
	"""
	Window to fill some informations to create an item
	label npc gender	npc gender field
	create button		cancel button
	"""
	_app = None
	_parent = None
	_coordinates = None

	_messageLabel = None

	_saveButton = None
	_cancelButton = None

	itemAdded = QtCore.pyqtSignal(int, int)
	itemUpdated = QtCore.pyqtSignal(int, int)

	def __init__(self, parent, app, coordinates=None, row=None):
		"""
		Creates the window GUI and displays the window
		"""
		QtGui.QDialog.__init__(self, parent)
		self._app = app
		self._parent = parent
		self._editedRow = None
		if coordinates is None and row is None:
			raise BaseException("At least a row or a tuple of coordinates is needed")
		elif coordinates is None:
			self._editedRow = row['internalName']
			self._coordinates = (row['x'], row['y'])
		else:
			self._coordinates = coordinates

		self._parent.selectCell(self._coordinates[0], self._coordinates[1])
		self._row = row
		self.setFixedWidth(250)
		self.initUI()
		self.setWindowTitle(self._title)
		self.setModal(True)
		self.connectSignals()
		self.show()

	def initUI(self):
		"""
		Creates the UI
		"""
		layout = QtGui.QGridLayout()

		self._messageLabel = QtGui.QLabel()
		self._messageLabel.setWordWrap(True)

		fieldsLayout = self.getFields(self._row)

		if self._editedRow is not None:
			self._saveButton = QtGui.QPushButton(_('EDIT_BUTTON'))
		else:
			self._saveButton = QtGui.QPushButton(_('CREATE_BUTTON'))
		self._saveButton.clicked.connect(self.createItem)
		self._cancelButton = QtGui.QPushButton(_('CANCEL_BUTTON'))
		self._cancelButton.clicked.connect(self.close)

		layout.addWidget(self._messageLabel, 0, 0, 1, 2)
		layout.addLayout(fieldsLayout, 1, 0, 1, 2)
		layout.addWidget(self._saveButton, 2, 0)
		layout.addWidget(self._cancelButton, 2, 1)

		self.setLayout(layout)

	def connectSignals(self):
		"""
		Connect a signal to unselect the cell if the window is rejected
		"""
		self.rejected.connect(self._parent.unselectCell)

	def displayMessage(self, message):
		"""
		Method to display a message in the window.
		"""
		self._messageLabel.setText(message)
		self.adjustSize()


