# BitChat Casino Bot - Testing Guide

## Quick Test Setup

### Step 1: Clone & Install
```bash
git clone https://github.com/KXNGJXNESAI/games.git
cd games
bash install.sh
```

### Step 2: Validate Setup
```bash
python3 test_bot.py
```

This will verify:
- ✅ Python 3.10+
- ✅ All dependencies installed
- ✅ Cashu CLI working
- ✅ All modules can be imported
- ✅ All syntax is correct

### Step 3: Get Test Cashu Tokens
Use the **testnut.cashu.space** mint (fake sats - perfect for testing)

**Option A: Via cashu.me (Easiest)**
1. Go to https://cashu.me
2. Select mint: `https://testnut.cashu.space`
3. Click "Request tokens" to get test ecash
4. Copy the token (looks like: `cashuBo2F0gaJhaUgA2...`)

**Option B: Via CLI**
```bash
# Check balance
CASHU_DIR=./house_wallet MINT_URL=https://testnut.cashu.space cashu balance

# Receive tokens
CASHU_DIR=./house_wallet MINT_URL=https://testnut.cashu.space cashu receive cashuBo2F0gaJhaUgA2...
```

### Step 4: Fund House Wallet (Optional)
```bash
CASHU_DIR=./house_wallet MINT_URL=https://testnut.cashu.space cashu receive <token>
```

Check balance:
```bash
CASHU_DIR=./house_wallet MINT_URL=https://testnut.cashu.space cashu balance
```

### Step 5: Start the Bot
```bash
python3 main.py
```

When prompted:
- **Geohash:** `test` (or any channel name)
- **Nickname:** `TestBot`
- **Mint URL:** `https://testnut.cashu.space`

### Step 6: Test Games

Once bot is running, join the chat and try:

**Roulette:**
```
!roulette red cashuBo2F0gaJhaUgA2...
!roulette 17 cashuBo2F0gaJhaUgA2...
!roulette high cashuBo2F0gaJhaUgA2...
```

**Hangman:**
```
!hangman cashuBo2F0gaJhaUgA2...
!hangman guess e
!hangman guess a
!hangman word hello
```

**Blackjack:**
```
!21 cashuBo2F0gaJhaUgA2...
!21 hit
!21 stand
!21 status
```

**Other Commands:**
```
!help              # Show all games
!balance           # Show house wallet balance
```

---

## Testing Checklist

- [ ] Run `python3 test_bot.py` - all tests pass
- [ ] Dependencies install without errors
- [ ] Python 3.10+ detected
- [ ] Cashu CLI working
- [ ] secrets.txt created
- [ ] Bot connects to Nostr relays
- [ ] Bot joins geohash channel
- [ ] Can place roulette bets
- [ ] Can play hangman
- [ ] Can play blackjack
- [ ] Winnings paid out correctly
- [ ] House wallet balance updates

---

## Troubleshooting

**"test_bot.py fails"**
```bash
python3 test_bot.py
# Check output for which test failed
# Install missing dependencies: pip install -r requirements.txt
```

**"Connection refused"**
- Check internet connection
- Try different Nostr relay
- Run: `python3 -c "import websockets; print('OK')"`

**"Cashu token invalid"**
- Make sure token is from testnut.cashu.space mint
- Token may have expired (get fresh from cashu.me)
- Check token format starts with `cashuBo` or `cashuA`

**"Bot not responding"**
- Check bot is still running in terminal
- Check geohash channel matches your command
- Look for errors in bot console output
- Run with debug: `DEBUG=1 python3 main.py`

**"Balance shows 0"**
- Fund wallet first: `CASHU_DIR=./house_wallet MINT_URL=https://testnut.cashu.space cashu receive <token>`
- Check CASHU_DIR and MINT_URL environment variables match
- Try: `CASHU_DIR=./house_wallet MINT_URL=https://testnut.cashu.space cashu balance`

**"Import errors"**
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade

# Or install individually
pip install websockets>=12.0
pip install cashu>=0.19.0
pip install marshmallow>=3.13,<4
```

---

## Full Test Workflow

```bash
# 1. Install
bash install.sh

# 2. Validate setup
python3 test_bot.py

# 3. Get test tokens from https://cashu.me (mint: testnut.cashu.space)

# 4. Fund house wallet
CASHU_DIR=./house_wallet MINT_URL=https://testnut.cashu.space cashu receive <TOKEN>

# 5. Start bot
python3 main.py

# 6. Test commands in Nostr chat
# !roulette red <TOKEN>
# !hangman <TOKEN>
# !21 <TOKEN>
```

---

## Next Steps After Testing

1. ✅ Test with testnut.cashu.space (fake money)
2. Switch to production mint (https://21mint.me) when confident
3. Deploy to server for 24/7 operation
4. Add real Cashu funding
5. Announce bot to Nostr community
6. Go live! 🚀

---

## Debug Logging

Run bot with debug output:
```bash
DEBUG=1 python3 main.py
```

This creates a timestamped log file with all events.

---

## Need More Help?

1. Check bot console for error messages
2. Run tests: `python3 test_bot.py`
3. Check debug logs in `logs/casino_bot_*.log`
4. Review [README.md](README.md) for more info
5. Check [INSTALL.md](INSTALL.md) for setup issues
