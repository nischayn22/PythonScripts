import httplib
import sys
import re
import urllib2
import urlparse
import string
import urllib


action = 'cgi_bin/inet_pnrstat_cgi.cgi'
#linkregex = re.compile('<TABLE width="100%" border="0" cellpadding="0" cellspacing="1" class="table_border" id="center_table" >(.*?)<TR>
#<td colspan="4"><font color="#1219e8" size="1"><b> * Please Note that in case the Final Charts have not been prepared, the Current Status might #upgrade/downgrade at a later stage.</font></b></Td>
#</TR>
#</TABLE>')

	
while 1:

	print "welcome enter pnr number"
	pnr = "4240394339"
	conn = httplib.HTTPConnection("www.indianrail.gov.in")
	params = urllib.urlencode({'@'+'lccp_pnrno1': pnr, '@submit':"Get Status"})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn.request("post",'/'+action,params,headers)
	res = conn.getresponse()
	print res.status, res.reason
	#, res.read()
	data = res.read()
	f = open('pnrstatus.html', 'r+')
	f.write(data)
