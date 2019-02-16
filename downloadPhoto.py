#! python3
# downloadPhoto.py - Downloads photos from thispersondoesnotexist.com repeatedly.
# by headless ghost

import requests, os, bs4
                                                        # Instructions:
url = 'https://thispersondoesnotexist.com'              # <<< starting url
os.makedirs('aiphoto', exist_ok=True)   				# <<< store comics in ./aiphoto
for x in range(100):                                    # <<< place amount of pics you want here!!!!!!!!!
	
	# Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    imageName = 'download%d.jpg' % x

		# Save the image to ./aiphoto.
    imageFile = open(os.path.join('aiphoto', imageName), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
        #imageFile.close()

print('Done.')