from TouchPortalAPI.tppbuild import *

__version__ = 2002
PLUGIN_ID = "com.KillerBOSS.TPPlugins.TPSpeedTest"

TPSDK_DEFAULT_VERSION = 6

TP_PLUGIN_INFO = {
    'sdk': 6,
    'version': __version__,
    'name': "SpeedTest",
    "id": PLUGIN_ID,
    'plugin_start_cmd_windows': "%TP_PLUGIN_FOLDER%TPSpeedTest\\TPSpeedtest.exe",
    'plugin_start_cmd_linux': "sh %TP_PLUGIN_FOLDER%TPSpeedTest\\start.sh",
    'plugin_start_cmd_mac': "sh %TP_PLUGIN_FOLDER%TPSpeedTest\\start.sh",
    'configuration': {
        'colorDark': '#0d162c',
        'colorLight': '#4b84f3',
    },
    "doc": {
        "repository": "KillerBOSS2019:TP-Speed-Test-Plugin",
        "Install": "1. Download latest version of plugin for your system.\n2. Import downloaded tpp by click the gear button next to email/notification icon.\n3. If this is first plugin, you will need to restart TouchPortal for it to work.",
        "description": "SpeedTest Plugin using https://www.speedtest.net/ API for [TouchPortal](https://www.touch-portal.com/)"
    }
}

TP_PLUGIN_SETTINGS = {
    "Auto Start": {
        "name": "Auto Start SpeedTest",
        "type": "text",
        "minValue": 0,
        "maxValue": 360,
        "default": "0",
        "readOnly": False,
        "doc": "In order to enable automatically test you will need to enter a number that's equal or greater than 5. Otherwise It means it's disabled."
    },
    "Check Update": {
        "name": "Auto Check Update",
        "type": "text",
        "default": "True",
        "readOnly": False,
        "doc": "If I release any new update you will receive a TouchPortal notification about it."
    }
}

TP_PLUGIN_CATEGORIES = {
    "main": {
        "id": PLUGIN_ID + ".main",
        "name": "Touch Portal SpeedTest",
        "imagepath": "%TP_PLUGIN_FOLDER%TPSpeedTest\\icon.png",
    },
    "download": {
        "id": PLUGIN_ID + ".download",
        "name": "Download Speed Results"
    },
    "upload": {
        "id": PLUGIN_ID + ".upload",
        "name": "Upload Speed Results"
    }
}

TP_PLUGIN_ACTIONS = {
    "Start Speedtest": {
        "category": "main",
        "id": PLUGIN_ID + ".act.startTest",
        "name": "Start Speedtest",
        "prefix": TP_PLUGIN_CATEGORIES["main"]["name"],
        "type": "communicate",
        "tryInline": True,
        "format": "Start speedtest using server $[1]",
        "doc": "Starts speedtest process.",
        "data": {
            "SpeedtestServer": {
                "id": PLUGIN_ID + ".act.startTest.servers",
                "type": "choice",
                "label": "Speedtest Server",
                "default": "Best server (based on ping)",
                "valueChoices": []
            }
        }
    },
}

TP_PLUGIN_STATES = {
    "result Download bits": {
        "category": "download",
        "id": PLUGIN_ID + ".st.result.download.bits",
        "type": "text",
        "desc": "Download speed in (bits)",
        "default": "",
    },
    "result Download bytes": {
        "category": "download",
        "id": PLUGIN_ID + ".st.result.download.bytes",
        "type": "text",
        "desc": "Download speed in (bytes)",
        "default": "",
    },
    "result Download kilobits": {
        "category": "download",
        "id": PLUGIN_ID + ".st.result.download.kilobits",
        "type": "text",
        "desc": "Download speed in (kilobits)",
        "default": "",
    },
    "result Download kilobytes": {
        "category": "download",
        "id": PLUGIN_ID + ".st.result.download.kilobytes",
        "type": "text",
        "desc": "Download speed in (kilobytes)",
        "default": "",
    },
    "result Download megabits": {
        "category": "download",
        "id": PLUGIN_ID + ".st.result.download.megabits",
        "type": "text",
        "desc": "Download speed in (megabits)",
        "default": "",
    },
    "result Download megabytes": {
        "category": "download",
        "id": PLUGIN_ID + ".st.result.download.megabytes",
        "type": "text",
        "desc": "Download speed in (megabytes)",
        "default": "",
    },
    
    "result Upload bits": {
        "category": "upload",
        "id": PLUGIN_ID + ".st.result.upload.bits",
        "type": "text",
        "desc": "Upload speed in (bits)",
        "default": "",
    },
    "result Upload bytes": {
        "category": "upload",
        "id": PLUGIN_ID + ".st.result.upload.bytes",
        "type": "text",
        "desc": "Upload speed in (bytes)",
        "default": "",
    },
    "result Upload kilobits": {
        "category": "upload",
        "id": PLUGIN_ID + ".st.result.upload.kilobits",
        "type": "text",
        "desc": "Upload speed in (kilobits)",
        "default": "",
    },
    "result Upload kilobytes": {
        "category": "upload",
        "id": PLUGIN_ID + ".st.result.upload.kilobytes",
        "type": "text",
        "desc": "Upload speed in (kilobytes)",
        "default": "",
    },
    "result Upload megabits": {
        "category": "upload",
        "id": PLUGIN_ID + ".st.result.upload.megabits",
        "type": "text",
        "desc": "Upload speed in (megabits)",
        "default": "",
    },
    "result Upload megabytes": {
        "category": "upload",
        "id": PLUGIN_ID + ".st.result.upload.megabytes",
        "type": "text",
        "desc": "Upload speed in (megabytes)",
        "default": "",
    },

    "result Ping": {
        "category": "main",
        "id": PLUGIN_ID + ".st.result.ping",
        "name": "Ping",
        "type": "text",
        "desc": "Ping",
        "default": "",
    },
    "result ISP": {
        "category": "main",
        "id": PLUGIN_ID + ".st.result.isp",
        "name": "ISP",
        "type": "text",
        "desc": "ISP",
        "default": "",
    },
    "result Image": {
        "category": "main",
        "id": PLUGIN_ID + ".st.result.image",
        "name": "Image",
        "type": "text",
        "desc": "Image",
        "default": "",
    },
    "Speed Test Status": {
        "category": "main",
        "id": PLUGIN_ID + ".st.status",
        "name": "Speed Test Status",
        "type": "text",
        "desc": "Plugin Status",
        "default": "",
    },
    "Speed Test Server": {
        "category": "main",
        "id": PLUGIN_ID + ".st.server",
        "name": "Speed Test Server",
        "type": "text",
        "desc": "Speed Test Server",
        "default": "",
    }
}
