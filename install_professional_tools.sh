#!/bin/bash
# install_professional_tools.sh

echo "🔒 Installing Professional Ethical Security Testing Tools"
echo "=========================================================="
echo "LEGAL USE ONLY - AUTHORIZED TESTING REQUIRED"
echo "=========================================================="

# Update system
sudo apt update && sudo apt upgrade -y

# Install core security tools
echo "Installing core security tools..."
sudo apt install -y \
    nmap \
    nikto \
    wireshark \
    apktool \
    john \
    hydra \
    sqlmap \
    git \
    python3-pip \
    build-essential

# Install Metasploit Framework
echo "Installing Metasploit Framework..."
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
chmod 755 msfinstall
./msfinstall

# Install Burp Suite (manual download required)
echo "Note: Burp Suite Professional requires manual download from:"
echo "https://portswigger.net/burp/releases"

# Install additional Python security libraries
echo "Installing Python security libraries..."
pip3 install requests beautifulsoup4 scapy pwntools

# Download wordlists for John and Hydra
echo "Downloading security wordlists..."
sudo apt install -y wordlists
git clone https://github.com/danielmiessler/SecLists.git /opt/SecLists

# Create tool directories
mkdir -p ~/security-tools/{reports,logs,wordlists}

echo "=========================================================="
echo "Installation Complete!"
echo "=========================================================="
echo "Installed Tools:"
echo "✓ Metasploit Framework"
echo "✓ John the Ripper" 
echo "✓ Hydra"
echo "✓ SQLmap"
echo "✓ Nmap"
echo "✓ Nikto"
echo "✓ Wireshark"
echo "✓ Apktool"
echo "=========================================================="
echo "IMPORTANT: Always obtain proper authorization before testing!"
echo "Use responsibly and ethically."
