# Ref: SX1272 Datasheet
# Accession: G00051

import enum

from ...support.bitstruct import *


__all__ = [
    # Register addresses
    "ADDR_OP_MODE", "ADDR_FIFO_ADDR_PTR", "ADDR_FIFO_TX_BASE_ADDR",
    "ADDR_FIFO_RX_BASE_ADDR", "ADDR_FIFO_RX_CURRENT_ADDR", "ADDR_IRQ_FLAGS_MASK",
    "ADDR_IRQ_FLAGS", "ADDR_RX_NB_BYTES", "ADDR_RX_HEADER_CNT_VALUE_MSB",
    "ADDR_RX_HEADER_CNT_VALUE_LSB", "ADDR_RX_PACKET_CNT_VALUE_MSB",
    "ADDR_RX_PACKET_CNT_VALUE_LSB", "ADDR_MODEM_STAT", "ADDR_PKT_SNR_VALUE",
    "ADDR_PKT_RSSI_VALUE", "ADDR_RSSI_VALUE", "ADDR_HOP_CHANNEL",
    "ADDR_MODEM_CONFIG_1", "ADDR_MODEM_CONFIG_2", "ADDR_SYMB_TIMEOUT_LSB",
    "ADDR_PREAMBLE_MSB", "ADDR_PREAMBLE_LSB", "ADDR_PAYLOAD_LENGTH",
    "ADDR_MAX_PAYLOAD_LENGTH", "ADDR_HOP_PERIOD", "ADDR_FIFO_RX_BYTE_ADDR",
    "ADDR_FEI_MSB", "ADDR_FEI_MIB", "ADDR_FEI_LSB", "ADDR_RSSI_WIDEBAND",
    "ADDR_DETECT_OPTIMIZE", "ADDR_INVERT_IQ", "ADDR_DETECTION_THRESHOLD",
    "ADDR_SYNC_WORD", "ADDR_INVERT_IQ_2", "ADDR_CHIRP_FILTER"
    # Registers
    "REG_OP_MODE", "REG_IRQ_FLAGS_MASK", "REG_IRQ_FLAGS", "REG_MODEM_STAT",
    "REG_HOP_CHANNEL", "REG_MODEM_CONFIG_1", "REG_MODEM_CONFIG_2",
    "REG_FEI_MSB", "REG_DETECT_OPTIMIZE", "REG_INVERT_IQ",
    # Enumerations
    "PLLTIMEOUT", "MODEMBW", "CODINGRATE", "HEADERMODE", "SPREADINGFACTOR",
    "TXMODE", "LNAGAINSOURCE", "DETECTOPTIMIZE", "DETECTIONTHRESHOLD", "LONGRANGEMODE",
    "ACCESSSHAREDREG", "MODE"
]

# Register addresses

ADDR_OP_MODE                 = 0x01
ADDR_FIFO_ADDR_PTR           = 0x0D
ADDR_FIFO_TX_BASE_ADDR       = 0x0E
ADDR_FIFO_RX_BASE_ADDR       = 0x0F
ADDR_FIFO_RX_CURRENT_ADDR    = 0x10
ADDR_IRQ_FLAGS_MASK          = 0x11
ADDR_IRQ_FLAGS               = 0x12
ADDR_RX_NB_BYTES             = 0x13
ADDR_RX_HEADER_CNT_VALUE_MSB = 0x14
ADDR_RX_HEADER_CNT_VALUE_LSB = 0x15
ADDR_RX_PACKET_CNT_VALUE_MSB = 0x16
ADDR_RX_PACKET_CNT_VALUE_LSB = 0x17
ADDR_MODEM_STAT              = 0x18
ADDR_PKT_SNR_VALUE           = 0x19
ADDR_PKT_RSSI_VALUE          = 0x1A
ADDR_RSSI_VALUE              = 0x1B
ADDR_HOP_CHANNEL             = 0x1C
ADDR_MODEM_CONFIG_1          = 0x1D
ADDR_MODEM_CONFIG_2          = 0x1E
ADDR_SYMB_TIMEOUT_LSB        = 0x1F
ADDR_PREAMBLE_MSB            = 0x20
ADDR_PREAMBLE_LSB            = 0x21
ADDR_PAYLOAD_LENGTH          = 0x22
ADDR_MAX_PAYLOAD_LENGTH      = 0x23
ADDR_HOP_PERIOD              = 0x24
ADDR_FIFO_RX_BYTE_ADDR       = 0x25
ADDR_FEI_MSB                 = 0x28
ADDR_FEI_MID                 = 0x29
ADDR_FEI_LSB                 = 0x2A
ADDR_RSSI_WIDEBAND           = 0x2C
ADDR_DETECT_OPTIMIZE         = 0x31
ADDR_INVERT_IQ               = 0x33
ADDR_DETECTION_THRESHOLD     = 0x37
ADDR_SYNC_WORD               = 0x39
ADDR_INVERT_IQ_2             = 0x3B
ADDR_CHIRP_FILTER            = 0x3D

class LONGRANGEMODE(enum.IntEnum):
    _FSK_OOK = 0b0
    _LORA    = 0b1

