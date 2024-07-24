import ida_idaapi

from PyQt5.QtWidgets import QApplication


class fusion_style_plugin_t(ida_idaapi.plugin_t):
    flags = ida_idaapi.PLUGIN_FIX
    wanted_name = "Fusion"

    def init(self):
        QApplication.setStyle("Fusion")
        return ida_idaapi.PLUGIN_SKIP

    def run(self):
        pass

    def term(self):
        pass


def PLUGIN_ENTRY():
    return fusion_style_plugin_t()
