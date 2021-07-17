__Copyright__ = """
    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) 2021 DamienS

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import TouchPortalAPI
import speedtest
import threading
import requests
import base64
from TouchPortalAPI import Tools
import sys

TPClient = TouchPortalAPI.Client('SpeedTest')
running = True
global AutoStartTimer, AutoStart
AutoStart = True
servers = []
threads = None

@TPClient.on('info')
def main(client, data):
    global AutoStartTimer, AutoStart
    print(data)
    AutoStartTimer = data['settings'][1]['Auto Start in minutes']
    if data['settings'][0]['Auto Start'] == "True":
        AutoStart = True
    else:
        AutoStart = False
    updateStates()

        
@TPClient.on('settings')
def updateSettings(client,data):
    global AutoStartTimer, AutoStart
    AutoStartTimer = data['values'][1]['Auto Start in minutes']
    if data['values'][0]['Auto Start'] == "True":
        AutoStart = True
    else:
        AutoStart = False
    print(AutoStart)
    

def MainSpeedTest():
    try:
        SPT = speedtest.Speedtest()
        SPT.get_servers(servers)
        SPT.get_best_server()
        DownloadSpeed = SPT.download(threads=threads)
        UploadSpeed = SPT.upload(threads=threads,pre_allocate=False)
        SPT.results.share()
        results_dict = SPT.results.dict()
        downloadSpeed = [
            {
                'id': 'KillerBOSS.TPPlugins.SpeedTest.Download.Bits',
                'value': str(round(results_dict['download'], 2))
            },
            {
                'id': 'KillerBOSS.TPPlugins.SpeedTest.Download.Bytes',
                'value': str(round(results_dict['download'] / 8, 2))
            },
            {
                'id': 'KillerBOSS.TPPlugins.SpeedTest.Download.Kilobits',
                'value': str(round(results_dict['download'] / 1000, 2))
            },
            {
                'id': 'KillerBOSS.TPPlugins.SpeedTest.Download.Kilobytes',
                'value': str(round(results_dict['download'] / 8000, 2))
            },
            {
                'id': 'KillerBOSS.TPPlugins.SpeedTest.Download.Megabits',
                'value': str(round(results_dict['download'] / 1000000, 2))
            }
        ]
        TPClient.stateUpdateMany(downloadSpeed)
        
        uploadSpeed = [
            {
                "id": "KillerBOSS.TPPlugins.SpeedTest.Upload.Bits",
                "value": str(round(results_dict['upload'], 2))
            },
            {
                "id": "KillerBOSS.TPPlugins.SpeedTest.Upload.Bytes",
                "value": str(round(results_dict['upload'] / 8, 2))
            },
            {
                "id": "KillerBOSS.TPPlugins.SpeedTest.Upload.Kilobits",
                "value": str(round(results_dict['upload'] / 1000, 2))
            },
            {
                "id": "KillerBOSS.TPPlugins.SpeedTest.Upload.Kilobytes",
                "value": str(round(results_dict['upload'] / 8000, 2))
            },
            {
                "id": "KillerBOSS.TPPlugins.SpeedTest.Upload.Megabits",
                "value": str(round(results_dict['upload'] / 1000000, 2))
            }
        ]
        TPClient.stateUpdateMany(uploadSpeed)
        print("Done", results_dict)
    except Exception as e:
        print(e)


    extraData = [
        {
            "id": 'KillerBOSS.TPPlugins.SpeedTest.pings',
            "value": str(round(results_dict['ping'], 0))
        },
        {
            "id": 'KillerBOSS.TPPlugins.SpeedTest.ISP',
            "value": results_dict['client']['isp']
        },
        {
            "id": 'KillerBOSS.TPPlugins.SpeedTest.ImageData',
            "value": base64.b64encode(requests.get(results_dict['share']).content).decode('utf-8')
        }
        ]
    print(str(Tools.convertImage_to_base64(results_dict['share'])))
    TPClient.stateUpdateMany(extraData)

@TPClient.on('action')
def Actions(client,data):
    if data['actionId'] == 'KillerBOSS.TPPlugins.SpeedTest.Actions.TestAgain':
        MainSpeedTest()

def updateStates():
    global timer
    if running:
        if AutoStart:
            timer = threading.Timer(int(AutoStartTimer)*60, updateStates)
            MainSpeedTest()
        else:
            print("Auto Start is disabled")
            timer = threading.Timer(60, updateStates)
        timer.start()
    else:
        timer.cancel()
@TPClient.on('closePlugin')
def shutdown(client, data):
    global running
    print(data)
    timer.cancel()
    TPClient.disconnect()
    sys.exit()

TPClient.connect()
