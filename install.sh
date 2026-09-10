#!/bin/bash
set -e

echo "🎰 BitChat Casino Bot - Automated Setup"
echo "========================================"
echo ""

# Check Python version
echo "✓ Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.10+ first."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "  Found Python $PYTHON_VERSION"

# Check pip
echo "✓ Checking pip..."
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed."
    exit 1
fi

# Install Python dependencies
echo ""
echo "✓ Installing Python dependencies..."
pip3 install -r requirements.txt --quiet

# Verify Cashu CLI
echo "✓ Verifying Cashu CLI..."
if ! command -v cashu &> /dev/null; then
    echo "⚠️  Cashu CLI not found in PATH. Installing via pip..."
    pip3 install cashu --quiet
fi

CASHU_VERSION=$(cashu --version 2>/dev/null || echo "unknown")
echo "  Cashu version: $CASHU_VERSION"

# Create directories
echo ""
echo "✓ Creating required directories..."
mkdir -p house_wallet
mkdir -p games

# Run interactive setup
echo ""
echo "✓ Starting interactive configuration..."
python3 setup.py

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Fund the house wallet (optional):"
echo "     CASHU_DIR=./house_wallet MINT_URL=<your_mint> cashu receive <token>"
echo ""
echo "  2. Start the bot:"
echo "     python3 main.py"
echo ""
