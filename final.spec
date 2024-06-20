# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/Users/robot/Documents/GitHub/JBNU_PPP_2024/final/final.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/robot/Documents/GitHub/JBNU_PPP_2024/final/mirrored_positions.json', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='final',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
