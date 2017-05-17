import requests
from ccf_list import ccf_list

#cats=['data mining', 'artificial intelligence','data science','information retrieval','knowledge management','recommender systems','e-commerce','web']
cats=['NLP', 'artificial intelligence','computational linguistics','natural language processing','data science','information retrieval','semantics','linguistics']
stop_pt='Expired CFPs'
url='http://www.wikicfp.com/cfp/call'
time_pt_l='<td align="left">'
time_pt_r='</td>'

results={}

print('NAME   | CCF-RANK |  DUE  |  CATEGORY\n------------------------------------------------')
for cat in cats:
    stop = False
    for page_i in range(1, 101):
        response=requests.get(url, {'conference': cat, 'page': page_i})
        body = response.text
        page_pt = '| Page '
        page = body[body.rfind(page_pt) + len(page_pt):]
        page = int(page[:page.find(' ')])

        if stop_pt in body: stop=True
        while 1:
            name_pt='<td rowspan="2" align="left">'
            next_name_i=body.find(name_pt)
            if next_name_i<0:break
            body=body[next_name_i+len(name_pt):]

            if stop and (stop_pt not in body): break
            this_url=body[:body.find('>')]
            body=body[body.find('>')+1:]
            name=body[:body.find('<')]
            short=name.upper().split()[0]
            if short in ccf_list.keys():
                body=body[body.find(time_pt_l)+len(time_pt_l):]
                when=body[:body.find(time_pt_r)]
                body=body[body.find(time_pt_l)+len(time_pt_l):]
                body=body[body.find(time_pt_l)+len(time_pt_l):]
                due=body[:body.find(time_pt_r)]
                print(name,'|', ccf_list[short],'|', due,'|', cat)
        if stop: break
"""
Output Sample:

NAME   | CCF-RANK |  DUE  |  CATEGORY
------------------------------------------------
SIGIR eCom 2017 | DM-A | Jun 15, 2017 | NLP
NIPS 2017 | AI-A | May 19, 2017 | artificial intelligence
ICONIP 2017 | AI-C | Jun 10, 2017 | artificial intelligence
IJCAI - CAI4HCD 2017 | AI-A | Jun 15, 2017 | artificial intelligence
CIKM 2017 | DM-B | May 23, 2017 (May 16, 2017) | information retrieval
SIGIR eCom 2017 | DM-A | Jun 15, 2017 | information retrieval
"""