class ACCESSSHAREDREG(enum.IntEnum):
    _LoRa = 0b0
    _XXK = 0b1

class MODE(enum.IntEnum):
    _SLEEP = 0b000
    _STDBY = 0b001
    _FSTX = 0b010
    _TX = 0b011
    _FSRX = 0b100
    _RXCONT = 0b101
    _RXSINGLE = 0b110
    _CAD = 0b111

REG_OP_MODE = bitstruct("REG_OP_MODE", 8, [
    ("MODE", 3),
    (None, 3),
    ("ACCESS_SHARED_REG", 1),
    ("LONG_RANGE_MODE", 1)
])

REG_IRQ_FLAGS_MASK = bitstruct("REG_IRQ_FLAGS_MASK", 8, [
    ("CAD_DETECTED_MASK", 1),
    ("FHSS_CHANGE_CHANNEL_MASK", 1),
    ("CAD_DONE_MASK", 1),
    ("TX_DONE_MASK", 1),
    ("VALID_HEADER_MASK", 1),
    ("PAYLOAD_CRC_ERROR_MASK", 1),
    ("RX_DONE_MASK", 1),
    ("RX_TIMEOUT_MASK", 1)
])

REG_IRQ_FLAGS = bitstruct("REG_IRQ_FLAGS", 8, [
    ("CAD_DETECTED", 1),
    ("FHSS_CHANGE_CHANNEL", 1),
    ("CAD_DONE", 1),
    ("TX_DONE", 1),
    ("VALID_HEADER", 1),
    ("PAYLOAD_CRC_ERROR", 1),
    ("RX_DONE", 1),
    ("RX_TIMEOUT", 1)
])

REG_MODEM_STAT = bitstruct("REG_MODEM_STAT", 8, [
    ("SIGNAL_DETECTED", 1),
    ("SIGNAL_SYNCHRONIZED", 1),
    ("RX_ONGOING", 1),
    ("HEADER_INFO_VALID", 1),
    ("MODEM_CLEAR", 1),
    ("RX_CODING_RATE", 3)
])

class PLLTIMEOUT(enum.IntEnum):
    _PLL_LOCK = 0b0
    _PLL_NO_LOCK = 0b1

REG_HOP_CHANNEL = bitstruct("REG_HOP_CHANNEL", 8, [
    ("FHSS_PRESENT_CHANNEL", 6),
    ("CRC_ON_PAYLOAD", 1),
    ("PLL_TIMEOUT", 1)
])

class MODEMBW(enum.IntEnum):
    _BW_125kHz = 0b00
    _BW_250kHz = 0b01
    _BW_500kHz = 0b10

class CODINGRATE(enum.IntEnum):
    _4_OVER_5 = 0b001
    _4_OVER_6 = 0b010
    _4_OVER_7 = 0b011
    _4_OVER_8 = 0b100

class HEADERMODE(enum.IntEnum):
    _EXPLICIT_HEADER = 0b0
    _IMPLICIT_HEADER = 0b1

REG_MODEM_CONFIG_1 = bitstruct("REG_MODEM_CONFIG_1", 8, [
    ("LOW_DATA_RATE_OPTIMIZE", 1),
    ("RX_PAYLOAD_CRC_ON", 1),
    ("IMPLICIT_HEADER_MODE_ON", 1),
    ("CODING_RATE", 3),
    ("BW", 2)
])

class SPREADINGFACTOR(enum.IntEnum):
    _SPREAD_6 = 6
    _SPREAD_7 = 7
    _SPREAD_8 = 8
    _SPREAD_9 = 9
    _SPREAD_10 = 10
    _SPREAD_11 = 11
    _SPREAD_12 = 12

class TXMODE(enum.IntEnum):
    _NORMAL = 0b0
    _CONTINUOUS = 0b1

class LNAGAINSOURCE(enum.IntEnum):
    _LNA_GAIN_REG = 0b0
    _LNA_GAIN_AGC = 0b1

REG_MODEM_CONFIG_2 = bitstruct("REG_MODEM_CONFIG_2", 8, [
    ("SYMB_TIMEOUT_MSB", 2),
    ("AGC_AUTO_ON", 1),
    ("TX_CONTINUOUS_MODE_ON", 1),
    ("SPREADING_FACTOR", 4)
])

REG_FEI_MSB = bitstruct("REG_FEI_MSB", 8, [
    ("FREQ_ERROR_MSB", 4),
    (None, 4)
])

class DETECTOPTIMIZE(enum.IntEnum):
    _SF7_TO_12 = 0x03
    _SF6 = 0x05

REG_DETECT_OPTIMIZE = bitstruct("REG_DETECT_OPTIMIZE", 8, [
    ("DETECTION_OPTIMIZE", 3),
    (None, 4),
    ("AUTOMATIC_IF_ON", 1)
])

REG_INVERT_IQ = bitstruct("REG_INVERT_IQ", 8, [
    ("INVERT_IQTX", 1),
    (None, 5),
    ("INVERT_IQRX", 1),
    (None, 1)
])

class DETECTIONTHRESHOLD(enum.IntEnum):
    _SF7_TO_12 = 0x0A
    _SF6 = 0x0C