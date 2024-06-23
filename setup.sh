#!/bin/bash

# Custom installation directory
INSTALL_DIR=$HOME/custom-libsqlite3

# Create the installation directory
mkdir -p $INSTALL_DIR

# Update package list and download the package
apt-get update
apt-get install -y libsqlite3-dev  # Install the necessary system dependency

# Clone the repository
git clone https://github.com/NaveenKumar075/DocGPT-RAG-With-Groq-LLM.git
cd DocGPT-RAG-With-Groq-LLM/pysqlite3

# Set environment variables for custom library path
export CPATH=$INSTALL_DIR/usr/include:$CPATH
export LIBRARY_PATH=$INSTALL_DIR/usr/lib/x86_64-linux-gnu:$LIBRARY_PATH
export LD_LIBRARY_PATH=$INSTALL_DIR/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH

# Build and install pysqlite3
python setup.py install --prefix=$INSTALL_DIR

# Optionally, add the environment variables to .bashrc for persistence
echo "export CPATH=$INSTALL_DIR/usr/include:\$CPATH" >> ~/.bashrc
echo "export LIBRARY_PATH=$INSTALL_DIR/usr/lib/x86_64-linux-gnu:\$LIBRARY_PATH" >> ~/.bashrc
echo "export LD_LIBRARY_PATH=$INSTALL_DIR/usr/lib/x86_64-linux-gnu:\$LD_LIBRARY_PATH" >> ~/.bashrc

# Install Python packages from requirements.txt
pip install -r requirements.txt