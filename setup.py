"""Interactive setup wizard for BitChat Casino Bot."""

import os
import sys
import json
from config import Config

def get_user_input(prompt: str, default: str = None) -> str:
    """Get user input with optional default value."""
    if default:
        display_prompt = f"{prompt} [{default}]: "
    else:
        display_prompt = f"{prompt}: "
    
    user_input = input(display_prompt).strip()
    return user_input if user_input else default

def setup_wizard():
    """Run interactive setup wizard."""
    print("\n" + "="*50)
    print("BitChat Casino Bot - Setup Wizard")
    print("="*50 + "\n")
    
    # Step 1: Geohash channel
    print("Step 1: Geohash Channel")
    print("-" * 30)
    print("Enter the BitChat geohash channel (e.g., 'gc', 'sf', 'nyc')")
    print("This determines which location channel the bot joins.")
    geohash = get_user_input("Geohash channel", "gc")
    
    # Step 2: Bot nickname
    print("\nStep 2: Bot Nickname")
    print("-" * 30)
    print("Enter a display name for the bot in chat.")
    nickname = get_user_input("Bot nickname", Config.DEFAULT_NICKNAME)
    
    # Step 3: Cashu mint URL
    print("\nStep 3: Cashu Mint URL")
    print("-" * 30)
    print("Enter the Cashu mint URL for ecash transactions.")
    print("Popular options:")
    print("  - https://testnut.cashu.space (test mint, fake sats)")
    print("  - https://21mint.me (production)")
    print("  - https://mint.minibits.cash (production)")
    mint_url = get_user_input("Cashu mint URL", Config.DEFAULT_MINT_URL)
    
    # Step 4: Nostr relays (optional)
    print("\nStep 4: Nostr Relays (Optional)")
    print("-" * 30)
    print("Use default relays? (recommended)")
    use_defaults = get_user_input("Use default relays?", "yes").lower() in ['yes', 'y']
    
    relays = Config.DEFAULT_RELAYS
    if not use_defaults:
        print("Enter relay URLs separated by commas:")
        relay_input = input("Relays: ").strip()
        if relay_input:
            relays = [r.strip() for r in relay_input.split(",")]
    
    # Save configuration
    print("\n" + "="*50)
    print("Saving configuration...")
    print("="*50)
    
    config_data = {
        "geohash": geohash,
        "nickname": nickname,
        "mint_url": mint_url,
        "relays": relays
    }
    
    # Save to secrets file
    Config.save_secrets("", config_data)
    
    print("\n✅ Configuration saved to secrets.txt")
    print("\nConfiguration:")
    print(f"  Geohash:    {geohash}")
    print(f"  Nickname:   {nickname}")
    print(f"  Mint URL:   {mint_url}")
    print(f"  Relays:     {len(relays)} relays configured")
    
    print("\n" + "="*50)
    print("Setup wizard complete!")
    print("="*50)
    print("\nNext steps:")
    print("  1. Optionally fund the house wallet:")
    print("     CASHU_DIR=./house_wallet MINT_URL={} cashu receive <token>".format(mint_url))
    print("\n  2. Start the bot:")
    print("     python3 main.py")

if __name__ == "__main__":
    try:
        setup_wizard()
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Setup error: {e}")
        sys.exit(1)
