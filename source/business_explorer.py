"""Business-specific marketing choices, with one insight and example per context."""
from pathlib import Path
from html import escape as e
import hashlib
import os
import shutil
from bs4 import BeautifulSoup

ROOT = Path(os.environ.get("MARKETING_OUTPUT_DIR", Path(__file__).resolve().parent.parent))
SITE = ROOT / "website"

THEME = 'marketing'
SECTION_ID = 'business'
HEADING = 'Different buying decisions. Different marketing choices.'
INTRO = 'The buying situation changes the message, the path to action and what counts as success. Explore how I adapt the marketing choices to the business.'
DOMAINS = [{'key': 'saas',
  'name': 'B2B & SaaS',
  'icon': 'saas',
  'angle': 'A considered decision',
  'basis': 'Professional agency and SaaS marketing experience.',
  'title': 'Make expertise lead to a relevant next step.',
  'why': 'Prospects need to connect a service or product with a problem they recognize. I align useful content, '
         'the offer and the next action around that need.',
  'lens': [('Message', 'Answer the problem the prospect is already trying to solve.'),
           ('Journey', 'Connect search and educational content with service evaluation or product use.'),
           ('Success signal', 'A qualified enquiry for an agency; a relevant signup for a SaaS service.')],
  'case_url': '/work/golden-owl/',
  'case_name': 'Golden Owl demand generation',
  'evidence': 'Service-led campaigns, landing-page work and sales feedback connected acquisition with lead '
              'quality.',
  'limit': 'Professional delivery. Traffic and lead results cover different reporting windows.'},
 {'key': 'commerce',
  'name': 'Ecommerce',
  'icon': 'commerce',
  'angle': 'A product decision',
  'basis': 'Marketplace operations, supported by professional retail analysis.',
  'title': 'Help the shopper make a confident product choice.',
  'why': 'Retail marketing has to connect the reason to visit with the product a shopper needs. I read '
         'acquisition alongside product discovery, purchase friction and repeat behaviour.',
  'lens': [('Message', 'Match product information and content to the shopper’s need.'),
           ('Journey', 'Connect discovery with product evaluation, cart progression and return visits.'),
           ('Success signal', 'Completed purchases and repeat-customer behaviour, read alongside acquisition.')],
  'case_url': '/#experience',
  'case_name': 'Canawan marketplace experience',
  'evidence': 'Content planning, SEO and ecommerce operations connected product discovery with the offer across '
              'Etsy and Amazon work.',
  'limit': 'Professional ecommerce experience. Retail analysis informs recommendations, not a claim of launched '
           'retention uplift.'},
 {'key': 'education',
  'name': 'Education',
  'icon': 'education',
  'angle': 'A time-sensitive decision',
  'basis': 'Professional consumer acquisition work for The Lab Singapore.',
  'title': 'Timing is part of the offer.',
  'why': 'Parents consider a course in the context of their child’s needs and the school calendar. The audience, '
         'message and media plan need to meet that decision window.',
  'lens': [('Message', 'Connect the course with parents’ needs, age fit and holiday plans.'),
           ('Journey', 'Use search for active intent and social to build consideration before the decision.'),
           ('Success signal', 'Review enquiries by platform and quality; paid enrolment needs follow-up.')],
  'case_url': '/work/the-lab/',
  'case_name': 'The Lab education campaign',
  'evidence': 'Audience planning and spend pacing followed the June school-holiday period.',
  'limit': 'May–Jul 2025 professional project. Enquiries are not confirmed paid enrolments.'}]


def icon(kind):
    paths = {
        'commerce': '<path d="M5 7h14l1 14H4L5 7Z"/><path d="M8 7V6a4 4 0 0 1 8 0v1"/>',
        'saas': '<path d="m12 3 10 5-10 5L2 8l10-5Zm-10 9 10 5 10-5M2 16l10 5 10-5"/>',
        'finance': '<path d="m2 8 10-5 10 5H2Zm2 3v7m5-7v7m6-7v7m5-7v7M2 21h20"/>',
        'education': '<path d="m2 9 10-5 10 5-10 5-10-5Zm4 2v6c3 3 9 3 12 0v-6M22 9v8"/>',
    }
    return f'<svg class="bc-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[kind]}</svg>'


def render_explorer():
    html = f'<section class="business-explorer bc-{THEME}" id="{SECTION_ID}" aria-labelledby="bc-heading"><div class="bc-inner"><header class="bc-header"><h2 id="bc-heading">{HEADING}</h2><p>{e(INTRO)}</p></header><div class="bc-choices" role="tablist" aria-label="Choose a business context" hidden>'
    for i, d in enumerate(DOMAINS):
        html += f'<button type="button" id="bc-tab-{d["key"]}" role="tab" aria-controls="bc-panel-{d["key"]}" aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}">{icon(d["icon"])}<span><strong>{e(d["name"])}</strong><small>{e(d["angle"])}</small></span></button>'
    html += '</div>'
    for d in DOMAINS:
        html += f'<div class="bc-panel" id="bc-panel-{d["key"]}" role="tabpanel" aria-labelledby="bc-tab-{d["key"]}" tabindex="0"><div class="bc-insight"><p class="bc-basis">{e(d["basis"])}</p><h3>{e(d["title"])}</h3><p class="bc-why">{e(d["why"])}</p><div class="bc-example"><a href="{d["case_url"]}">{e(d["case_name"])}</a><p>{e(d["evidence"])}</p><small>{e(d["limit"])}</small></div></div><dl class="bc-lens">'
        for label, text in d['lens']:
            html += f'<div><dt>{e(label)}</dt><dd>{e(text)}</dd></div>'
        html += '</dl></div>'
    return html + '</div></section>'

def attach_assets(soup):
 for name,tag,attr in [('business-explorer.css','link','href'),('business-explorer.js','script','src'),('portrait.css','link','href')]:
  source=ROOT/'source'/name;shutil.copy2(source,SITE/name)
  for old in soup.select(f'{tag}[{attr}^="/{name}"]'):old.decompose()
  digest=hashlib.sha256(source.read_bytes()).hexdigest()[:10]
  node=soup.new_tag(tag,**{attr:f'/{name}?v={digest}'})
  if tag=='link':node['rel']='stylesheet';soup.head.append(node)
  else:node['defer']='';soup.body.append(node)

def update_home():
 p=SITE/'index.html';soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 old=soup.select_one('#business')
 if old is None:raise RuntimeError('Missing marketing business section')
 old.replace_with(BeautifulSoup(render_explorer(),'html.parser'))
 attach_assets(soup)
 soup.select_one('.portrait-frame img')['alt']='Phan Hoai Thu at The Future of Artificial Intelligence event'
 soup.select_one('.portrait-frame img')['src']='/assets/katherine-ava.png'
 p.write_text(str(soup),encoding='utf-8')

if __name__=='__main__':
 update_home()
