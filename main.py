from volume_control import *
from brightness_control import *
from bluetooth_test_client import *

def clamp01(x):
    return min(1, max(0, x))

async def brightness(client):
    currentBrightness = await client.get_brightness()
    print(currentBrightness)
    await setBrightness(clamp01(currentBrightness/500) * 255)


async def volume(client):
    currentVolume = await client.get_volume()
    if currentVolume < 0:
        currentVolume = 0
    elif currentVolume > 60:
        currentVolume = 60
    print(currentVolume)
    await setVolume(currentVolume, "Speakers (Realtek(R) Audio)")


async def main():
    client = NsBleClient()
    await client.discover_and_connect()
    while True:
        await brightness(client)
        await asyncio.sleep(1)
        await volume(client)
        await asyncio.sleep(1)



async def test():
    client = NsBleClient()
    await client.discover_and_connect()
    for i in range(10):
        print(await client.get_brightness())

        await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(main())
