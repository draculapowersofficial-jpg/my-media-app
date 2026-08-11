[app]
title = Universal Media Downloader
package.name = unimediadownloader
package.domain = org.mymediaapp
source.dir = .
source.include_exts = py,png,jpg
version = 1.0.0

# Injects your required libraries straight into the APK package environment
requirements = python3,flet,yt-dlp,certifi

orientation = portrait
fullscreen = 1

# Essential internet setup parameters
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

android.archs = arm64-v8a
android.accept_sdk_license = True
