[app]

title = Mohadeseh Gym

package.name = mohadesehgym

package.domain = org.mohadeseh

source.dir = .

source.include_exts = py,png,jpg,kv,atlas,ttf,json,mp3,wav

version = 1.0

requirements = python3,kivy==2.3.1

orientation = portrait

fullscreen = 0


# Android

android.api = 34

android.minapi = 23

android.ndk = 25b

android.archs = arm64-v8a


# permissions

android.permissions = INTERNET


# icon اگر نداری کامنت بماند
# icon.filename = %(source.dir)s/icon.png


[buildozer]

log_level = 2

warn_on_root = 1
