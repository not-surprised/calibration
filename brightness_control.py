import screen_brightness_control as sbc

async def setBrightness(brightness):
    current_brightness = sbc.get_brightness()
    sbc.fade_brightness(brightness, start=current_brightness)

async def setBrightness2(brightness, monitor):
    current_brightness =sbc.get_brightness()
    monitors = sbc.list_monitors()
    sbc.set_brightness(brightness, display=monitors[monitor])

async def getBrightness():
    return sbc.get_brightness()

async def getBrightness2(monitor):
    return sbc.get_brightness(monitor)

async def getMonitors():
    monitors = sbc.list_monitors()
    return monitors

# monitors = getMonitors()
# print(monitors)
# brightness = getBrightness()
# print(brightness)
# setBrightness(brightness - 20)
# # setBrightness2(brightness + 20, 0)