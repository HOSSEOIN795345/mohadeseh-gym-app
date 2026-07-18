[app]

# نام برنامه
title = Mohadeseh Gym


# نام پکیج (بدون فاصله)
package.name = mohadesehgym


# دامنه پکیج
package.domain = org.mohadeseh


# محل main.py
source.dir = .


# فایل‌هایی که داخل APK قرار می‌گیرند
source.include_exts = py,kv,png,jpg,jpeg,ttf,mp3,json,atlas,wav


# نسخه برنامه
version = 1.0


# کتابخانه‌ها
requirements = python3,kivy==2.3.1


# حالت صفحه
orientation = portrait


# تمام صفحه نباشد
fullscreen = 0



# -----------------------
# Android
# -----------------------

android.api = 34

android.minapi = 23

android.ndk = 25b

android.archs = arm64-v8a


# نسخه دقیق build tools
android.build_tools_version = 34.0.0


# نام Activity
android.entrypoint = org.kivy.android.PythonActivity


# اجازه اینترنت
android.permissions = INTERNET



# -----------------------
# Python For Android
# -----------------------

p4a.branch = master



# -----------------------
# فایل‌های اضافی
# -----------------------

android.add_src = .


# -----------------------
# تنظیمات Buildozer
# -----------------------

log_level = 2

warn_on_root = 1
