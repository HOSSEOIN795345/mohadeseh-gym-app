[app]

title = MohadesehGym
package.name = mohadesegym
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,ttf

version = 0.1

requirements = python3==3.10.11,kivy==2.2.0

orientation = portrait

fullscreen = 0

android.api = 33
android.minapi = 24
android.ndk = 25b

android.permissions = INTERNET

[buildozer]

log_level = 2
warn_on_root = 1
