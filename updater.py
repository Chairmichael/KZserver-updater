# updater.py

from bs4 import BeautifulSoup
import requests
from bisect import bisect

BSPS_TAG = '<a href="bsps/">bsps/</a>'
WEBSITE = 'https://kzmaps.tangoworldwide.net/'
# site tree:
#	bsps/
#		*.bsp
#	mapcycles/
#		gokz.txt
#		kztimer.txt
LAST_UPDATED_DATE_FILE = 'date_updated.txt'
BSP_MANIFEST_FILE = 'bsp_manifest.txt'

def update_local_manifest():
	pass


def updateMaps():
	print('Updating maps')
	bsps_page = requests.get(WEBSITE + 'bsps/')
	new_manifest = []
	soup = BeautifulSoup(bsps_page.content, features='lxml')
	for l in str(soup).split('\n'):
		if '.bsp' in l:
			start = l.find('"') + 1
			end = l.find('"', start)
			mapname = l[start:end]
			item = l.split()
			item[0] = mapname
			item.pop(1)
			new_manifest.append(item)

	local_manifest = []
	with open(BSP_MANIFEST_FILE) as local_manifest_file:
		for l in local_manifest_file:
			local_manifest.append(l.split())

	maps_to_download = []
	for x in new_manifest:
		i = bisect(local_manifest, x) - 1
		if x == local_manifest[i]:


	# i = 0
	# for x in new_manifest:
	# 	i += 1
	# 	if (i < 20):
	# 		print(x)


def main():
	# Get main page
	kzmaps_page = requests.get(WEBSITE)
	soup = BeautifulSoup(kzmaps_page.content, features='lxml')
	# Get date modified of bsps dir
	lines = str(soup).split('\n')
	bsp_line = ''
	for l in lines:
		if 'bsps' in l:
			bsp_line = l
	# date_bsps_modified = bsp_line[len(BSPS_TAG):-2].strip()
	date_bsps_modified = ' '.join(bsp_line.split()[-3:-1])
	print(date_bsps_modified)

	# Compare the dates
	with open(LAST_UPDATED_DATE_FILE, 'r+') as datefile:
		if datefile.read().strip() != date_bsps_modified:
			datefile.write(date_bsps_modified)
			updateMaps()
		else:
			print('Up to date')



	# Get differences of the two files
	# Download the new maps

if __name__ == '__main__':
	main()
