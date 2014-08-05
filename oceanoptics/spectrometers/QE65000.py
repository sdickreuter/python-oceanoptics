# tested
# ----------------------------------------------------------
from __future__ import print_function
from ..base import OceanOpticsBase as _OOBase
from ..base import OceanOpticsTEC as _OOTEC
#----------------------------------------------------------


class QE65000(_OOBase, _OOTEC):
    def __init__(self):
        super(QE65000, self).__init__('QE65000')
        self.initialize_TEC()
