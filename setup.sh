# Update package index
sudo apt-get update

# Install system dependencies
sudo apt-get install -y libsqlite3-dev

# Install wheel package
pip install wheel

# Install Python packages from requirements.txt
pip install -r requirements.txt