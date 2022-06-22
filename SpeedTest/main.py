# import speedtest

# sptest = speedtest.Speedtest()

# servers = sorted(sptest.get_servers().items())

# for _, servers in servers:
#     for server in servers:
#         line = ('%(id)5s) %(sponsor)s (%(name)s, %(country)s) '
#                 '[%(d)0.2f km]' % server)
#         print(line)

# print(sptest.config)

import subprocess
import sys
from argparse import ArgumentParser
from threading import Thread
from time import sleep

import speedtest
import TouchPortalAPI
from TouchPortalAPI import TYPES, Tools
from TouchPortalAPI.logger import Logger

from TPPEntry import *

autoStartTest = 0
running = True

TPClient = TouchPortalAPI.Client(TP_PLUGIN_INFO["id"])
g_log = Logger(TP_PLUGIN_INFO["id"])

def updateResult(result):
    downloadSpeedState = [
        {
            "id": TP_PLUGIN_STATES["result Download bits"]["id"],
            "value": str(round(result['download'], 2))
        },
        {
            "id": TP_PLUGIN_STATES["result Download bytes"]["id"],
            "value": str(round(result['download'] / 8, 2))
        },
        {
            "id": TP_PLUGIN_STATES["result Download kilobits"]["id"],
            "value": str(round(result['download'] / 1000, 2))
        },
        {
            "id": TP_PLUGIN_STATES["result Download kilobytes"]["id"],
            "value": str(round(result['download'] / 8000, 2))
        },
        {
            "id": TP_PLUGIN_STATES["result Download megabits"]["id"],
            "value": str(round(result['download'] / 1000000, 2))
        },
        {
            "id": TP_PLUGIN_STATES["result Download megabytes"]["id"],
            "value": str(round(result['download'] / 8000000, 2))
        }
    ]
    TPClient.stateUpdateMany(downloadSpeedState)
    
    uploadSpeedState = [
        {
            "id": TP_PLUGIN_STATES["result Upload bits"]["id"],
            "value": str(round(result['upload'], 2))
        },
        {
            "id": TP_PLUGIN_STATES["result Upload bytes"]["id"],
            "value": str(round(result['upload'] / 8, 2))
        },
        {
            "id": TP_PLUGIN_STATES["result Upload kilobits"]["id"],
            "value": str(round(result['upload'] / 1000, 2))
        },
        {
            "id": TP_PLUGIN_STATES["result Upload kilobytes"]["id"],
            "value": str(round(result['upload'] / 8000, 2))
        },
        {
            "id": TP_PLUGIN_STATES["result Upload megabits"]["id"],
            "value": str(round(result['upload'] / 1000000, 2))
        },
        {
            "id": TP_PLUGIN_STATES["result Upload megabytes"]["id"],
            "value": str(round(result['upload'] / 8000000, 2))
        }
    ]
    TPClient.stateUpdateMany(uploadSpeedState)

    TPClient.stateUpdate(TP_PLUGIN_STATES["result Ping"]["id"], str(round(result['ping'], 0)))
    TPClient.stateUpdate(TP_PLUGIN_STATES["result ISP"]["id"], result['client']['isp'])
    TPClient.stateUpdate(TP_PLUGIN_STATES["result Image"]["id"], Tools.convertImage_to_base64(result["share"], type="Web"))

def getServers():
    sptest = speedtest.Speedtest()
    servers = sorted(sptest.get_servers().items())
    server_list = {}
    for _, servers in servers:
        for server in servers:
            line = ('%(sponsor)s (%(name)s, %(country)s) '
                        '[%(d)0.2f km]' % server)
            server_list[line] = server['id']
    return server_list

def startSpeedTest(server):
    sptest = speedtest.Speedtest()
    serverlist = getServers()

    if not TPClient.choiceUpdateList[TP_PLUGIN_ACTIONS["Start speedtest"]["data"]["SpeedtestServer"]["id"]] == list(serverlist.keys()):
        TPClient.stateUpdate(TP_PLUGIN_ACTIONS["Start speedtest"]["data"]["SpeedtestServer"]["id"], list(serverlist.keys()))

    if server == "Best server (based on ping)":
        sptest.get_best_server()
    else:
        sptest.get_servers([serverlist[server]])
    g_log.debug("start to test")

    sptest.download()
    sptest.upload()
    sptest.results.share()

    result = sptest.results.dict()
    updateResult(result)

def speedTestTracker():
    while running:
        if autoStartTest >= 5:
            g_log.info(f"Waiting {autoStartTest*60} seconds before starting speedtest.")
            sleep(60*autoStartTest) # convert input to minutes
            try:
                startSpeedTest("Best server (based on ping)")
            except Exception as e:
                g_log.error(f"Error Starting speedtest {e}")


def settingsHandler(settings:list):
    global autoStartTest

    try:
        autoStartTest = int(settings[0]['Auto Start SpeedTest'])
    except (ValueError, IndexError):
        autoStartTest = 0


# Event handler

speedtestThread = Thread(target=speedTestTracker, daemon=True)

