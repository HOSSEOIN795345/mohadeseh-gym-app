[app]

title = Mohadeseh Gym

package.name = mohadesehgym

package.domain = org.mohadeseh

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,mp3,json,wav

version = 1.0

requirements = python3,kivy==2.3.1

orientation = portrait

fullscreen = 0

android.api = 34

android.minapi = 23

android.ndk = 25b

android.archs = arm64-v8a

android.accept_sdk_license = True

android.permissions = INTERNET

p4a.bootstrap = sdl2

android.add_src = .

[buildozer]

log_level = 2
