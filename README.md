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
- 🔁 Auto-refresh every 15 seconds

---

## 🖼️ Screenshot

<img width="568" height="480" alt="Screenshot from 2025-07-16 23-46-01" src="https://github.com/user-attachments/assets/899a0dab-db20-4d56-a954-8e7ae5fc9f5e" />

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
---

## ☕ Buy me a Coffee (via Crypto)

 ⏱️ Great Scott! A Tip for the Flux Capacitor?

If this tool saved you 1.21 gigawatts of brainpower, feel free to flux me some crypto love:

- **Solana (SOL):** `bc1q2u0n2rdpwz67hgs7felvk380xzumjju4vy7yf6`
- **Bitcoin (BTC):** `GcS2ZvH4JpZD8hBruEQhQWZCaUVKrerQy8xHwtuXcRoa`
