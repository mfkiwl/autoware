# from python_qt_binding import QtCore
# from python_qt_binding import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtWidgets

# from ..plugins.basic import AwToggleSwitch
from ...core import myutils
from ..plugins.basic import QToggleImage


class AwToggleGatewayWidget(QtWidgets.QWidget):

    def __init__(self, context):
        super(AwToggleGatewayWidget, self).__init__()
        self.context = context

        layout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel('Gateway')
        layout.addWidget(self.label)

        # self.switch = AwToggleSwitch()
        self.switch = QToggleImage(myutils.package('resources/toggle_off.png'), myutils.package('resources/toggle_on.png'))
        self.switch.switchedOn.connect(self.switchedOn)
        self.switch.switchedOff.connect(self.switchedOff)
        layout.addWidget(self.switch)

        self.setLayout(layout)

    def switchedOn(self):
        print('gateway switch on')

    def switchedOff(self):
        print('gateway switch off')
