"""Debug and logging utilities for casino bot."""

import os
import sys
import logging
from datetime import datetime

# Setup logging directory
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Create logger
logger = logging.getLogger("CasinoBot")
logger.setLevel(logging.DEBUG)

# File handler
log_file = os.path.join(LOG_DIR, f"casino_bot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
if os.environ.get('DEBUG', '').lower() in ['true', '1', 'yes']:
    console_handler.setLevel(logging.DEBUG)
else:
    console_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def log_startup(config):
    """Log startup configuration (no sensitive data)."""
    logger.info("="*60)
    logger.info("🎰 CASINO BOT STARTING UP")
    logger.info("="*60)
    logger.info(f"Geohash Channel: {config.get('geohash', 'unknown')}")
    logger.info(f"Bot Nickname: {config.get('nickname', 'unknown')}")
    logger.info(f"Mint URL: {config.get('mint_url', 'unknown')}")
    logger.info(f"Relays: {len(config.get('relays', []))} configured")
    logger.info("="*60)

def log_relay_connect(relay_url, status):
    """Log relay connection attempt."""
    logger.info(f"[RELAY] {relay_url} - {status}")

def log_relay_message(relay, event_type, content):
    """Log relay message received."""
    logger.debug(f"[RELAY MSG] {relay} - Type: {event_type} - Content: {content[:50]}...")

def log_game_start(player, game, amount):
    """Log when a game starts."""
    logger.info(f"[GAME START] Player: {player} | Game: {game} | Bet: {amount}")

def log_game_result(player, game, result, payout):
    """Log game result."""
    status = "WIN" if payout > 0 else "LOSS" if payout < 0 else "PUSH"
    logger.info(f"[GAME RESULT] {status} | Player: {player} | Game: {game} | Result: {result} | Payout: {payout}")

def log_wallet_action(action, amount, result):
    """Log wallet operations."""
    logger.info(f"[WALLET] {action} | Amount: {amount} | Result: {result}")

def log_error(error_type, message, player=None):
    """Log errors."""
    prefix = f"[{error_type}]"
    if player:
        prefix += f" Player: {player}"
    logger.error(f"{prefix} {message}")

def log_debug(message):
    """Log debug messages."""
    logger.debug(f"[DEBUG] {message}")

if __name__ == "__main__":
    logger.info("Debug logging module loaded successfully")
    logger.info(f"Debug mode: {os.environ.get('DEBUG', 'disabled')}")
    logger.info(f"Log file: {log_file}")
