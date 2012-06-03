import httplib
import sys
import re
import urllib2
import urlparse
import string
import urllib

#http://www.irctc-pnrstatus.com/PnrIframe.aspx?pnrNo1=4240394339&pnrNo2=
#http://50.31.134.135:8080/web1/PnrServlet?pnrno=4240394339
#http://www.irctc-pnrstatus.com/IndianRail.aspx?pnrNo1=4240394339
#action = 'trains/pnr_check'
#linkregex = re.compile('<TABLE width="100%" border="0" cellpadding="0" cellspacing="1" class="table_border" id="center_table" >(.*?)<TR>
#<td colspan="4"><font color="#1219e8" size="1"><b> * Please Note that in case the Final Charts have not been prepared, the Current Status might #upgrade/downgrade at a later stage.</font></b></Td>
#</TR>
#</TABLE>')

	
while 1:

	#print "welcome enter pnr number"
	#pnr = raw_input()
	pnr1="424"
	pnr2="0394339"
	conn = httplib.HTTPConnection("50.31.134.135")
	conn.request("GET",'/web1/PnrServlet?pnrno=4240394339')
	res = conn.getresponse()
	print res.status, res.reason
	#, res.read()
	data = res.read()
	f = open('pnrstatus.html', 'r+')
	f.write(data)
