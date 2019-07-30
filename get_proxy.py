#AUTHOR: ANDY TRAN DAO ANH
#DATE: 30 JULY 2019
#PURPORSE: OBTAIN AND VERIFY PROXY ADDRESSES

import sys, time 
import urllib3
from system_handler import writeListToFile





def getProxyList(targetURL, pathOut):
	http = urllib3.PoolManager()
	try:
		response = http.request('GET', targetURL)
		print('Getting data from', targetURL, '...')
		if response.status == 200:
			data = response.data.decode('utf-8')
			proxList = str(data).split('\n')
			writeListToFile(proxList, pathOut)

	except Exception as e:
		print(e)





if __name__ == '__main__':

	proxyData = [{'target_url' : 'https://proxy.rudnkh.me/txt',
				'path_out' : 'D:/Proxy/List/raw_text_rudnkh.txt'},
				{'target_url' : 'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
				'path_out' : 'D:/Proxy/List/raw_text_clarketm.txt'}
				]

	for item in proxyData:
		#print(item['target_url'], item['path_out'])
		getProxyList(item['target_url'], item['path_out'])
		time.sleep(10)



	


	

