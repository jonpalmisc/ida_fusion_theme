# IDA Fusion Theme

This plugin simply forces IDA to use the "Fusion"
[QStyle](https://doc.qt.io/qt-5/gallery.html), regardless of the platform IDA
is running on.

This style is already the default on Linux. However, Qt supports this style on
all platforms---there is just no way to change it via IDA's preferences or
config files.

## Install

Just copy `fusion.py` into your IDA plugins folder. If you are on macOS, you
can use the `install.sh` script which does that automatically.
