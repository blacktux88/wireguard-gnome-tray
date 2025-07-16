#!/usr/bin/env python3
import gi
import subprocess
import signal
import os

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3, GLib

APP_ID = "wg-tray"
REFRESH_INTERVAL = 15 * 1000  # 15 Sekunden
PREFIX = "WG-"

class WgTray:
    def __init__(self):
        self.indicator = AppIndicator3.Indicator.new(
            APP_ID,
            os.path.join(os.path.dirname(__file__), "icon-wg.png"),
            AppIndicator3.IndicatorCategory.APPLICATION_STATUS
        )
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.refresh_menu()
        GLib.timeout_add(REFRESH_INTERVAL, self.refresh_menu)

    def get_all_wg_connections(self):
        try:
            output = subprocess.check_output(["nmcli", "-t", "-f", "NAME", "con", "show"]).decode()
            lines = output.strip().split("\n")
            return [line for line in lines if line.startswith(PREFIX)]
        except subprocess.CalledProcessError:
            return []

    def get_active_connections(self):
        try:
            output = subprocess.check_output(["nmcli", "-t", "-f", "NAME", "con", "show", "--active"]).decode()
            return set(output.strip().split("\n")) if output.strip() else set()
        except subprocess.CalledProcessError:
            return set()

    def toggle_connection(self, widget, conn_name):
        if conn_name in self.get_active_connections():
            subprocess.call(["nmcli", "con", "down", conn_name])
        else:
            subprocess.call(["nmcli", "con", "up", conn_name])
        self.refresh_menu()

    def import_wireguard_conf(self, widget):
        dialog = Gtk.FileChooserDialog(
            title="WireGuard .conf-Datei importieren",
            action=Gtk.FileChooserAction.OPEN,
            buttons=(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK)
        )
        filter_conf = Gtk.FileFilter()
        filter_conf.set_name("WireGuard-Konfiguration (*.conf)")
        filter_conf.add_pattern("*.conf")
        dialog.add_filter(filter_conf)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            filepath = dialog.get_filename()
            self.import_and_deactivate(filepath)
        dialog.destroy()

    def import_and_deactivate(self, filepath):
        try:
            output = subprocess.check_output([
                "nmcli", "connection", "import", "type", "wireguard", "file", filepath
            ]).decode()

            if "Connection '" in output:
                conn_name = output.split("Connection '")[1].split("'")[0]
                subprocess.check_call([
                    "nmcli", "connection", "modify", conn_name, "connection.autoconnect", "no"
                ])
                subprocess.call(["nmcli", "connection", "down", conn_name])
                print(f"[+] Importiert & Autoconnect deaktiviert: {conn_name}")
                self.refresh_menu()
            else:
                print("[!] Kein Verbindungsname erkannt.")
        except subprocess.CalledProcessError as e:
            print(f"[!] Fehler beim Import: {e}")

    def refresh_menu(self, *args):
        menu = Gtk.Menu()
        all_wg = self.get_all_wg_connections()
        active = self.get_active_connections()

        if not all_wg:
            item = Gtk.MenuItem(label="(Keine WG-Verbindungen)")
            item.set_sensitive(False)
            menu.append(item)
        else:
            for conn in sorted(all_wg):
                status_icon = "✅" if conn in active else "❌"
                label = f"{conn}  {status_icon}"
                item = Gtk.MenuItem(label=label)
                item.connect("activate", self.toggle_connection, conn)
                menu.append(item)

        menu.append(Gtk.SeparatorMenuItem())

        import_item = Gtk.MenuItem(label="📥 WG .conf importieren…")
        import_item.connect("activate", self.import_wireguard_conf)
        menu.append(import_item)

        quit_item = Gtk.MenuItem(label="⏻ Beenden")
        quit_item.connect("activate", lambda _: Gtk.main_quit())
        menu.append(quit_item)

        menu.show_all()
        self.indicator.set_menu(menu)
        return True

def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    WgTray()
    Gtk.main()

if __name__ == "__main__":
    main()
