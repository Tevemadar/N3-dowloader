import sys,urllib.request,re,os
if len(sys.argv)!=2:
  print("Specify an N3 block identifier")
  sys.exit()
dataset=sys.argv[1]
with urllib.request.urlopen("http://cmbn-navigator.uio.no/navigator/feeder/all_pyramids/?id="+dataset) as http:
  page=http.read().decode("utf-8")
trs=page.split("</tr>")
if len(trs)==1:
  print("Some error happened,see N3 message below:")
  print()
  print(re.match(".*<body>(.*)</body>",page.replace("\r","").replace("\n",""),re.MULTILINE).groups()[0])
  sys.exit()
folder="downloads/"+dataset
os.makedirs(folder,exist_ok=True)
os.chdir(folder)
for row in (re.sub("\\s+","",tr) for tr in trs[1:-1]):
  pair=re.match("<tr><td>([^<]+)</td><td>([^<]+)",row).groups()
  print(pair)
  with open(pair[1]+".zip","wb") as f:
    with urllib.request.urlopen("http://cmbn-navigator.uio.no/navigator/feeder/pyramid/?id="+pair[0]) as http:
      while True:
        chunk=http.read(64*1024*1024)
        if not chunk:
          break
        f.write(chunk)

