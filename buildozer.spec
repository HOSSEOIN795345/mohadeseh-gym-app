[app]

title = Mohadeseh Gym

package.name = mohadesehgym

package.domain = org.mohadeseh


source.dir = .


source.include_exts = py,png,jpg,kv,atlas,json,mp3,ttf,wav


version = 1.0


requirements = python3,kivy==2.3.1,cython==0.29.36


orientation = portrait


fullscreen = 0



# Android

android.api = 35

android.minapi = 23

android.ndk = 25b

android.build_tools_version = 35.0.0


android.accept_sdk_license = True


android.archs = arm64-v8a,armeabi-v7a


android.enable_androidx = True



# permissions

android.permissions = INTERNET,VIBRATE



# assets

presplash.filename = assets/icon.png

icon.filename = assets/icon.png



# logging

log_level = 2



[buildozer]

log_level = 2
