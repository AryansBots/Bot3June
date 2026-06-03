# This file is a part of NEO-WZML (github.com/irisXDR/NEO-WZML)
#
# Copy to `config.py` and fill in your values. `config.py` is git-ignored.
# BOT_TOKEN, TELEGRAM_API, TELEGRAM_HASH, OWNER_ID, DATABASE_URL, BASE_URL,
# UPSTREAM_REPO, UPSTREAM_BRANCH, AUTO_UPDATE and UPDATE_PKGS may also be set via env vars.

# REQUIRED
BOT_TOKEN = "8648384810:AAEDj7xlJlkfGsxtt8Yfm4VqWPftF8JljNg"
OWNER_ID = 8449664001
TELEGRAM_API = 5360874
TELEGRAM_HASH = "4631f40a1b26c2759bf1be4aff1df710"
DATABASE_URL = "mongodb+srv://kipsas449_db_user:hjo9dNUs3Bd5ar1C@cluster0.5vdpbkt.mongodb.net/?appName=Cluster0"  # mongodb:// or mongodb+srv:// URI

# General
DEFAULT_LANG = "en"
TG_PROXY = {}  # {"scheme": "socks5", "hostname": "", "port": 0, "username": "", "password": ""}
USER_SESSION_STRING = "BQHUiVYAc2dK2CCiOKAKBkZ-imlltsyxnZj0WcbwARAH-bmB-SNaqiyqbnYwCpWw8VSJEMiBlxILwJ6M2K-bIUyApk3VzCAkSfXHUvD7fDZQ-8cniWymYXZ6FfOVlaIZ0EhChGmfaGxae2fVt8dCZ4grPXbmtA6ZH5Gj4Fwu7q1tF1kwyyPnETdpoARKY0AmdZ7rlNFoiwYcPRscf28LaW63izZuXKKLXfZNXJWPac-VT_eFmnLkN6kY6xzPZ8_uJJfzLIrnoclNk8OFPaSYmywogRzkCwCX85vgAk0ZG2fMSAYrcTJwgHKi0wvCw3zktBQJXgFnIfEZWuyA-Tl3BDwCbl6wAAAAFpZhgmAA"
CMD_SUFFIX = ""
TIMEZONE = "UTC"

# Authorization
AUTHORIZED_CHATS = ""  # space-separated chat ids; empty = all
EXCEP_CHATS = ""
SUDO_USERS = "8449664001"
FORCE_SUB_IDS = "-1002896296138"
LOGIN_PASS = ""

# Status & defaults
STATUS_LIMIT = 10
STATUS_UPDATE_INTERVAL = 15
DEFAULT_UPLOAD = "rc"  # "rc" | "gd" | "ddl"
INCOMPLETE_TASK_NOTIFIER = False
EXCLUDED_EXTENSIONS = ""

# Bot behavior
BOT_PM = True
SET_COMMANDS = True
SHOW_EXTRA_CMDS = True
SAFE_MODE = False
STRICT_AUTH_MODE = False
STRICT_FILE_MODE = False
MEDIA_STORE = True
DELETE_LINKS = False
CLEAN_LOG_MSG = False

# Disable feature surfaces
DISABLE_TORRENTS = False
DISABLE_LEECH = False
DISABLE_BULK = False
DISABLE_MULTI = False
DISABLE_SEED = False
DISABLE_FF_MODE = False

# Limiters (0 = unlimited)
BOT_MAX_TASKS = 0
USER_MAX_TASKS = 0
USER_TIME_INTERVAL = 0
VERIFY_TIMEOUT = 0

# Task size limits in GB (0 = unlimited)
DIRECT_LIMIT = 0
MEGA_LIMIT = 0
TORRENT_LIMIT = 0
GDRIVE_LIMIT = 0  # download + upload
RCLONE_LIMIT = 0  # download + upload
CLONE_LIMIT = 0
JD_LIMIT = 0
YTDLP_LIMIT = 0
PLAYLIST_LIMIT = 0
LEECH_LIMIT = 0
EXTRACT_LIMIT = 0
ARCHIVE_LIMIT = 0
STORAGE_LIMIT = 0  # min free disk GB

# Queueing (0 = no cap)
QUEUE_ALL = 0
QUEUE_DOWNLOAD = 0
QUEUE_UPLOAD = 0

# Filename rules
MIRROR_PREFIX = ""
MIRROR_SUFFIX = ""
MIRROR_NAME_SWAP = ""
LEECH_NAME_SWAP = ""

# Leech
LEECH_SPLIT_SIZE = 0  # bytes; 0 = Telegram default
AS_DOCUMENT = False
EQUAL_SPLITS = False
MEDIA_GROUP = False
LEECH_PREFIX = ""
LEECH_SUFFIX = ""
LEECH_FONT = ""
CAP_FONT = "code"  # code | bold | italic
LEECH_CAPTION = "Thanks For Using WayneBots"
THUMBNAIL_LAYOUT = ""  # e.g. "3x4"
SAVE_MSG = False
SOURCE_LINK = False
SCREENSHOTS_MODE = False
SHOW_MEDIAINFO = True

# Custom command tables
FFMPEG_CMDS = {}
UPLOAD_PATHS = {}

# Log channels
LEECH_DUMP_CHAT = ""
LINKS_LOG_ID = ""
MIRROR_LOG_ID = ""

# Telegraph
AUTHOR_NAME = ""
AUTHOR_URL = ""

# Hyper TG (helper bot tokens, comma-separated)
HELPER_TOKENS = ""

# Mega
MEGA_EMAIL = ""
MEGA_PASSWORD = ""
MEGA_ENABLED = True

# JDownloader
JD_EMAIL = ""
JD_PASS = ""
JD_MODE = False

# Google Drive
GDRIVE_ID = ""
GD_DESP = "Uploaded with Wayne Bots"
IS_TEAM_DRIVE = False
USER_TD_MODE = False
USER_TD_SA = ""
STOP_DUPLICATE = False
DISABLE_DRIVE_LINK = False
INDEX_URL = ""
USE_SERVICE_ACCOUNTS = False
JIODRIVE_TOKEN = ""
GDTOT_CRYPT = ""

# Rclone
RCLONE_PATH = ""
RCLONE_FLAGS = ""
RCLONE_SERVE_URL = ""
RCLONE_SERVE_PORT = 0
RCLONE_SERVE_USER = ""
RCLONE_SERVE_PASS = ""
SHOW_CLOUD_LINK = True

# yt-dlp
YT_DLP_OPTIONS = ""  # JSON string, e.g. '{"format": "bv*+ba/b"}'

# DDL & link APIs
FILELION_API = ""
STREAMWISH_API = ""
INSTADL_API = ""
DEBRID_LINK_API = ""
REAL_DEBRID_API = ""

# Web UI / qBittorrent / Aria2c
BASE_URL = "0.0.0.0"  # public URL of this bot's web frontend
BASE_URL_PORT = 880
WEB_PINCODE = True
TORRENT_TIMEOUT = 0

# RSS
RSS_DELAY = 600
RSS_CHAT = ""
RSS_SIZE_LIMIT = 0

# Torrent search
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

# Self-update
UPSTREAM_REPO = "https://github.com/AryansBots/Bot3June"
UPSTREAM_BRANCH = "master"
AUTO_UPDATE = False
UPDATE_PKGS = True
UPGRADE_PACKAGES = False
