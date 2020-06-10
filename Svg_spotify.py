from PIL import Image, ImageOps
import requests
import sys
import os

URI = sys.argv[1]

def main(URI):



    r = requests.get("https://scannables.scdn.co/uri/plain/png/000000/white/640/" + URI, stream=True)
    ext = r.headers['content-type'].split('/')[-1] 
    with open("SpotifyCodeDownload.png", 'wb') as f:
        for chunk in r.iter_content(1024): 
            f.write(chunk)

    im = Image.open('SpotifyCodeDownload.png')
    im_invert = ImageOps.invert(im)
    im_invert.save('SpotifyCodeDownloadi.png')

    Image.open("SpotifyCodeDownloadi.png").save("SpotifyCodeDownloadb.bmp")

    os.system('potrace --svg SpotifyCodeDownloadb.bmp -o SpotifyCodeDownloads.svg ')
        
    os.system('blender -b --python BlenderStl.py')

    #os.rename('out.stl', 

if (len(sys.argv)>1):
    main(URI)
    
else:
    print("Usage: python Spotifcode.py <URI>")
    main(URI)

