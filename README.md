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

This tool requires the following packages to be installed on your Linux system:

```bash
sudo apt install \
  network-manager \
  wireguard \
  python3 \
  python3-gi \
  gir1.2-gtk-3.0 \
  gir1.2-appindicator3-0.1
```

---

## 🧩 How to Install & Run

### 1. Check if Python 3 is installed

```bash
python3 --version
```

If it's not installed:

```bash
sudo apt install python3
```

---

### 2. Clone this repository

```bash
git clone https://github.com/YOURNAME/wireguard-gnome-tray.git
cd wireguard-gnome-tray
```

---

### 3. Make the script executable

```bash
chmod +x wg_tray.py
```

---

### 4. Run the tray app

```bash
./wg_tray.py
```

Or, alternatively:

```bash
python3 wg_tray.py
```

---

## ⚠️ Disclaimer

This tool modifies system network connections using `nmcli`.

It is intended for sysadmins and technically-minded users who:

- know what WireGuard `.conf` files are
- understand how NetworkManager functions
- are aware of what gets written into `/etc/NetworkManager/`

If you import shady VPN configs or run this on a production system without thinking — that's on you.

**Use at your own risk. No warranty. No support. Just clean GNOME tray magic.**

---

## ☕ Buy me a Coffee (via Crypto)

### ⏱️ Great Scott! A Tip for the Flux Capacitor?

If this tool saved you 1.21 gigawatts of brainpower, feel free to flux me some crypto love:

- **Bitcoin (BTC):** `bc1q2u0n2rdpwz67hgs7felvk380xzumjju4vy7yf6`
- **Solana (SOL):** `GcS2ZvH4JpZD8hBruEQhQWZCaUVKrerQy8xHwtuXcRoa`

> Roads? Where we’re going, we don’t need VPN GUIs.
