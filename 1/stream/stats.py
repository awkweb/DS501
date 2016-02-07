from utils import load_json


broncos = load_json('json/broncos')
panthers = load_json('json/panthers')
patriots = load_json('json/patriots')
counts = load_json('json/counts')

print "Broncos", len(broncos)
print "Panthers", len(panthers)
print "Patriots", len(patriots)

for c in counts:
    print c
