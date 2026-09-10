# One-Click Installation Guide

## Quick Start (Recommended)

### On macOS/Linux:
```bash
bash install.sh
```

### On Windows (PowerShell):
```powershell
python setup.py
```

---

## Manual Setup (If Script Doesn't Work)

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Verify Cashu CLI
```bash
cashu --version
```
If not found, install with: `pip install cashu`

### 3. Run Configuration Wizard
```bash
python setup.py
```

### 4. (Optional) Fund the House Wallet
```bash
CASHU_DIR=./house_wallet MINT_URL=<your_mint_url> cashu receive <cashu_token>
```

### 5. Start the Bot
```bash
python main.py
```

---

## System Requirements

- **Python 3.10+** ([Download](https://www.python.org/downloads/))
- **pip** (usually included with Python)
- **Internet connection** (for Nostr relays and Cashu mint)

---

## What the Install Script Does

✅ Verifies Python 3.10+ is installed  
✅ Checks and installs pip  
✅ Installs all Python dependencies from `requirements.txt`  
✅ Verifies/installs Cashu CLI  
✅ Creates required directories (`house_wallet/`, `games/`)  
✅ Launches interactive configuration wizard  

---

## Troubleshooting

**"Python not found"**
- Install Python 3.10+ from https://www.python.org/downloads/

**"Cashu CLI not found"**
- Run: `pip install cashu`

**"Permission denied" (Linux/macOS)**
- Make script executable: `chmod +x install.sh`
- Then run: `bash install.sh`

**"secrets.txt not created"**
- Run `python setup.py` manually to generate it

For more help, see the main [README.md](README.md).
