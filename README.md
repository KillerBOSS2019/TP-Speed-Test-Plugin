
# SpeedTest


![Downloads](https://img.shields.io/github/downloads/KillerBOSS2019/TP-Speed-Test-Plugin/total) 
![Forks](https://img.shields.io/github/forks/KillerBOSS2019/TP-Speed-Test-Plugin) 
![Stars](https://img.shields.io/github/stars/KillerBOSS2019/TP-Speed-Test-Plugin) 
![License](https://img.shields.io/github/license/KillerBOSS2019/TP-Speed-Test-Plugin)

- [SpeedTest](#SpeedTest)
  - [Description](#description)
  - [Settings Overview](#Settings-Overview)
  - [Features](#Features)
    - [Actions](#actions)
    - [States](#states)
  - [Installation Guide](#installation)
  - [Bugs and Support](#bugs-and-suggestion)
  - [License](#license)
  
# Description

SpeedTest Plugin using https://www.speedtest.net/ API for [TouchPortal](https://www.touch-portal.com/)

This documentation generated for SpeedTest V2000 with [Python TouchPortal SDK](https://github.com/KillerBOSS2019/TouchPortal-API).

## Settings Overview
### Auto Start
| Read-only | Type | Default Value | Max. Value |
| --- | --- | --- | --- |
| False | text | 0 | 360 |

Automatically start speedtest in minutes If entered number is greater than 5.

### Check Update
| Read-only | Type | Default Value |
| --- | --- | --- |
| False | text | True |

If I release any new update you will receive a TouchPortal notification about it.


# Features

## Actions
<details open><summary><b>Category:</b> main <ins>(Click to expand)</ins></summary><table>
<tr valign='buttom'><th>Action Name</th><th>Description</th><th>Format</th><th nowrap>Data<br/><div align=left><sub>choices/default (in bold)</th><th>On<br/>Hold</sub></div></th></tr>
<tr valign='top'><td>Start speedtest</td><td>Starts speedtest process.</td><td>Start speedtest using server [1]</td><td><ol start=1><li>Type: choice &nbsp; 
Default: <b>Best server (based on ping)</b></li>
</ol></td>
<td align=center>No</td>
</tr></table></details>
<br>

## States
<details open><summary><b>Base Id:</b> com.KillerBOSS.TPPlugins.TPSpeedTest <b>Category:</b> main <ins>(Click to expand)</ins></summary>


| Id | Description | DefaultValue | parentGroup |
| --- | --- | --- | --- |
| .st.result.download.bits | Download speed in (bits) |  | Download speed result |
| .st.result.download.bytes | Download speed in (bytes) |  | Download speed result |
| .st.result.download.kilobits | Download speed in (kilobits) |  | Download speed result |
| .st.result.download.kilobytes | Download speed in (kilobytes) |  | Download speed result |
| .st.result.download.megabits | Download speed in (megabits) |  | Download speed result |
| .st.result.download.megabytes | Download speed in (megabytes) |  | Download speed result |
| .st.result.upload.bits | Upload speed in (bits) |  | Upload speed result |
| .st.result.upload.bytes | Upload speed in (bytes) |  | Upload speed result |
| .st.result.upload.kilobits | Upload speed in (kilobits) |  | Upload speed result |
| .st.result.upload.kilobytes | Upload speed in (kilobytes) |  | Upload speed result |
| .st.result.upload.megabits | Upload speed in (megabits) |  | Upload speed result |
| .st.result.upload.megabytes | Upload speed in (megabytes) |  | Upload speed result |
| .st.result.ping | Ping |  |   |
| .st.result.isp | ISP |  |   |
| .st.result.image | Image |  |   |
</details>

<br>

# Installation
1. Download latest version of plugin for your system.
2. Import downloaded tpp by click the gear button next to email/notification icon.
3. If this is first plugin, you will need to restart TouchPortal for it to work.
# Bugs and Suggestion
Open an [issue](https://github.com/KillerBOSS2019/TP-Speed-Test-Plugin/issues) or join offical [TouchPortal Discord](https://discord.gg/MgxQb8r) for support.


# License
This plugin is licensed under the [GPL 3.0 License] - see the [LICENSE](LICENSE) file for more information.

