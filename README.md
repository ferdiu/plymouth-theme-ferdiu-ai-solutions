![ferdiu ai solutions plymouth theme](screenshot.png)

# plymouth-theme-ferdiu-ai-solutions

A minimal Plymouth two-step theme for **ferdiu ai solutions**.

This theme:

- Replaces the OEM firmware logo
- Uses a pure black background
- Centers the ferdiu ai solutions logo
- Applies the brand accent color `#b875dc`
- Is packaged as a clean, Fedora-ready RPM

Author: Federico Manzella

---

## 📦 Building the RPM

### 1. Install build dependencies

```bash
sudo dnf install rpm-build rpmdevtools
````

### 2. Prepare rpmbuild tree (if not already done)

```bash
rpmdev-setuptree
```

### 3. Build the RPM

From the repository root:

```bash
rpmbuild -ba plymouth-theme-ferdiu-ai-solutions.spec
```

The resulting RPM will be located in:

```
$(rpm --eval %_topdir)/RPMS/noarch/
```

---

## 🚀 Installing the Theme

```bash
sudo rpm -ivh $(rpm --eval %_topdir)/RPMS/noarch/plymouth-theme-ferdiu-ai-solutions-*.rpm
```

The installation automatically:

* Sets the theme as default
* Rebuilds the initramfs via `dracut`

---

## 🧪 Testing Without Rebooting

You can preview the theme immediately:

```bash
sudo plymouthd --no-daemon --debug
sudo plymouth --show-splash
```

To exit the splash:

```bash
sudo plymouth quit
```

---

## 🔄 Restoring the Default Theme

If needed:

```bash
sudo plymouth-set-default-theme bgrt
sudo dracut -f
```

---

## 📁 Repository Structure

```
plymouth-theme-ferdiu-ai-solutions/
├── ferdiu-ai-solutions-logo.png
├── ferdiu-ai-solutions.plymouth
├── plymouth-theme-ferdiu-ai-solutions.spec
└── README.md
```

---

## 🎨 Branding

* Background: `#000000`
* Accent: `#b875dc`
* Layout: Centered logo with spinner below

---

## 📜 License

License: MIT AND LicenseRef-Logo-Proprietary
