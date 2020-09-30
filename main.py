# calisacak once active urlleri cek
# linkleri topla
# linkleri tek tek db den sorgula yayinlanmis mi ?
# yayinlanmamis olanlari yayinlanmasi icin hazirla
# icerde var ama yayinlanmamis varsa hazirla sonra yayinla
# update

import data
from request import get_request_xml

def main():
    db = data()
    req = request()
    active_domin_list = db.get_active_domain_list() # get_active_url_list; get active list from db - technella
    for domain in active_domin_list: #loop for 
        request_url = db.get_request_url()
        for url in request_url:
            links = get_request_xml(url)
            for link in links:
                if !isLinkPublished(link):
                    publish(link)
                else:
                    if publish_control(link):
                        publish(link)


    print('main')

if __name__ == "__main__":
    main()
