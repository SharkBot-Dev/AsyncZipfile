import async_zip
import asyncio

async def main():
    zip = async_zip.AsyncZip()
    await zip.create_zipfile('test.zip')
    await zip.write_zipfile('test.zip', 'test.txt', 'test.txt')

    await zip.extract_all('test.zip', 'test')

asyncio.run(main())