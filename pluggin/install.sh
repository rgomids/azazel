#!/bin/bash

# Define constants
APP_NAME="azazel"
INSTALL_DIR="/opt/$APP_NAME"
VENV_DIR="$INSTALL_DIR/venv"
ENTRY_SCRIPT="$INSTALL_DIR/$APP_NAME.py"
PROFILE_FILE="$HOME/.bashrc"

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Install necessary packages
echo "Installing required packages..."
sudo apt install -y python3 python3-pip python3-venv espeak

# Clone or copy your library into /opt
echo "Setting up the application in $INSTALL_DIR..."
sudo mkdir -p "$INSTALL_DIR"
sudo cp -r ./* "$INSTALL_DIR"
sudo chown -R $USER:$USER "$INSTALL_DIR"

# Create a virtual environment
echo "Creating a virtual environment..."
python3 -m venv "$VENV_DIR"

# Activate the virtual environment and install dependencies
echo "Installing dependencies in the virtual environment..."
source "$VENV_DIR/bin/activate"
pip3 install -r "$INSTALL_DIR/requirements.txt"
deactivate

# Add alias to the shell profile
echo "Creating an alias to run the application..."
ALIAS_COMMAND="alias $APP_NAME='source $VENV_DIR/bin/activate && python3 $ENTRY_SCRIPT'"
if ! grep -q "$ALIAS_COMMAND" "$PROFILE_FILE"; then
    echo "$ALIAS_COMMAND" >> "$PROFILE_FILE"
    echo "Alias added to $PROFILE_FILE. Use '$APP_NAME' to run the application."
else
    echo "Alias already exists in $PROFILE_FILE."
fi

# Reload the shell profile
echo "Reloading shell profile..."
source "$PROFILE_FILE"
