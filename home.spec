# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:\\Users\\joy84\\OneDrive\\文件\\GitHub\\TKMeatMG\\home.py'],
    pathex=[],
    binaries=[],
    datas=[('Y:\\anaconda3\\envs\\tkinter\\Lib\\site-packages\\customtkinter', 'customtkinter/'), ('Y:\\anaconda3\\envs\\tkinter\\Lib\\site-packages\\tkcalendar', 'tkcalendar/'), ('Y:\\anaconda3\\envs\\tkinter\\Lib\\site-packages\\babel', 'babel/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='home',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='home',
)
