# WireGuard GNOME Tray

A lightweight, GNOME-compatible tray application to manage your WireGuard VPN connections using `nmcli`.  
Built with Python and GTK3, this tray tool is designed for sysadmins and advanced users who want quick control of WireGuard interfaces from the desktop panel.

---

## 🚀 Features

- 🟢 List all VPN connections starting with `WG-`
- 📥 Import `.conf` files via a GUI file dialog
- 🚫 Automatically disables `autoconnect` on import
- 📴 Ensures connections are disconnected after import
- 🖱️ Connect/disconnect any WireGuard VPN with a single click
- 🧼 Clean GTK AppIndicator integration with no terminal window
- 🔁 Auto-refresh every 15 seconds

---

## 🖼️ Screenshot

![Tray Menu](screenshot.png)

---

## 🛠️ Requirements

Install the following packages on your Linux system:

```bash
sudo apt install \
  network-manager \
  wireguard \
  python3-gi \
  gir1.2-gtk-3.0 \
  gir1.2-appindicator3-0.1
