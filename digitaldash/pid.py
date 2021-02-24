"""PID objects class"""
from typing import Mapping
from static.constants import PID_UNITS
from static.constants import KE_PID

class PID():
    """Class for managing PID information."""

    value: str
    unit: str
    range: Mapping[str, str]
    unitLabel: str

    def __init__(self, **kwargs: str) -> None:
        super(PID, self).__init__()

        self.value = kwargs.get('pid', None)
        self.unit = PID_UNITS[kwargs.get('unit', '')]
        self.unitLabel = kwargs.get('unit', '')
        self.range = KE_PID.get(self.value).get('units').get(self.unitLabel)

        self.generateByteCode()

    def generateByteCode(self) -> None:
        """Deprecated"""
        self.byteCode = []
        if len(self.byteCode) == 6:
            self.byteCode = (int(self.value, 16) >> 8) & 0xFF        # Mode
            self.byteCode.append(0x00)                               # PID byte 0
        else:
            self.byteCode.append((int(self.value, 16) >> 16) & 0xFF) # Mode
            self.byteCode.append((int(self.value, 16) >> 8) & 0xFF)  # PID byte 0
        self.byteCode.append((int(self.value, 16)) & 0xFF)           # PID byte 1
