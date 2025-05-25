
# Nginx Proxy Manager Access List IP Updater

This script automatically updates the IP address in an Nginx Proxy Manager access list by using the Nginx Proxy Manager API. It checks your current public IP address and updates the access list only if the IP has changed.

## Features

- Authenticates to Nginx Proxy Manager to obtain a valid JWT token.
- Retrieves your current public IP address.
- Updates the specified access list with the new IP via the API.
- Skips update if the IP has not changed.
- Designed to be run periodically (e.g., via cron).

## Requirements

- Python 3
- `requests` Python package (install with `pip3 install requests`)

## Configuration

Edit the script to set the following variables:

```python
NPM_HOST = "https://npm.ezample.com"
USERNAME = "acladmin@example.com"
PASSWORD = "tupasswordsupersegura"
ACCESS_LIST_ID = 1
ACCESS_LIST_NAME = "MI_ZONA"
LAST_IP_FILE = "/tmp/last_public_ip.txt"
```

## Usage

1. Ensure the `requests` library is installed:

   ```bash
   pip3 install requests
   ```

2. Make the script executable:

   ```bash
   chmod +x /path/to/update_npm_access_list.py
   ```

3. Run manually to test:

   ```bash
   ./update_npm_access_list.py
   ```

4. Set up a cron job to run every 20 minutes:

   ```cron
   */20 * * * * /usr/bin/python3 /path/to/update_npm_access_list.py > /dev/null 2>&1
   ```

## Notes

- The script stores the last known IP address in a local file to avoid unnecessary updates.
- The script uses the official Nginx Proxy Manager API and performs authentication every time it runs to get a fresh token.
- Make sure your user has permission to update the specified access list.

## License

This program is free software: you can redistribute it and/or modify  
it under the terms of the GNU General Public License as published by  
the Free Software Foundation, either version 3 of the License, or  
(at your option) any later version.

This program is distributed in the hope that it will be useful,  
but WITHOUT ANY WARRANTY; without even the implied warranty of  
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the  
[GNU General Public License](https://www.gnu.org/licenses/) for more details.

You should have received a copy of the GNU General Public License  
along with this program.  If not, see <https://www.gnu.org/licenses/>.
