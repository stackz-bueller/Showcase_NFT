# Showcase_NFT
Python Script that gathers NFT ERC 721 in ether address using OpenSeas API, and displays it using OpenCV

## Description of Program
This package calls OpenSeas API and captures response. Next, package formats the information received, and creates custom
artwork objects. After, the package, can randomly show art from wallet or showcases 5 random pieces of art, in various
formats, jpg, png, gif. The images are scaled accordingly since most NFT Art is produced at the highest quality. For gifs, the package temporarily stores the gif and then cleans up file so space isn't taken up by multiple files


## Start Up
### Packages Needed to Run Script
 - Pillow, OpenCV, urlib, Requests
 
### How to run
- Open the config.py file and replace text in owner_addr to your ether address, under quotes
- Open engine.py and run script

- Script will randomly choose 5 NFT Tokens inside wallet and displays them
- Script handles both still images and gifs of any size

### Screen Navagation
- Press 0 to see next image
- Press ESC for GIFs

### To Do
- Focus on Making Images dynamic in shape for screen dimensions
- Adding Feature to show NFT Art based on Orientation,
- - i.e. Landscaped Art and Portrait Art, or solely square shaped Art
- 
- Update CV to run Full Screen
- Will be adding a seperate branch to work with motion activated gifs using gpio on Raspberry Pi


