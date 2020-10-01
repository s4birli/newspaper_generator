# calisacak once active urlleri cek
# linkleri topla
# linkleri tek tek db den sorgula yayinlanmis mi ?
# yayinlanmamis olanlari yayinlanmasi icin hazirla
# icerde var ama yayinlanmamis varsa hazirla sonra yayinla
# update

from data.db_connection import db
from img.remove import remove_images
from bson import ObjectId


if __name__ == "__main__":
    remove_images()
    url_active_list = db().get_active_urls()
    for url in url_active_list:
        request_active_list = db().get_active_requests(ObjectId(url['_id']))
        for req in request_active_list:
            run(url, req)


# f"{a} {b}"
# test.title()
# test.find('tst')
# primitive types int, string, boolen
