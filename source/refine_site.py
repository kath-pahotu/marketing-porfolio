"""Apply recruiter-focused presentation to generated marketing pages."""
from pathlib import Path
from bs4 import BeautifulSoup
from html import escape as e
from PIL import Image, ImageDraw, ImageFont
import os,re,json,shutil
from content import CASES, PROFILE

root=Path(os.environ.get('MARKETING_OUTPUT_DIR',Path(__file__).resolve().parent.parent))
site=root/'website'
shutil.copy2(root/'source'/'refinements.css',site/'refinements.css')
def fragment(s):return BeautifulSoup(s,'html.parser')
def save(path,soup):path.write_text(str(soup),encoding='utf-8')

tables={
 'golden-owl':('Acquisition and visibility evidence',['Measure','Baseline','Later observation'],[
  ['Monthly visits','3,000 · Jun 2024','30,000 · Jun 2025'],
  ['Work-with-us cost per lead','VND 1.6M','VND 736K'],
  ['Top-5 keywords','—','228 · May 2025']], 'Traffic, paid-media and ranking figures use different reporting windows.'),
 'the-lab':('Meta acquisition: May to June 2025',['Measure','May','June'],[
  ['Spend','SG$951.50','SG$849.10'],['Leads','9','14'],['Cost per lead','SG$105.72','SG$60.65']],
  'Cost per lead = spend ÷ leads. July planning is part of the three-month engagement; these results compare May and June only.'),
 'leaserunner':('Organic acquisition evidence',['Measure','Baseline','Later observation'],[
  ['Monthly visits','5,600 · Dec 2024','27,500 · Jun 2025'],['Organic share of sessions','—','81% · Jun 2025']],
  'Traffic is an acquisition measure; signup, activation and revenue require separate measurement.'),
 'turisvpn':('Organic topic-to-download performance',['Content theme','Download rate','Decision'],[
  ['VPN','2.15%','Prioritize product-intent topics'],['Streaming','0.26%','Improve the path from discovery to product'],['Browsing','1.73%','Develop relevant content'],['IP','4.01%','Validate the smaller 474-session sample']],
  'Topic analysis: 1 Apr–7 Jul 2025. Download events are a product-interest proxy, not verified activation.'),
 'laptop-sgn':('Where the customer journey narrows',['Step or audience','Observed rate'],[
  ['Product page → cart','21.46%'],['Cart → checkout','27.47%'],['Checkout → purchase','63.46%'],['Returning-user conversion','2.50%'],['New-user conversion','1.07%']],
  'Each rate retains its own denominator. These are observed behaviours, not measured uplift from a launched intervention.')
}
for c in CASES:
 path=site/'work'/c['slug']/'index.html'; s=BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser')
 role=fragment(f'''<section class="case-brief" aria-label="Project summary"><dl><div><dt>My role</dt><dd>{e(c['role'])}</dd></div><div><dt>Period</dt><dd>{e(c['period'])}</dd></div><div><dt>Engagement</dt><dd>{e(c['engagement'])}</dd></div></dl><p><strong>Business objective:</strong> {e(c['goal'])}</p><p><strong>My ownership:</strong> {e(c['ownership'])}</p></section>''')
 s.select_one('.case-hero').append(role)
 s.select_one('.back-link')['href']='/work/'
 s.select_one('#work-done h2').string='How I delivered the work'
 evidence=s.select_one('#evidence')
 if c['slug'] in tables:
  title,cols,rows,note=tables[c['slug']]
  html='<div class="evidence-table-wrap"><table class="evidence-table"><caption>'+e(title)+'</caption><thead><tr>'+''.join('<th scope="col">'+e(x)+'</th>' for x in cols)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(('<th scope="row">' if i==0 else '<td>')+e(v)+('</th>' if i==0 else '</td>') for i,v in enumerate(row))+'</tr>' for row in rows)+'</tbody></table></div><p class="evidence-note">'+e(note)+'</p>'
  evidence.h2.insert_after(fragment(html))
  pictures=evidence.find_all('figure')
  details=s.new_tag('details',attrs={'class':'source-materials'}); summary=s.new_tag('summary'); summary.string='View original campaign materials'; details.append(summary)
  for pic in pictures:
   cap=pic.find('figcaption'); cap.string=re.sub(r',? page \d+','',cap.get_text()).replace('from the marketing portfolio','').replace('from the original analysis','').strip()
   details.append(pic.extract())
  evidence.append(details)
 else:
  # Keep the narrative evidence visible and descriptive; original charts can be opened at full size.
  for cap in evidence.select('figcaption'):
   cap.string=re.sub(r',? page \d+','',cap.get_text()).replace('from the marketing portfolio','').strip()
 for li in s.select('#context li'):
  if 'Supplied PDF' in li.get_text():li.string='Source: campaign reports and project materials reproduced on this page.'
 if c['slug']=='growth-and-retention':
  evidence.append(fragment('<p><a class="button primary" href="https://kathuatwork.com/private/mobility/">Open detailed case with password</a></p>'))
 save(path,s)

