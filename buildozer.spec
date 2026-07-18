[app]

title = MyApp
package.name = myapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0


[buildozer]
log_level = 2


[app:android]

android.api = 33
android.minapi = 21

# 👇 مهم
android.sdk = 33
android.ndk = 25b

# 👇 اینو ست می‌کنیم ولی بازم 37 نصب کردیم برای safety
android.build_tools = 33.0.2

android.accept_sdk_license = True
