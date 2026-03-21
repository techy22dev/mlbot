# REQUIRED CONFIG
BOT_TOKEN = "8790597478:AAH86Jgh7o82T2ZnSM7_j2kZqiArtT8H13E"
OWNER_ID = 989262779
TELEGRAM_API = 17545386
TELEGRAM_HASH = "f1d5ee6adccd34db0aab30115f4c30db"
# OPTIONAL CONFIG
TG_PROXY = {}
USER_SESSION_STRING = ""
CMD_SUFFIX = ""
AUTHORIZED_CHATS = "-1001970217512"
SUDO_USERS = "989262779"
DATABASE_URL = "mongodb+srv://justin22:Subash7550@cluster0.3zj66gf.mongodb.net/?appName=Cluster0"
DATABASE_NAME = "mltb"
STATUS_LIMIT = 4
DEFAULT_UPLOAD = "rc"
STATUS_UPDATE_INTERVAL = 10
FILELION_API = ""
STREAMWISH_API = ""
EXCLUDED_EXTENSIONS = ""
INCLUDED_EXTENSIONS = ""
INCOMPLETE_TASK_NOTIFIER = False
YT_DLP_OPTIONS = ""
USE_SERVICE_ACCOUNTS = False
NAME_SUBSTITUTE = r""
FFMPEG_CMDS = {"merge": ["-f concat -safe 0 -i mltb.txt -c copy mltb.mp4 -del"]}
UPLOAD_PATHS = {}
# GDrive Tools
GDRIVE_ID = ""
IS_TEAM_DRIVE = False
STOP_DUPLICATE = False
INDEX_URL = ""
# Rclone
RCLONE_PATH = ""
RCLONE_FLAGS = ""
RCLONE_SERVE_URL = ""
RCLONE_SERVE_PORT = 0
RCLONE_SERVE_USER = ""
RCLONE_SERVE_PASS = ""
# JDownloader
JD_EMAIL = ""
JD_PASS = ""
# Sabnzbd
USENET_SERVERS = [
    {
        "name": "main",
        "host": "",
        "port": 563,
        "timeout": 60,
        "username": "",
        "password": "",
        "connections": 8,
        "ssl": 1,
        "ssl_verify": 2,
        "ssl_ciphers": "",
        "enable": 1,
        "required": 0,
        "optional": 0,
        "retention": 0,
        "send_group": 0,
        "priority": 0,
    }
]
# Nzb search
HYDRA_IP = ""
HYDRA_API_KEY = ""
# Update
UPSTREAM_REPO = ""
UPSTREAM_BRANCH = "master"
# Leech
LEECH_SPLIT_SIZE = 2
AS_DOCUMENT = False
EQUAL_SPLITS = False
MEDIA_GROUP = False
USER_TRANSMISSION = False
HYBRID_LEECH = False
LEECH_FILENAME_PREFIX = ""
LEECH_DUMP_CHAT = "-1001970217512"
CLONE_DUMP_CHATS = "-1001970217512"
FILES_LINKS = False
THUMBNAIL_LAYOUT = ""
# qBittorrent/Aria2c
TORRENT_TIMEOUT = 0
BASE_URL = ""
BASE_URL_PORT = 0
WEB_PINCODE = False
# Queueing system
QUEUE_ALL = 0
QUEUE_DOWNLOAD = 0
QUEUE_UPLOAD = 0
# RSS
RSS_DELAY = 600
RSS_CHAT = ""
RSS_SIZE_LIMIT = 0
# Torrent Search
SEARCH_API_LINK = ""
SEARCH_LIMIT = 0
SEARCH_PLUGINS = [
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/piratebay.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/limetorrents.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torlock.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torrentscsv.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/eztv.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torrentproject.py",
    "https://raw.githubusercontent.com/MaurizioRicci/qBittorrent_search_engines/master/kickass_torrent.py",
    "https://raw.githubusercontent.com/MaurizioRicci/qBittorrent_search_engines/master/yts_am.py",
    "https://raw.githubusercontent.com/MadeOfMagicAndWires/qBit-plugins/master/engines/linuxtracker.py",
    "https://raw.githubusercontent.com/MadeOfMagicAndWires/qBit-plugins/master/engines/nyaasi.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/ettv.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/glotorrents.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/thepiratebay.py",
    "https://raw.githubusercontent.com/v1k45/1337x-qBittorrent-search-plugin/master/leetx.py",
    "https://raw.githubusercontent.com/nindogo/qbtSearchScripts/master/magnetdl.py",
    "https://raw.githubusercontent.com/msagca/qbittorrent_plugins/main/uniondht.py",
    "https://raw.githubusercontent.com/khensolomon/leyts/master/yts.py",
]
