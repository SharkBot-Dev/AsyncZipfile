import zipfile
import asyncio
import io
from pathlib import Path
from typing import List, Union

class AsyncZip:
    def __init__(self):
        pass

    async def create_zipfile(self, filename: str):
        def _create():
            with zipfile.ZipFile(filename, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
                pass
        await asyncio.to_thread(_create)

    async def write_zipfile(self, zipname: str, arcname: str, filepath: str = None, io_: io.BytesIO = None):
        def _write():
            with zipfile.ZipFile(zipname, 'a', compression=zipfile.ZIP_DEFLATED) as zf:
                if io_:
                    zf.writestr(arcname, io_.getvalue())
                elif filepath:
                    zf.write(filepath, arcname=arcname)
                else:
                    raise ValueError("filepath か io_ のどちらかを指定してください。")
        await asyncio.to_thread(_write)

    async def compress_files(
        self,
        zipname: str,
        files: List[Union[str, tuple[str, io.BytesIO]]]
    ):
        def _compress():
            with zipfile.ZipFile(zipname, "w", compression=zipfile.ZIP_DEFLATED) as zf:
                for f in files:
                    if isinstance(f, str):
                        zf.write(f, arcname=f)
                    elif isinstance(f, tuple) and isinstance(f[1], io.BytesIO):
                        arcname, bio = f
                        zf.writestr(arcname, bio.getvalue())
                    else:
                        raise ValueError("サポートされてないファイルが渡されました。")

        await asyncio.to_thread(_compress)

    async def extract_all(self, zipname: str, extract_dir: str):
        def _extract():
            with zipfile.ZipFile(zipname, "r") as zf:
                zf.extractall(path=extract_dir)
        await asyncio.to_thread(_extract)

    async def extract_file(self, zipname: str, filename: str) -> bytes:
        def _extract_file():
            with zipfile.ZipFile(zipname, "r") as zf:
                return zf.read(filename)
        return await asyncio.to_thread(_extract_file)