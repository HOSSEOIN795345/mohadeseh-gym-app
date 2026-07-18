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

# 👇 خیلی مهم
android.api = 33
android.minapi = 21

# 👇 هماهنگ با build.yml
android.sdk = 33
android.ndk = 25b
android.build_tools = 33.0.2

# جلوگیری از دانلودهای خراب
android.accept_sdk_license = True
