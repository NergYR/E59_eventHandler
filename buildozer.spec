[app]

# Title of your application
title = E59 Event

# Package name
package.name = e59Event

# Domain
package.domain = e59.fr
version = 0.1

# Source code directory
source.dir = .

# Requirements
requirements = python3,kivy,plyer,pyzbar,Pillow

# Android specific
android.permissions = CAMERA, INTERNET
android.archs = arm64-v8a, armeabi-v7a
android.api = 31
android.minapi = 21
android.enable_androidx = True
