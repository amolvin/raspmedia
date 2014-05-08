# UDP config
UDP_HOST = ""
UDP_PORT = 60005
UDP_BROADCAST_HOST = '<broadcast>'

# predefined message flags
CONFIG_UPDATE = 0x00
PLAYER_START = 0x01
PLAYER_STOP = 0x02
SERVER_REQUEST = 0x03
FILELIST_REQUEST = 0x04
FILELIST_RESPONSE = 0x05
CONFIG_REQUEST = 0x06
DELETE_FILE = 0x07
PLAYER_IDENTIFY = 0x08
PLAYER_IDENTIFY_DONE = 0x10

# msg interpreter result
INTERPRETER_SUCCESS = 0xf00
INTERPRETER_SERVER_REQUEST = 0xf01
INTERPRETER_ERROR = 0xf02
INTERPRETER_FILELIST_REQUEST = 0xf03
INTERPRETER_FILELIST_RESPONSE = 0xf04

# player states
PLAYER_STARTED = 0x80
PLAYER_STOPPED = 0x81
PLAYER_STATE_UNDEFINED = 0x82

# filetypes
SUPPORTED_IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.JPG', '.JPEG', '.png', '.PNG')
SUPPORTED_VIDEO_EXTENSIONS = ('.mp4', '.m4v', '.mpeg', '.mpg', '.mpeg1', '.mpeg4')
