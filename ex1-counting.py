
urls= [
    "http://www.google.com/a.txt",      
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "http://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png" 
]

fn= {}

for x in urls:
    if x.split('/')[-1] in fn:
        fn[x.split('/')[-1]] += 1
    else:
        fn[x.split('/')[-1]] = 1

for a in sorted(fn)[0:3]:
    print(a, fn[a])