@TPClient.on(TYPES.onConnect)
def onStart(data):
    g_log.info(f"Connected to TP v{data.get('tpVersionString', '?')}, plugin v{data.get('pluginVersion', '?')}.")
    g_log.debug(f"Connection: {data}")

    settingsHandler(data.get('settings', []))

    servers = getServers()
    TPClient.choiceUpdate(TP_PLUGIN_ACTIONS["Start speedtest"]["data"]["SpeedtestServer"]["id"], list(servers.keys()))

    # checking for update
    github_check = Tools.updateCheck("KillerBOSS2019", "TP-Speed-Test-Plugin")
    versionInt = int("".join(github_check.split(".")))
    
    if versionInt > data.get("pluginVersion"):
        g_log.debug(f"Found new version of speedtest plugin: {github_check}")
        if data['settings'][1]['Auto Check Update'].lower() == "true":
            g_log.debug("Auto update is enabled. sending user notification")
            TPClient.showNotification(
                notificationId=TP_PLUGIN_INFO["id"] + ".updateNotification",
                title=f"Speedtest Plugin V{github_check} is available",
                msg="A new Speedtest plugin Version is available and ready to Download. This may include Bug Fixes and or New Features",
                options= [{
                "id":TP_PLUGIN_INFO["id"] + ".updateNotification.downloadButton",
                "title":"Click here to Update"
                }])

    speedtestThread.start()

@TPClient.on(TYPES.onNotificationOptionClicked)
def notificationOption(data):
    g_log.debug("Notification option: ", data)
    if data['optionId'] == TP_PLUGIN_INFO["id"] + ".updateNotification.downloadButton":
        g_log.debug("User clicked download button")
        github_check = TouchPortalAPI.Tools.updateCheck("KillerBOSS2019", "TP-Speed-Test-Plugin")
        subprocess.run(f"Start https://github.com/KillerBOSS2019/TP-Speed-Test-Plugin/releases/tag/{github_check}", stdout=subprocess.PIPE, shell=True)

@TPClient.on(TYPES.onSettingUpdate)
def onSettingEvent(data):
    g_log.debug(f"Settings: {data}")
    settingsHandler(data.get('values', []))

@TPClient.on(TYPES.onAction)
def onAction(data):
    g_log.debug(f"Action: {data}")

    if data['actionId'] == TP_PLUGIN_ACTIONS["Start speedtest"]["id"]:
        startSpeedTest(data['data'][0]['value'])

# Shutdown handler
@TPClient.on(TYPES.onShutdown)
def onShutdown(data):
    g_log.info('Received shutdown event from TP Client.')

# Error handler
@TPClient.on(TYPES.onError)
def onError(exc):
    g_log.error(f'Error in TP Client event handler: {repr(exc)}')

def main():
    global TPClient, g_log, running
    ret = 0

    # default log file destination
    logFile = f"./{PLUGIN_ID}.log"
    # default log stream destination
    logStream = sys.stdout

    # Set up and handle CLI arguments. These all relate to logging options.
    # The plugin can be run with "-h" option to show available argument options.
    # Addtionally, a file constaining any of these arguments can be specified on the command line
    # with the `@` prefix. For example: `plugin-example.py @config.txt`
    # The file must contain one valid argument per line, including the `-` or `--` prefixes.
    # See the plugin-example-conf.txt file for an example config file.
    parser = ArgumentParser(fromfile_prefix_chars='@')
    parser.add_argument("-d", action='store_true',
                        help="Use debug logging.")
    parser.add_argument("-w", action='store_true',
                        help="Only log warnings and errors.")
    parser.add_argument("-q", action='store_true',
                        help="Disable all logging (quiet).")
    parser.add_argument("-l", metavar="<logfile>", 
                        help=f"Log file name (default is '{logFile}'). Use 'none' to disable file logging.")
    parser.add_argument("-s", metavar="<stream>",
                        help="Log to output stream: 'stdout' (default), 'stderr', or 'none'.")

    # his processes the actual command line and populates the `opts` dict.
    opts = parser.parse_args()
    del parser

    # trim option string (they may contain spaces if read from config file)
    opts.l = opts.l.strip() if opts.l else 'none'
    opts.s = opts.s.strip().lower() if opts.s else 'stdout'
    print(opts)

    # Set minimum logging level based on passed arguments
    logLevel = "INFO"
    if opts.q: logLevel = None
    elif opts.d: logLevel = "DEBUG"
    elif opts.w: logLevel = "WARNING"

    # set log file if -l argument was passed
    if opts.l:
        logFile = None if opts.l.lower() == "none" else opts.l
    # set console logging if -s argument was passed
    if opts.s:
        if opts.s == "stderr": logStream = sys.stderr
        elif opts.s == "stdout": logStream = sys.stdout
        else: logStream = None

    # Configure the Client logging based on command line arguments.
    # Since the Client uses the "root" logger by default,
    # this also sets all default logging options for any added child loggers, such as our g_log instance we created earlier.
    TPClient.setLogFile(logFile)
    TPClient.setLogStream(logStream)
    TPClient.setLogLevel(logLevel)

    # ready to go
    g_log.info(f"Starting {TP_PLUGIN_INFO['name']} v{TP_PLUGIN_INFO['version']} on {sys.platform}.")

    try:
        TPClient.connect()
        g_log.info('TP Client closed.')
    except KeyboardInterrupt:
        g_log.warning("Caught keyboard interrupt, exiting.")
    except Exception:
        from traceback import format_exc
        g_log.error(f"Exception in TP Client:\n{format_exc()}")
        ret = -1
    finally:
        TPClient.disconnect()

    del TPClient
    running = False

    g_log.info(f"{TP_PLUGIN_INFO['name']} stopped.")
    return ret

if __name__ == "__main__":
    sys.exit(main())