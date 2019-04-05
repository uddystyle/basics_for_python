# ディクショナリ型を使いこなす
# update()メソッドによるディクショナリの連結
rssitem = {"title": "Pythonの勉強前",
           "link": "http://host.to/blog/entry",
           "dc:date": "2016-05-16T13:24:04Z"}
rssitem.update({"title": "Pythonを勉強中",
                "dc:creator": "someone"})
rssitem.keys()
print(rssitem)
