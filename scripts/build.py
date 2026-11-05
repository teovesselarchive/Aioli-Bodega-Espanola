"""Build a portable static restaurant demo using Python's standard library."""
from pathlib import Path
from html import escape as esc
import json, shutil
ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/'dist'
MENU=json.loads((ROOT/'data/menu.json').read_text())
BOOK='https://www.opentable.com/restref/client/?rid=58273'
MAP='https://www.google.com/maps/search/?api=1&query=Aioli+Bodega+Espanola+1800+L+Street+Sacramento'
photos={
'paella':('aioli-cuisine-08a','Aioli’s seafood paella with mussels, shrimp and lemon',1024,734),
'lamb':('aioli-cuisine-05a','Grilled lamb chops and vegetables at Aioli',2500,1609),
'vegetables':('aioli-cuisine-06a','A plate of grilled seasonal vegetables',2361,1500),
'salad':('aioli-cuisine-07a','Fresh salad with citrus, olives and greens',1024,654),
'dessert':('aioli-cuisine-04a','Almond cake with cream and orange',1024,712),
'squid':('aioli-cuisine-02a','Aioli’s stuffed squid with sauce and herbs',1024,640),
'wine':('aioli-atmo-06a','Wine bottles in the bodega’s wooden wine shelves',848,566),
'ceramic':('aioli-atmo-03a','Painted Spanish ceramic pitcher and wine bottles at Aioli',721,1080),
'chandelier':('aioli-atmo-02a','Decorative metal chandelier inside Aioli',721,1080),
'sculpture':('aioli-atmo-07a','Sculpture displayed inside the bodega',721,1080)}
def photo(key,cls='',eager=False,sizes='(max-width: 700px) 100vw, 55vw'):
 name,alt,w,h=photos[key]
 widths=[480,960]+([1600] if w>960 else [])
 return f'<img class="{cls}" src="{{BASE}}assets/images/{name}-960.webp" srcset="'+', '.join(f'{{BASE}}assets/images/{name}-{x}.webp {min(x,w)}w' for x in widths)+f'" sizes="{sizes}" width="{w}" height="{h}" alt="{alt}" loading="{"eager" if eager else "lazy"}" decoding="async"'+(' fetchpriority="high"' if eager else '')+'>'
def button(label,url,kind=''):
 return f'<a class="button {kind}" href="{url}">{label}</a>'
