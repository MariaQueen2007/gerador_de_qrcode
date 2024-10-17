https://deb.nodesource.com/setup_16.x — Node.js 16 "Gallium" (deprecated)
   * https://deb.nodesource.com/setup_18.x — Node.js 18 "Hydrogen" (Maintenance)
   * https://deb.nodesource.com/setup_19.x — Node.js 19 "Nineteen" (deprecated)
   * https://deb.nodesource.com/setup_20.x — Node.js 20 LTS "Iron" (recommended)
   * https://deb.nodesource.com/setup_21.x — Node.js 21 "Iron" (current)


curl -sL https://deb.nodesource.com/setup_20.x -o /tmp/nodesource_setup.sh
nano /tmp/nodesource_setup.sh
sudo bash /tmp/nodesource_setup.sh
sudo apt install nodejs
node -v