# AX3 160 MHz Fix

The Huawei AX3 sometimes drops its 5 GHz bandwidth back to 80 MHz (probably a firmware bug).

`SET_BW_160MHz.py` logs into the router web UI and sets the 5 GHz bandwidth back to 20/40/80/160 MHz.

## Setup

```
pip install playwright
playwright install chromium
```

Set `ROUTER` and `PASSWORD` at the top of the script.

## Run

```
python3 SET_BW_160MHz.py
```
