# Downloads brand logos from Wikipedia/Wikidata/Commons for the Palate intro reel.
import json, os, subprocess, urllib.request, urllib.parse
UA = {'User-Agent': 'PalateReelBot/1.0 (https://trypalate.github.io)'}
def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30).read()
PAGES = ['Chipotle_Mexican_Grill','Taco_Bell',"McDonald's",'In-N-Out_Burger','Chick-fil-A','Shake_Shack','Five_Guys','Popeyes',"Wendy's",'Burger_King','KFC','Starbucks','Subway_(restaurant)',"Domino's",'Panda_Express','Wingstop']
os.makedirs('reel-assets', exist_ok=True); report = {}
for page in PAGES:
    slug = ''.join(c for c in page.lower() if c.isalnum())
    try:
        s = json.loads(get('https://en.wikipedia.org/api/rest_v1/page/summary/' + urllib.parse.quote(page)))
        qid = s.get('wikibase_item'); files = {}
        if qid:
            ent = json.loads(get(f'https://www.wikidata.org/wiki/Special:EntityData/{qid}.json'))['entities'][qid]
            claims = ent.get('claims', {})
            for prop in ('P154',):
                for c in claims.get(prop, [])[:2]:
                    fn = c['mainsnak'].get('datavalue', {}).get('value')
                    if fn: files.setdefault('logo', fn)
        if 'logo' in files:
            fn = files['logo']; url = 'https://commons.wikimedia.org/wiki/Special:FilePath/' + urllib.parse.quote(fn.replace(' ', '_'))
            data = get(url); ext = fn.rsplit('.', 1)[-1].lower()
            raw = f'reel-assets/{slug}-logo.{ext}'; open(raw, 'wb').write(data)
            if ext == 'svg':
                subprocess.run(['rsvg-convert', '-w', '800', '-a', '-b', 'none', raw, '-o', f'reel-assets/{slug}-logo.png'], check=False)
            report[slug] = {'page': page, 'logo': fn}
        if s.get('originalimage'):
            src = s['originalimage']['source']; thumb = (s.get('thumbnail') or {}).get('source', src)
            data = get(thumb); ext = thumb.rsplit('.', 1)[-1].lower()[:4]
            open(f'reel-assets/{slug}-summary.{ext}', 'wb').write(data); report.setdefault(slug, {'page': page})['summary'] = src
    except Exception as e:
        report[slug] = {'page': page, 'error': str(e)}
json.dump(report, open('reel-assets/report.json', 'w'), indent=1)
print(json.dumps(report, indent=1))
