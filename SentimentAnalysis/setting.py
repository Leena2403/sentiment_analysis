import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()

# from AppKit import NSApplicationDelegate
#
# class AppDelegate(NSApplicationDelegate):
#     def applicationSupportsSecureRestorableState(self):
#         return True

# Then you would instantiate your AppDelegate and set it as the application's delegate.
# For example:
# app_delegate = AppDelegate.alloc().init()
# NSApp().setDelegate_(app_delegate)
