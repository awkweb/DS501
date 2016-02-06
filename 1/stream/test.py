from utils import load_json


broncos = load_json('json/broncos')
panthers = load_json('json/panthers')
counts = load_json('json/counts')

print len(broncos)
print len(panthers)

for c in counts:
    print c