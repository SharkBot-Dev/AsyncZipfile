# AsyncZipfile
zipfileというライブラリを非同期で使えるようにしたものです。

# 使い方
```
import async_zip
import asyncio

async def main():
    zip = async_zip.AsyncZip()
    await zip.create_zipfile('test.zip') # zipファイルを作成
    await zip.write_zipfile('test.zip', 'test.txt', 'test.txt') # test.txtをtest.txtという名前でzipに保存

    await zip.extract_all('test.zip', 'test') # zipをtestに解凍

asyncio.run(main())
```