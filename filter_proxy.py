import sys, time 	
import requests, json
import system_handler as sysHand
from alternate_agent import getRamdomUserAgent
import urllib3




def verifyProxy(proxyList, outPath):

	statList = []

	dateStamp = sysHand.getDateStamp()

	statList.append('Start verifying proxy at ' + dateStamp)

	file = open(outPath, 'a', encoding = 'utf-8')

	for item in proxyList:
		user_agent = getRamdomUserAgent()		
		headers = {'User-Agent': user_agent}
		proxies = {}

		proxies['http'] = item
		proxies['https'] = item
		
		print('Verifying:', item)
		print('using agent:', headers['User-Agent'])
		print('using proxy:', proxies)
		try:
			urlTest = "http://icanhazip.com"
			resTest = requests.get(urlTest, proxies=proxies, headers=headers)
			print('using IP:', resTest.text)
			file.write(str(item) + '\n')			
			statList.append('Sucessfully verified IP ' + str(item))
			time.sleep(2)

		except urllib3.exceptions.ConnectTimeoutError:
			statList.append('Connection Time Out Error with IP ' + str(item))
			print('Connection Time Out Error with IP ' + str(item))
		except urllib3.exceptions.ConnectionError:
			print('Connection Error with IP ' + str(item))
			statList.append('Connection Error with IP ' + str(item))
		except  urllib3.exceptions.MaxRetryError:
			print('Max Retry Error with IP ' + str(item))
			statList.append('Max Retry Error with IP ' + str(item))

		except Exception as e:
			statList.append('Error verifying IP ' + str(item))
			print(e)

	file.close()

	dateStamp = sysHand.getDateStamp()

	statList.append('Finish verifying proxy at ' + dateStamp)

	return statList
		




if __name__ == '__main__':
	proxyDir = 'D:/Proxy/List'
	outPath = 'D:/Proxy/Filter/good_proxy_list.txt'
	logDir =  'D:/Proxy/Log'
	initialString = "Proxy_Verification_Log_"
	logPath = sysHand.getDatedFilePath(initialString, logDir)
	#clear file contents
	open(outPath, "w").close()
	proxyList = sysHand.loadProxyLines(proxyDir)
	statusList = verifyProxy(proxyList, outPath)
	sysHand.writeListToFile(statusList, logPath)

