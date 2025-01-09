#!/bin/bash

# Start updating local system
sudo apt update

# Define constants
APP_NAME="azazel"
INSTALL_DIR="/opt/$APP_NAME"
VENV_DIR="$INSTALL_DIR/venv"
ENTRY_SCRIPT="$INSTALL_DIR/$APP_NAME.py"
PROFILE_FILE="$HOME/.zshrc"
TEMP="/"var/tmp""
OUTPUT_FILE="$TEMP/output.wav"
HISTORIC="$TEMP/historic.txt"
USE_VOICE="True"


# Export to local variables 
# export USE_VOICE

# Creating azazel dir and files
sudo touch $OUTPUT_FILE
sudo touch $HISTORIC


# Experimental   - Adding parameters for instalation
# for arg in "$@"; do
#     case $arg in
#         --use-voice|-v) USE_VOICE="True" ;;
#         # caso precise de mais um padrao, adicione abaixo. Ex abaixo
#         # --enable-debug|-u) ENABLE_DEBUG="true" ;;
#         *) echo "Unknow Parameter: $arg"; exit 1 ;;
#     esac
# done


# Install necessary packages
echo "Installing required system packages..."
sudo apt install -y python3 python3-pip python3-venv espeak portaudio19-dev python3-pyaudio


# Clone your library into /opt
echo "Setting up the application in $INSTALL_DIR..."
sudo mkdir -p "$INSTALL_DIR"
sudo cp -r ./* "$INSTALL_DIR"
sudo chown -R $USER:$USER "$INSTALL_DIR"

# Create a virtual environment install dependencies
echo "Creating a virtual environment..."
python3 -m venv "$VENV_DIR"
echo "Installing python dependencies on venv..."
source "$VENV_DIR/bin/activate"
pip3 install -r "$INSTALL_DIR/requirements.txt"
deactivate

# Add alias to the shell profile
echo "Creating an alias to run the application..."
ALIAS_COMMAND="alias $APP_NAME='source $VENV_DIR/bin/activate && nohup python3 $ENTRY_SCRIPT && deactivate &'"
if ! grep -q "$ALIAS_COMMAND" "$PROFILE_FILE"; then
    echo "$ALIAS_COMMAND" >> "$PROFILE_FILE"
    echo "Alias added to $PROFILE_FILE. Use '$APP_NAME' to run the application."
else
    echo "Alias already exists in $PROFILE_FILE."
fi

# Reload the shell profile
echo "Reloading shell profile..."
source "$PROFILE_FILE"
