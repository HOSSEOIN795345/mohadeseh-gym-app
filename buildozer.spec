[app]

# (str) Title of your application
title = Mohadeseh Gym


# (str) Package name
package.name = mohadesehgym


# (str) Package domain
package.domain = org.mohadeseh


# (str) Source code where main.py lives
source.dir = .


# (list) Source files to include
source.include_exts = py,kv,png,jpg,jpeg,ttf,mp3,json,atlas


# (str) Application version
version = 1.0


# (list) Application requirements
requirements = python3,kivy==2.3.1


# (str) Supported orientation
orientation = portrait


# (bool) Allow fullscreen
fullscreen = 0



# (str) Presplash
# presplash.filename = %(source.dir)s/assets/presplash.png


# (str) Icon
# icon.filename = %(source.dir)s/assets/icon.png



#
# Android specific
#

# (bool) Indicate if the application should be built for Android
android.api = 34

android.minapi = 23

android.ndk = 25b

android.archs = arm64-v8a


# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity


# (bool) Enable Android permissions
android.permissions = INTERNET



#
# Python-for-android
#

p4a.branch = master


#
# Logging
#

log_level = 2


#
# Build settings
#

warn_on_root = 1


#
# iOS
#

# ios.kivy_ios_dir = ../kivy-ios


#
# Services
#

# android.add_src =


#
# Assets
#

# Include fonts and sounds
android.add_src = .


#
# Private storage
#

android.private_storage = True