def head(title,base,desc):
 return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} | Aioli Bodega Española</title><meta name="description" content="{desc}"><meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="#651b2c"><link rel="icon" href="{base}assets/images/aioli-logo.webp"><link rel="stylesheet" href="{base}assets/fonts/fonts.css?v=2"><link rel="stylesheet" href="{base}styles.css?v=2.1"><script defer src="{base}app.js?v=2.1"></script><noscript><style>.menu-controls,.print-menu{{display:none}}@media(max-width:767px){{.site-header{{height:auto;flex-wrap:wrap}}.nav-toggle{{display:none}}.mobile-nav[hidden]{{display:flex!important;position:static;padding:20px 0}}}}</style></noscript></head><body><a class="skip" href="#main">Skip to content</a>'''
def header(active=''):
 links=[('The menu','menu/'),('The bodega','bodega/'),('Find us','visit/')]
 return '<header class="site-header"><a class="brand" href="{BASE}" aria-label="Aioli Bodega Española home"><img src="{BASE}assets/images/aioli-logo.webp" width="68" height="68" alt="Aioli"><span>Bodega<br>Española</span></a><nav class="desktop-nav" aria-label="Main navigation">'+''.join(f'<a href="{{BASE}}{url}"'+(' aria-current="page"' if url==active else '')+f'>{text}</a>' for text,url in links)+'</nav><a class="button header-book" href="{BASE}visit/#reservations">Book a table</a><button class="nav-toggle" aria-expanded="false" aria-controls="mobile-nav">Menu</button><nav id="mobile-nav" class="mobile-nav" aria-label="Mobile navigation" hidden>'+''.join(f'<a href="{{BASE}}{url}">{text}</a>' for text,url in links)+'<a href="{BASE}visit/#reservations">Book a table</a></nav></header>'
def footer():
 return '''<footer class="footer"><div class="footer-kicker"><span>One more plate. One more story.</span><a href="{BASE}visit/#reservations">There’s a table for that.</a></div><p class="footer-signoff" lang="es">Nos vemos.</p><div class="footer-bottom"><span>Aioli Bodega Española<br>1800 L Street · Sacramento</span><div><a href="https://www.instagram.com/aioli_bodega/" target="_blank" rel="noopener">Instagram</a><a href="https://www.facebook.com/aiolibodegaespanola/" target="_blank" rel="noopener">Facebook</a></div><a href="tel:+19164479440">916.447.9440</a><span>Website concept<br>©2025 Reda Belalrbi &amp; Associates, Inc.</span></div></footer><a class="mobile-book" href="{BASE}visit/#reservations">Book a table</a>'''
def visitblock():
 return f'''<section class="visit-block" id="contact-aioli"><div class="visit-title"><span class="eyebrow">Your corner of Sacramento</span><h2 id="aioli-contact">L Street.<br>Spanish soul.</h2><p>1800 L Street<br>Midtown Sacramento, CA 95811</p>{button('Find your way',MAP,'outline')}</div><div class="visit-details"><h3>Come on over.</h3><dl><div><dt>Monday–Saturday</dt><dd>11 am–10 pm</dd></div><div><dt>Sunday</dt><dd>3 pm–9 pm</dd></div></dl><a class="phone" href="tel:+19164479440">916.447.9440</a><p>For a table, a question, or a special occasion,<br>give us a call.</p></div></section>'''
def sheets():
 sections=[('Chef Pablo’s seasonal selections',['aioli-chefs-choice-fall-2026-menu']),('Lunch',['aioli-lunch-fall-2026-menu-p1','aioli-lunch-fall-2026-menu-p2']),('Dessert & after-dinner drinks',['aioli-dessert-fall-2026-menu-p1','aioli-dessert-fall-2026-menu-p2']),('Wine, beer & cocktails',['aioli-wine-fall-2026-menu-p1','aioli-wine-fall-2026-menu-p2'])]
 return '<section class="printed-menus" id="original-menus"><div><span class="eyebrow">From the restaurant</span><h2>Prefer the printed copy?</h2><p>All seven original Fall 2026 menu sheets.</p></div><div>'+''.join('<details><summary>'+title+'</summary><div class="sheet-grid">'+''.join(f'<a href="{{BASE}}assets/originals/{name}.png" target="_blank" rel="noopener">Open sheet {i+1}<span>Full-size image</span></a>' for i,name in enumerate(files))+'</div></details>' for title,files in sections)+'</div></section>'
HOME='''<main id="main"><section class="poster-hero" id="content"><div class="poster-meta"><span>Spanish kitchen & wine bar</span><span>Midtown, Sacramento</span><span lang="es">Buen provecho.</span></div><h1 class="masthead" aria-label="Aioli"><span aria-hidden="true">A</span><span aria-hidden="true">I</span><span class="masthead-o" aria-hidden="true">O<img src="{BASE}assets/images/aioli-atmo-03a-480.webp" alt="" width="480" height="719"></span><span aria-hidden="true">L</span><span aria-hidden="true">I</span></h1><div class="hero-scene"><figure>'''+photo('paella',eager=True,sizes='(max-width: 767px) 100vw, 65vw')+'''<figcaption>Paella, for the middle of the table.</figcaption></figure><div class="hero-note"><p class="eyebrow">Bodega Española</p><h2>Tapas. <br>Vino.<br><em>Sobremesa.</em></h2><p>Spanish plates. A bottle to share.<br>A very good reason to stay a little longer.</p>'''+button('Explore the menu','{BASE}menu/')+'''<span class="hero-address">1800 L Street · Sacramento</span></div></div></section><div class="ceramic-rule" aria-hidden="true"></div>
<section class="manifesto"><p class="eyebrow">Life happens around a table.</p><h2>A little loud.<br>A little late.<br><span>A lot to love.</span></h2><div class="manifesto-note"><span lang="es">so·bre·me·sa</span><p>The conversation that keeps going<br>long after the plates are cleared.</p><p>Start with a few tapas. Pass around the paella. Let the next glass turn into the next story. That’s our kind of evening.</p><a class="text-link" href="{BASE}bodega/">Get to know the bodega</a></div></section>
<section class="kitchen-feature"><figure>'''+photo('lamb',sizes='100vw')+'''</figure><div class="kitchen-caption"><span class="eyebrow">From Chef Pablo’s kitchen</span><h2>Big plates.<br>Bigger appetites.</h2><a class="button" href="{BASE}menu/#seasonal">What’s cooking</a></div></section>
<section class="menu-invitation" id="aioli-menu"><div class="menu-invitation-heading"><span class="eyebrow">A little of this. A little of that.</span><h2 lang="es">La carta.</h2><p>From the first tapa<br>to the last drop.</p>'''+photo('squid',sizes='(max-width:767px) 45vw, 22vw')+'''</div><div class="menu-links">'''+''.join(f'<a href="{{BASE}}menu/#{cat}"><span class="menu-number">0{i+1}</span><span>{name}</span><small>{sub}</small></a>' for i,(cat,name,sub) in enumerate([('seasonal','De temporada','Chef Pablo’s selections'),('lunch','El almuerzo','Lunch & tapas'),('dessert','Algo dulce','Dessert & after dinner'),('drinks','Una copa','Cocktails & beer'),('wine','La bodega','The wine list'),('spirits','La última','Spirits & nightcaps')]))+'''</div></section>
<section class="bodega-story"><figure class="bodega-tall">'''+photo('ceramic')+'''<figcaption>Found in the bodega.</figcaption></figure><div class="bodega-story-copy"><span class="eyebrow">Full of flavor. Full of character.</span><h2 lang="es">Mucho<br>gusto.</h2><p>The painted ceramics. The well-stocked wine shelves. The little details worth looking up for.</p><p>There’s plenty to take in between courses.</p><a class="button outline" href="{BASE}bodega/">Take a look around</a></div><figure class="bodega-small">'''+photo('wine')+'''<figcaption>Something for your glass.</figcaption></figure></section>'''+visitblock()+'''</main>'''
CATS=[('seasonal','Seasonal','Chef Pablo’s selections'),('lunch','Lunch','Tapas, paella & more'),('dessert','Dessert','Sweet things & after dinner'),('drinks','Cocktails & beer','From the bar'),('wine','Wine','By the glass & bottle'),('spirits','Spirits','For the last glass'),('all','Everything','The complete menu')]
def money(value):
 value=str(value or '')
 return ('$'+value) if value and value[0].isdigit() else value

def menu_page():
 out='''<main id="main"><section class="menu-cover"><div class="menu-cover-title"><span class="eyebrow">Aioli Bodega Española · Fall 2026</span><h1 lang="es">La carta.</h1><p>Come hungry. Follow your appetite.</p></div><div class="menu-cover-photo">'''+photo('vegetables',eager=True)+'''</div><div class="menu-cover-note"><span>De la cocina<br>y de la bodega.</span><p>Spanish plates,<br>good wine,<br>something sweet.</p></div></section><section class="menu-browser" aria-label="Restaurant menu"><aside class="menu-controls"><div class="menu-controls-inner"><p class="eyebrow">What are you in the mood for?</p><div class="category-buttons" role="group" aria-label="Menu category">'''+''.join(f'<button data-category="{cat}"><span class="category-number">{i+1:02}</span>{label}</button>' for i,(cat,label,sub) in enumerate(CATS))+'''</div><div class="menu-search"><label for="menu-search">Find a dish, drink or ingredient</label><input type="search" id="menu-search" placeholder="Paella, Rioja, chocolate…" autocomplete="off"></div><label class="glass-filter" hidden><input type="checkbox" id="by-glass"> Available by the glass</label><p class="menu-source-note">Fall 2026 menus.<br>Prices & availability may change.</p><button class="print-menu text-link" type="button">Print this selection</button></div></aside><div class="menu-results"><div class="menu-section-title"><div><span class="eyebrow" id="category-kicker">Full food &amp; drinks menu</span><h2 id="category-title">The menu</h2></div><span class="menu-edition">Buen<br><em>provecho.</em></span></div><div class="menu-status"><p id="menu-status" role="status" aria-live="polite"></p><button class="clear-search" hidden>Clear search</button></div><div class="empty-state" hidden><h3>Nothing on the table yet.</h3><p>Try another name or ingredient, or browse everything.</p><button class="button reset-menu">Show the full menu</button></div>'''
 for group in MENU:
  cat=group.get('category',group.get('section','seasonal'))
  iswine=cat=='wine'
  out+=f'<section class="menu-group {"wine-group" if iswine else ""}" data-menu-category="{cat}"><h3>{esc(group["title"])}</h3>'
  if group.get('note'):out+='<p class="group-note">'+esc(group['note'])+'</p>'
  out+='<div class="dish-grid">'
  for item in group['items']:
   byglass=bool(item.get('glass'))
   out+=f'<article class="dish" data-glass="{str(byglass).lower()}"><div class="dish-main"><h4>{esc(item["name"])}</h4>'
   details=[]
   for field in ['description']:
    if item.get(field): details.append(str(item[field]))
   for field in ['vintage','region']:
    if item.get(field) and str(item[field]) not in ' '.join(details): details.append(str(item[field]))
   if details:out+='<p>'+esc(' · '.join(details))+'</p>'
   for option in item.get('options',[]):
    extra='+' if option.get('price_type')=='add-on' else ''
    out+='<p class="dish-option">'+esc(option['name'])+' <strong>'+extra+esc(money(option['price']))+'</strong></p>'
   out+='</div><div class="dish-prices">'
   if item.get('glass') or item.get('bottle'):
    for label,field in [('Glass','glass'),('Bottle','bottle')]:
     if item.get(field):out+=f'<span><small>{label}</small>{esc(money(item[field]))}</span>'
   else:
    price=money(item.get('price')) or 'Ask your server'
    out+='<span>'+esc(price)+'</span>'
   out+='</div></article>'
  out+='</div></section>'
 out+='''<p class="menu-disclaimer">Please tell your server about allergies or dietary requirements. Consuming raw or undercooked meat or eggs may increase the chance of foodborne illness. A 20% gratuity is included on parties of six or more. Lunch and bar selections retain the prices on their respective menus.</p></div></section>'''+sheets()+'''<section class="small-cta"><span class="eyebrow">Found something you like?</span><h2>Pull up a chair.</h2>'''+button('Book a table','{BASE}visit/#reservations')+'</section></main>'
 return out
BODEGA='''<main id="main"><section class="page-heading"><span class="eyebrow">The food. The wine. The little things.</span><h1>Inside<br>the bodega.</h1><p>Every corner has a little character.<br>Take your time looking around.</p></section><section class="gallery" aria-label="Photos of Aioli">'''+''.join(f'<figure class="gallery-{i}"><a class="gallery-open" href="{{BASE}}assets/images/{photos[k][0]}-960.webp" data-gallery="{i}" aria-label="Enlarge: {photos[k][1]}">{photo(k,sizes="(max-width:700px) 100vw, 50vw")}</a><figcaption><span>{i+1:02}</span>{label}<span>Enlarge</span></figcaption></figure>' for i,(k,label) in enumerate([('ceramic','A corner of the bodega'),('paella','Paella for the table'),('wine','Something from the cellar'),('lamb','From the grill'),('chandelier','Look a little closer'),('salad','Bright, fresh, full of flavor'),('sculpture','The character of Aioli'),('dessert','One last bite'),('vegetables','A seasonal plate'),('squid','From the kitchen')]))+'''</section><dialog class="lightbox" aria-label="Aioli photo gallery"><div class="lightbox-toolbar"><span class="gallery-count"></span><button class="close-lightbox">Close</button></div><img alt=""><div class="lightbox-bottom"><button class="prev-photo">Previous</button><p class="gallery-caption"></p><button class="next-photo">Next</button></div></dialog>'''+visitblock()+'''</main>'''
VISIT='''<main id="main"><section class="page-heading visit-heading"><span class="eyebrow">Midtown Sacramento · 1800 L Street</span><h1>Come on in.<br>Stay a while.</h1><p>Lunch plans. Dinner dates.<br>A table just because.</p></section><section class="reservation-panel" id="reservations"><div><span class="eyebrow">Good company starts here</span><h2>Your table<br>is calling.</h2><p>Find your table through OpenTable.<br>For questions or special arrangements, call us.</p><div class="reservation-actions">'''+button('Reserve on OpenTable',BOOK)+button('Call 916.447.9440','tel:+19164479440','outline')+'''</div><p class="booking-note">You’ll continue to Aioli’s booking page on OpenTable.</p></div>'''+photo('paella')+'''</section>'''+visitblock()+'''<section class="sister-spots"><span class="eyebrow">Around the neighborhood</span><h2>In good company.</h2><p>Meet our sister spots in Sacramento.</p><div><a href="https://brasseriedumonde.com/" target="_blank" rel="noopener"><h3>Brasserie du Monde</h3><span>1201 K Street</span><span>Visit website</span></a><a href="https://thegrandwinebar.com/" target="_blank" rel="noopener"><h3>The Grand Wine Bar</h3><span>1600 L Street</span><span>Visit website</span></a></div></section></main>'''
NOTFOUND='''<main id="main" class="not-found"><span class="eyebrow">404 · A little lost?</span><h1>This table<br>is empty.</h1><p>We couldn’t find that page. Let’s get you back to the bodega.</p>'''+button('Back to Aioli','{BASE}')+'</main>'
pages=[('index.html','Spanish kitchen & wine bar','Spanish tapas, paella, wine and cocktails in Midtown Sacramento.',HOME,''),('menu/index.html','The Menu','Explore Aioli’s full seasonal, lunch, dessert, cocktail, wine and spirits menus with prices.',menu_page(),'menu/'),('bodega/index.html','The Bodega','A look inside Aioli Bodega Española, its food, wine and dining-room details.',BODEGA,'bodega/'),('visit/index.html','Visit & Reservations','Reserve a table, find opening hours and get directions to Aioli Bodega Española in Sacramento.',VISIT,'visit/'),('404.html','Page not found','Return to Aioli Bodega Española.',NOTFOUND,'')]
DIST.mkdir(exist_ok=True)
for path,title,desc,body,active in pages:
 base='../' if '/' in path else './'
 html=(head(title,base,desc)+header(active)+body+footer()+'</body></html>').replace('{BASE}',base)
 for target in [ROOT/path,DIST/path]:target.parent.mkdir(parents=True,exist_ok=True);target.write_text(html)
for f in ['styles.css','app.js']:shutil.copy2(ROOT/f,DIST/f)
for d in ['assets','data']:shutil.copytree(ROOT/d,DIST/d,dirs_exist_ok=True)
for folder in [ROOT,DIST]:
 (folder/'.nojekyll').write_text('');(folder/'robots.txt').write_text('User-agent: *\nDisallow: /\n')
print(f'Built five pages, {sum(len(g["items"]) for g in MENU)} readable menu entries and seven original menu sheets.')
