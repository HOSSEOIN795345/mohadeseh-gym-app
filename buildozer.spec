[app]

title = Mohadeseh Gym
package.name = mohadesehgym
package.domain = org.mohadeseh

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 1

android.api = 33
android.minapi = 24

android.permissions = INTERNET

android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True
android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1
