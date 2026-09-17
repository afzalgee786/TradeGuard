[app]
title = TradeGuard
package.name = tradeguard
package.domain = com.tradeguard.app
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.permissions = INTERNET
android.ant = auto
p4a.bootstrap = sdl2
p4a.port = 8000

[buildozer]
log_level = 2
warn_on_root = 1
