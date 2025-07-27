#!/bin/bash
echo "Installing Cykrna Suite..."
INSTALL_DIR="$HOME/cykrna_suite"

# Create folders
mkdir -p $INSTALL_DIR/modules
mkdir -p $INSTALL_DIR/data

# Install dependencies
echo "Updating packages..."
if command -v pkg >/dev/null 2>&1; then
    pkg update -y && pkg install -y python git
elif command -v apt >/dev/null 2>&1; then
    sudo apt update -y && sudo apt install -y python3 python3-pip git
fi

echo "Installing Python libraries..."
pip install --upgrade pip
pip install requests yt-dlp opencv-python pillow

# Create launcher command
echo "Creating launcher..."
echo "python3 $INSTALL_DIR/cykrna_suite.py" > $HOME/.cykrna_launcher
chmod +x $HOME/.cykrna_launcher
if ! grep -q "alias cykrna=" $HOME/.bashrc; then
    echo "alias cykrna='bash \$HOME/.cykrna_launcher'" >> $HOME/.bashrc
fi

echo "Installation complete. Restart your terminal or run: source ~/.bashrc"
echo "Now start the suite by typing: cykrna"