homepath=site/'index.html'; home=BeautifulSoup(homepath.read_text(encoding='utf-8'),'html.parser')
library_section=home.select_one('#work').extract()
library_section.select_one('h2').string='Explore all projects'
library_section.select_one('h2').name='h1'
library_section.select_one('.section-kicker').string='Campaigns and independent analysis'
library_section.select_one('.section-heading > p').string='Professional delivery first, followed by solo projects in the order I completed them.'
for c, card in zip(CASES,library_section.select('.work-card')):
 label=home.new_tag('p',attrs={'class':'project-period'}); label.string=c['period']; card.select_one('.card-meta').insert_after(label)
lib=BeautifulSoup(str(home),'html.parser');lib.main.clear();lib.main.append(library_section)
lib.title.string='All projects | Phan Hoai Thu | KAThu on marketing'
lib.select_one('link[rel="canonical"]')['href']=PROFILE['site']+'/work/'
lib.select_one('meta[property="og:url"]')['content']=PROFILE['site']+'/work/'
lib.select_one('meta[property="og:title"]')['content']='Campaigns and independent projects | Phan Hoai Thu'
lib.select_one('meta[name="description"]')['content']='Browse Phan Hoai Thu’s paid acquisition, SEO, conversion and independent analytics work.'
save(site/'work'/'index.html',lib)

home.h1.string='Digital marketing, from strategy to conversion.'
home.select_one('.hero-lede').string='I lead paid acquisition, SEO and conversion projects: set the plan, guide the team and use analytics to improve the next decision.'
home.select_one('.hero-location').string='3+ years in marketing and e-commerce · Ho Chi Minh City'
home.select_one('.hero-note span').string='My role'
home.select_one('.hero-note p').clear(); home.select_one('.hero-note p').append(fragment('Set the direction.<br/>Own the delivery.'))
featured=home.select_one('section[aria-labelledby="selected-heading"]');featured['id']='work'
featured.select_one('h2').string='Selected campaign work'
featured.select_one('.section-kicker').decompose()
featured.append(fragment('<p class="all-work-link"><a class="button secondary" href="/work/">Browse all 12 projects</a></p>'))
exp=home.select_one('#experience').extract();featured.insert_after(exp)
home.select_one('#about h2').clear();home.select_one('#about h2').append(fragment('Marketing leadership.<br/>Analytical depth.'))
home.select_one('#about p:nth-of-type(2)').string='I’m Thu, also known as Katherine. I turn business objectives into project KPIs, milestones and a practical delivery plan across paid campaigns, organic growth and customer journeys.'
home.select_one('#approach h2').string='Plan clearly. Guide the team. Measure progress.'
save(homepath,home)

# A text-based sharing card; deliberately independent of private project screenshots.
im=Image.new('RGB',(1200,630),'#f6f4fc');d=ImageDraw.Draw(im)
f=lambda n:ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',n)
d.rounded_rectangle((65,65,1135,565),radius=28,fill='white')
d.text((110,115),'Phan Hoai Thu',font=f(36),fill='#5936c9')
d.text((110,205),'Digital marketing,',font=f(62),fill='#252338')
d.text((110,282),'from strategy to conversion.',font=f(56),fill='#252338')
d.text((110,435),'Paid acquisition · SEO · Conversion · Analytics',font=f(26),fill='#5936c9')
im.save(site/'assets'/'social-preview.png',optimize=True)
for path in site.rglob('*.html'):
 s=BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser')
 if s.select_one('meta[http-equiv="refresh"]'):continue
 for name,value in [('og:image',PROFILE['site']+'/assets/social-preview.png'),('og:image:width','1200'),('og:image:height','630'),('og:image:alt','Phan Hoai Thu — digital marketing, from strategy to conversion')]:
  tag=s.new_tag('meta',attrs={'property':name,'content':value});s.head.append(tag)
 s.select_one('meta[name="twitter:card"]')['content']='summary_large_image'
 s.head.append(s.new_tag('link',attrs={'rel':'stylesheet','href':'/refinements.css?v=20260915'}))
 # Use actual image dimensions to reserve the correct layout space.
 for img in s.select('img[src^="/assets/"]'):
  with Image.open(site/img['src'].lstrip('/')) as asset:img['width']=str(asset.width);img['height']=str(asset.height)
 save(path,s)
sitemap=(site/'sitemap.xml').read_text();(site/'sitemap.xml').write_text(sitemap.replace('</urlset>','<url><loc>'+PROFILE['site']+'/work/</loc></url></urlset>'))
print('Refined homepage, all-work library and 12 case summaries')
