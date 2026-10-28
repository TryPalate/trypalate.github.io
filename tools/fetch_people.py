# Lead photos for the hot-take section of the reel, from Wikipedia (downscaled to 900px).
import json, os, io, urllib.request, urllib.parse
from PIL import Image
UA = {'User-Agent': 'PalateReelBot/1.0 (https://trypalate.github.io)'}
get = lambda u: urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=40).read()
PAGES = {'ronaldo':'Cristiano_Ronaldo','messi':'Lionel_Messi','brunomars':'Bruno_Mars','michaeljackson':'Michael_Jackson'}
os.makedirs('reel-assets/people', exist_ok=True); rep = {}
for k, page in PAGES.items():
    try:
        s = json.loads(get('https://en.wikipedia.org/api/rest_v1/page/summary/' + urllib.parse.quote(page)))
        src = (s.get('originalimage') or {}).get('source') or (s.get('thumbnail') or {}).get('source')
        im = Image.open(io.BytesIO(get(src))).convert('RGB'); im.thumbnail((900, 1200))
        im.save(f'reel-assets/people/{k}.jpg', quality=90); rep[k] = {'page': page, 'src': src, 'size': im.size}
    except Exception as e:
        rep[k] = {'page': page, 'error': str(e)}
json.dump(rep, open('reel-assets/people/report.json', 'w'), indent=1); print(json.dumps(rep, indent=1))
