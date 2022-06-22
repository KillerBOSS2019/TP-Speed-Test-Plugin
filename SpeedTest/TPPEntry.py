from TouchPortalAPI.tppbuild import *

__version__ = 2000
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
        'colorDark': '#000000',
        'colorLight': '#FFFFFF',
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
        "doc": "Automatically start speedtest in minutes If entered number is greater than 5."
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
    }
}

TP_PLUGIN_ACTIONS = {
    "Start speedtest": {
        "category": "main",
        "id": PLUGIN_ID + ".act.startTest",
        "name": "Start speedtest",
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
        "category": "main",
        "id": PLUGIN_ID + ".st.result.download.bits",
        "type": "text",
        "desc": "Download speed in (bits)",
        "parentGroup": "Download speed result",
        "default": "",
    },
    "result Download bytes": {
        "category": "main",
        "id": PLUGIN_ID + ".st.result.download.bytes",
        "type": "text",
        "desc": "Download speed in (bytes)",
        "parentGroup": "Download speed result",
        "default": "",
    },
    "result Download kilobits": {
        "category": "main",
        "id": PLUGIN_ID + ".st.result.download.kilobits",
        "type": "text",
        "desc": "Download speed in (kilobits)",
        "parentGroup": "Download speed result",
        "default": "",
    },
    "result Download kilobytes": {
        "category": "main",
        "id": PLUGIN_ID + ".st.result.download.kilobytes",
        "type": "text",
        "desc": "Download speed in (kilobytes)",
        "parentGroup": "Download speed result",
        "default": "",
    },
    "result Download megabits": {
        "category": "main",
        "id": PLUGIN_ID + ".st.result.download.megabits",
        "type": "text",
        "desc": "Download speed in (megabits)",
        "parentGroup": "Download speed result",
        "default": "",
    },
    "result Download megabytes": {
        "category": "main",
        "id": PLUGIN_ID + ".st.result.download.megabytes",
        "type": "text",
        "desc": "Download speed in (megabytes)",
        "parentGroup": "Download speed result",
        "default": "",
    },
    
    "result Upload bits": {
        "category": "main",
        "id": PLUGIN_ID + ".st.result.upload.bits",
        "type": "text",
        "desc": "Upload speed in (bits)",
        "parentGroup": "Upload speed result",
        "default": "",
    },
    "result Upload bytes": {
        "category": "main",
        "id": PLUGIN_ID + ".st.result.upload.bytes",
        "type": "text",
        "desc": "Upload speed in (bytes)",
        "parentGroup": "Upload speed result",
        "default": "",
    },
    "result Upload kilobits": {
        "category": "main",
        "id": PLUGIN_ID + ".st.result.upload.kilobits",
        "type": "text",
        "desc": "Upload speed in (kilobits)",
        "parentGroup": "Upload speed result",
        "default": "",
    },
    "result Upload kilobytes": {
        "category": "main",
        "id": PLUGIN_ID + ".st.result.upload.kilobytes",
        "type": "text",
        "desc": "Upload speed in (kilobytes)",
        "parentGroup": "Upload speed result",
        "default": "",
    },
    "result Upload megabits": {
        "category": "main",
        "id": PLUGIN_ID + ".st.result.upload.megabits",
        "type": "text",
        "desc": "Upload speed in (megabits)",
        "parentGroup": "Upload speed result",
        "default": "",
    },
    "result Upload megabytes": {
        "category": "main",
        "id": PLUGIN_ID + ".st.result.upload.megabytes",
        "type": "text",
        "desc": "Upload speed in (megabytes)",
        "parentGroup": "Upload speed result",
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
    }
}