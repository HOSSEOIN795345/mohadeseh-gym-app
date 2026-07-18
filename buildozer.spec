[app]

# (str) Title of your application
title = Mohadeseh Gym

# (str) Package name
package.name = mohadesehgym

# (str) Package domain
package.domain = org.mohadeseh

# (str) Source code directory
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,mp3,json,wav

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3,kivy==2.3.1

# (str) Supported orientation
orientation = portrait

# (str) Icon
icon.filename = %(source.dir)s/assets/icon.png


# (list) Supported architectures
android.archs = arm64-v8a


# (int) Android API
android.api = 34

# (int) Minimum Android API
android.minapi = 23

# (str) Android NDK version
android.ndk = 25b


# (bool) Fullscreen mode
fullscreen = 0


# (str) Presplash
# presplash.filename = %(source.dir)s/assets/presplash.png



[buildozer]

# Log level
log_level = 2


# (str) Warn when running as root
warn_on_root = 1



[app:android]

# Android permissions
android.permissions = VIBRATE,INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE


# Enable AndroidX
android.enable_androidx = True


# Use SDL2
p4a.bootstrap = sdl2


# Java source compatibility
android.gradle_dependencies =


# Copy libs
android.copy_libs = 1
