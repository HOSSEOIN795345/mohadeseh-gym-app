[app]

# نام برنامه
title = Mohadeseh Gym

# نام پکیج (بدون فاصله)
package.name = mohadesehgym

# دامنه
package.domain = org.mohadeseh

# مسیر کد اصلی
source.dir = .

# فایل‌هایی که باید داخل APK بروند
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,mp3,wav,json

# نسخه
version = 1.0


# وابستگی‌ها
requirements = python3,kivy==2.3.1


# حالت گوشی
orientation = portrait


# اندروید
android.api = 35
android.minapi = 23

# NDK سازگار
android.ndk = 25b

# قبول لایسنس
android.accept_sdk_license = True


# معماری گوشی‌ها
android.archs = arm64-v8a,armeabi-v7a


# بک‌گراند
fullscreen = 0


# آیکن (اگر داری)
# icon.filename = %(source.dir)s/assets/icon.png


# مجوزها (در صورت نیاز)
# android.permissions = INTERNET
