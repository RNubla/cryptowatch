# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['cryptowatch\\__main__.py'],
             pathex=['D:\\Programming\\Python\\cryptowatch'],
             binaries=[],
             datas=[('.\\assets\\*.ico', 'assets'), ('.\\preference.json', '.')],
             hiddenimports=['win10toast', 'cryptocompare'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='cryptowatch-0.0.1-win32',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
