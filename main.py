from volume_control import *
from brightness_control import *
from bluetooth_test_client import *

async def getPoints(client):
    currentPCVolume = await getVolume("Speakers (Realtek(R) Audio)")
    currentRoomVolume = await client.get_volume()

    currentPCBrightness = await getBrightness()
    currentRoomBrightness = await client.get_brightness()

    return [[currentPCVolume, currentRoomVolume], [currentPCBrightness, currentRoomBrightness]]

async def brightness(client, p1, p2):
    currentBrightness = await client.get_brightness()
    slope = (p1[1] - p2[1]) / (p1[0] - p2[0])
    setBrightnessTo = slope * (currentBrightness - p1[0]) + p1[1]
    if setBrightnessTo < 0:
        setBrightnessTo = 0
    elif setBrightnessTo > 100:
        setBrightnessTo = 100
    print(f"set brightness: {setBrightnessTo}")
    await setBrightness(setBrightnessTo)


async def volume(client, p1, p2):
    currentVolume = await client.get_volume()
    slope = (p1[1] - p2[1]) / (p1[0] - p2[0])
    setVolumeTo = slope * (currentVolume - p1[0]) + p1[1]
    if setVolumeTo < 0:
        setVolumeTo = 0
    elif setVolumeTo > 100:
        setVolumeTo = 100
    print(currentVolume)
    await setVolume(setVolumeTo, "Speakers (Realtek(R) Audio)")


async def main():
    client = NsBleClient()
    await client.discover_and_connect()

    flag = 0

    while flag != 'Y':
        flag = input("Are you ready to collect the first point? (Y/N)")
    point1Array = await getPoints(client)

    flag = 0

    while flag != 'Y':
        flag = input("Are you ready to collect the second point? (Y/N)")
    point2Array = await getPoints(client)


    volumeP1 = point1Array[0]
    volumeP2 = point2Array[0]

    brightnessP1 = point1Array[1]
    brightnessP2 = point2Array[1]

    while True:
        await brightness(client, brightnessP1, brightnessP2)
        await asyncio.sleep(1)
        await volume(client, volumeP1, volumeP2)
        await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(main())
