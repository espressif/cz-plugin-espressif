### ✨ New Features

- **test_esptool**: Added test for embedded and detected flash size match *(Jakub Kocka - c0ea74a)*
- **spi_connection**: Support --spi-connection on all chips *(radim.karnis - 1a38293)*

### 🐛 Bug Fixes

- **esp32c2**: Added get_flash_cap and get_flash_vendor *(Jakub Kocka - b8dd74d)*
- **testloadram**: Windows assertion error *(Jakub Kocka - cd51bbc)*
- **esp32c2**: Recommend using higher baud rate if connection fails *(Jakub Kocka - ef0c91f)*
- **test_esptool**: Fixed connection issue on Windows *(Jakub Kocka - 4622bb2)*
- **esptool**: Rephrase the --ram-only-header command message *(Marek Matej - da4a486)*
- **load_ram**: check for overlaps in bss section *(Peter Dragun - 3a82d7a)*
- **tests/intelhex**: make sure file is closed on Windows *(Peter Dragun - 900d385)*
- **spi_connection**: Unattach previously attached SPI flash *(radim.karnis - afaa7d2)*
- fixed exit() to be used from right module *(Jakub Kocka - d1610a9)*

### 📖 Documentation

- **advanced-topics**: Fixed strapping pin for Automatic Bootloader section *(Jakub Kocka - 590c2c6)*
- **serial-protocol**: add images and flowchart *(Peter Dragun - e99c114)*

<!-- by command:  `cz changelog v4.7.0 --template="RELEASE_NOTES.md.j2" --file-name="Release_notes_example.md"'` -->

<!-- pyproject.toml:   "release_notes_footer" not set  -->
