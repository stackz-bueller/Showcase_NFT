# Showcase_NFT (PIR Controlled Gif)
Python Script that gathers NFT ERC 721 in ethereal address using OpenSeas API, and displays it using OpenCV

## Description of Program
This package calls OpenSeas API and captures response. Next, package formats the information received, and creates custom
artwork objects. After, the package, can randomly show art from wallet or showcases 5 random pieces of art, in various
formats, jpg, png, gif. The images are scaled accordingly since most NFT Art is produced at the highest quality. For gifs, the package temporarily stores the gif and then cleans up file so space isn't taken up by multiple files


## Start Up
### Packages Needed to Run Script
 - Pillow, OpenCV
 
### How to run
- Open the config.py file and replace text in owner_addr to your ether address, under quotes
- Open engine.py and run script

- Script will run gif off motion sensing

### Next Up
Will be adding a seperate branch to work with motion activated gifs using gpio on Raspberry Pi


