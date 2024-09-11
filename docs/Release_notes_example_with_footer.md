### ✨ New features

- **test_esptool**: Added test for embedded and detected flash size match _(Jakub Kocka - c0ea74a)_
- **spi_connection**: Support --spi-connection on all chips _(radim.karnis - 1a38293)_

### 🐛 Bug fixes

- **esp32c2**: Added get_flash_cap and get_flash_vendor _(Jakub Kocka - b8dd74d)_
- **testloadram**: Windows assertion error _(Jakub Kocka - cd51bbc)_
- **esp32c2**: Recommend using higher baud rate if connection fails _(Jakub Kocka - ef0c91f)_
- **test_esptool**: Fixed connection issue on Windows _(Jakub Kocka - 4622bb2)_
- **esptool**: Rephrase the --ram-only-header command message _(Marek Matej - da4a486)_
- **load_ram**: check for overlaps in bss section _(Peter Dragun - 3a82d7a)_
- **tests/intelhex**: make sure file is closed on Windows _(Peter Dragun - 900d385)_
- **spi_connection**: Unattach previously attached SPI flash _(radim.karnis - afaa7d2)_
- fixed exit() to be used from right module _(Jakub Kocka - d1610a9)_

### 📖 Documentation

- **advanced-topics**: Fixed strapping pin for Automatic Bootloader section _(Jakub Kocka - 590c2c6)_
- **serial-protocol**: add images and flowchart _(Peter Dragun - e99c114)_

Thanks to <FILL OUT CONTRIBUTORS>, and others for contributing to this release!

# Results of checking the release against common anti-virus SW

<Upload the release binaries to VirusTotal and ADD a link to the report here>

The failures are probably false positives. You can mark esptool as safe in your anti-virus SW,
or [install esptool from source](https://docs.espressif.com/projects/esptool/en/latest/installation.html).

<!-- by command:   cz changelog v4.7.0 --template="RELEASE_NOTES.md.j2" --file-name="Release_notes_example with_footer.md"  -->

<!-- pyproject.toml:
    [tool.commitizen]
        release_notes_footer = """
Thanks to <FILL OUT CONTRIBUTORS>, and others for contributing to this release!

# Results of checking the release against common anti-virus SW

<Upload the release binaries to VirusTotal and ADD a link to the report here>

The failures are probably false positives. You can mark esptool as safe in your anti-virus SW,
or [install esptool from source](https://docs.espressif.com/projects/esptool/en/latest/installation.html).
"""-->
