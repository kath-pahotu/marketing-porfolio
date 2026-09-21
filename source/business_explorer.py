"""Campaign-led business context: journey, ecosystem and domain spotlight."""
from pathlib import Path
from html import escape as e
import hashlib
import os
import shutil
from bs4 import BeautifulSoup

ROOT = Path(os.environ.get('MARKETING_OUTPUT_DIR', Path(__file__).resolve().parent.parent))
SITE = ROOT / 'website'

DOMAINS = {
 'saas': {
  'name': 'B2B & SaaS', 'icon': 'saas', 'summary': 'From customer questions to qualified demand',
  'foundation': 'Golden Owl, TurisVPN & LeaseRunner',
  'context': 'Agency services and SaaS products need useful content, a clear offer and a path from interest to enquiry or signup.',
  'question': 'Which message and next step help someone evaluate the offer?',
  'title': 'Turn useful content into product intent.',
  'body': 'Connect SEO, content and conversion work so visibility supports a relevant product or service action.',
  'steps': ['Understand the customer need', 'Build demand with useful content', 'Connect interest to the offer'],
  'cases': [('golden-owl','Golden Owl','Acquisition strategy and delivery'),('turisvpn','TurisVPN','Content, localization and organic growth'),('leaserunner','LeaseRunner','SEO and the path to signup')],
  'support': [('thelook','TheLook','Independent funnel and lifecycle study')],
  'boundary': 'Professional delivery during Golden Owl, Apr 2024–Sep 2025. Downloads and signups indicate intent; they do not establish activation or revenue.',
 },
 'commerce': {
  'name': 'Ecommerce', 'icon': 'commerce', 'summary': 'From product discovery to repeat purchase',
  'foundation': 'Canawan + Laptop SGN',
  'context': 'Etsy and Amazon operations at Canawan and retail analysis for Laptop SGN ground my understanding of products, acquisition and purchase journeys.',
  'question': 'What helps a shopper move from discovery to a confident purchase?',
  'title': 'Connect the product to the purchase.',
  'body': 'Read channel quality, product selection and conversion friction together before choosing the next retail priority.',
  'steps': ['Match the product to the need', 'Understand the buying journey', 'Prioritize conversion and repeat value'],
  'cases': [('#experience','Canawan','Marketplace and dropshipping operations'),('laptop-sgn','Laptop SGN','Professional retail customer analysis')],
  'support': [('thelook','TheLook','Independent synthetic retail study'),('growth-and-retention','Mobility & delivery','Independent confidential marketplace study')],
  'boundary': 'Professional ecommerce experience informs the questions. TheLook and mobility are independent studies, not implemented marketing programmes.',
 },
 'education': {
  'name': 'Consumer acquisition', 'icon': 'education', 'summary': 'From audience needs to timely campaigns',
  'foundation': 'The Lab Singapore',
  'context': 'Parents considering coding and STEM programmes need a relevant offer, trust and the right timing around school holidays.',
  'question': 'How should the audience, message and media plan work together?',
  'title': 'Reach people at the right moment.',
  'body': 'Connect audience research and seasonal demand with a practical paid-media plan and clear lead targets.',
  'steps': ['Define the audience and timing', 'Guide the campaign delivery', 'Review lead quality before scaling'],
  'cases': [('the-lab','The Lab','Professional education campaign')],
  'support': [('campaign-targeting','Bank targeting','Independent audience-prioritization study'),('rokt','Rokt','Independent advertising holdout analysis')],
  'boundary': 'The Lab ran May–Jul 2025. Reported CPL compares May and June; leads are not paid enrolments. Supporting studies were completed independently.',
 },
}

STAGES = {
 'audience': {
  'label': 'Audience', 'title': 'Start with the customer.',
  'question': 'Who needs the offer, and what will matter to them?',
  'decision': 'My ownership: translate the business goal into audience priorities, project KPIs and a delivery plan.',
  'cases': [('the-lab','The Lab: campaign planning','Professional campaign','Connect parents’ needs, school-holiday timing and a coding/STEM offer to the campaign plan.'),('golden-owl','Golden Owl: demand strategy','Professional delivery','Connect a software agency’s service offer with customer questions and relevant acquisition channels.')],
  'support': [('campaign-targeting','Bank campaign targeting','Independent study in audience prioritization')],
  'boundary': 'The Lab and Golden Owl are professional work. Bank targeting demonstrates offline prioritization; it is not a campaign I launched.',
 },
 'demand': {
  'label': 'Build demand', 'title': 'Bring the right people in.',
  'question': 'Which channels and content earn relevant attention?',
  'decision': 'My ownership: plan channel activity, allocate resources, guide team members and track progress against KPIs.',
  'cases': [('turisvpn','TurisVPN: organic growth','Professional client work','Guide topic planning, localization and content delivery, using download intent to refine priorities.'),('the-lab','The Lab: paid acquisition','Professional campaign','Connect paid search and social activity to audience needs and campaign lead targets.')],
  'support': [('rokt','Rokt holdout analysis','Independent study in advertising incrementality')],
  'boundary': 'Downloads and enquiries are intermediate outcomes. The Rokt analysis uses a supplied dataset; I did not operate that advertising campaign.',
 },
 'conversion': {
  'label': 'Conversion', 'title': 'Make the next step clear.',
  'question': 'Does the journey help interest become meaningful action?',
  'decision': 'My ownership: connect content, website priorities and team delivery to a clearer route toward enquiry or signup.',
  'cases': [('conversion-optimization','Golden Owl: conversion work','Professional delivery','Connect educational content to service evaluation, enquiry and the sales conversation.'),('leaserunner','LeaseRunner: the signup journey','Professional client work','Bring landlord resources, technical SEO and service pages into a more connected customer journey.')],
  'support': [('thelook','TheLook ecommerce','Independent synthetic-data study of funnel friction')],
  'boundary': 'Signup is not a revenue measure. Golden Owl’s overall conversion change is observational, with several activities running concurrently.',
 },
 'learn': {
  'label': 'Learn & reinvest', 'title': 'Bring the learning back.',
  'question': 'What should the team improve or invest in next?',
  'decision': 'My ownership: review KPI progress, guide improvements and bring customer and sales evidence into the next plan.',
  'cases': [('lead-quality','Golden Owl: lead quality','Professional marketing–sales work','Read lead source and volume alongside commercial relevance and sales feedback.'),('laptop-sgn','Laptop SGN: retail behaviour','Professional retail analysis','Use funnel and repeat-customer behaviour to inform retail marketing priorities.')],
  'support': [('promotion-review','ZaloPay promotion review','Independent study of review capacity and cost exposure'),('growth-and-retention','Mobility & delivery','Independent confidential growth and retention study')],
  'boundary': 'Retail findings inform recommendations, not measured intervention uplift. Promotion-review signals do not establish fraud or recovered savings.',
 },
}

def icon(kind):
 paths = {
  'commerce':'<path d="M5 7h14l1 14H4L5 7Z"/><path d="M8 7V6a4 4 0 0 1 8 0v1"/>',
  'saas':'<path d="m12 3 10 5-10 5L2 8l10-5Zm-10 9 10 5 10-5M2 16l10 5 10-5"/>',
  'education':'<path d="m2 9 10-5 10 5-10 5-10-5Zm4 2v6c3 3 9 3 12 0v-6M22 9v8"/>',
 }
 return f'<svg class="bx-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[kind]}</svg>'

def url(slug):
 return '/'+slug if slug.startswith('#') else f'/work/{slug}/'

def links(cases):
 return '<ul class="bx-cases">'+''.join(f'<li><a href="{url(slug)}"><strong>{e(name)}</strong><span>{e(label)}</span></a></li>' for slug,name,label in cases)+'</ul>'

def supporting(cases):
 return '<details class="bx-support"><summary>Supporting analysis</summary>'+links(cases)+'</details>'

def choices(group,items,rich=False):
 return f'<div class="bx-choices bx-choices--{group}" role="group" aria-label="{("Explore a customer journey stage" if group=="journey" else "Explore a business domain")}" data-bx-controls="{group}" hidden>'+''.join(
  f'<button type="button" class="bx-choice" data-bx-choice="{key}" aria-pressed="{str(i==0).lower()}" aria-controls="bx-{group}-{key}">'+(icon(d['icon']) if rich else '')+f'<strong>{e(d.get("name",d.get("label","")))}</strong>'+(f'<span>{e(d["summary"])}</span>' if rich else '')+'</button>' for i,(key,d) in enumerate(items.items()))+'</div>'

def render_explorer():
 ecosystem='<div class="bx-map"><div class="bx-hub">Move the customer forward<span>Audience · Offer · Action</span></div>'+choices('ecosystem',DOMAINS,True)+'</div>'
 spotlight=choices('spotlight',DOMAINS)
 for key,d in DOMAINS.items():
  ecosystem+=f'<div class="bx-domain-detail" id="bx-ecosystem-{key}" data-bx-detail="ecosystem" data-bx-key="{key}"><div class="bx-context"><p class="bx-label">Commercial context</p><h3>{e(d["foundation"])}</h3><p>{e(d["context"])}</p><p class="bx-question-inline">{e(d["question"])}</p></div><div><p class="bx-label">Campaigns and professional work</p>{links(d["cases"])}{supporting(d["support"])}<p class="bx-boundary">{e(d["boundary"])}</p></div></div>'
  spotlight+=f'<div class="bx-spotlight" id="bx-spotlight-{key}" data-bx-detail="spotlight" data-bx-key="{key}"><div><h3>{e(d["title"])}</h3><p>{e(d["body"])}</p>{links(d["cases"])}{supporting(d["support"])}<p class="bx-boundary">{e(d["boundary"])}</p></div><div class="bx-visual" aria-label="{e(d["name"])} marketing sequence">{icon(d["icon"])}<ol>'+''.join(f'<li><span>{e(step)}</span></li>' for step in d['steps'])+'</ol></div></div>'
 journey=choices('journey',STAGES)
 for key,d in STAGES.items():
  journey+=f'<div class="bx-journey" id="bx-journey-{key}" data-bx-detail="journey" data-bx-key="{key}"><div class="bx-question"><h3>{e(d["title"])}</h3><p>{e(d["question"])}</p><p class="bx-decision">{e(d["decision"])}</p></div><div>'
  for slug,title,provenance,desc in d['cases']:
   journey+=f'<article class="bx-evidence"><p class="bx-label">{e(provenance)}</p><h4><a href="{url(slug)}">{e(title)}</a></h4><p>{e(desc)}</p></article>'
  journey+=supporting(d['support'])+f'<p class="bx-boundary">{e(d["boundary"])}</p></div></div>'
 panels=[('journey','Journey',journey),('ecosystem','Ecosystem',ecosystem),('spotlight','Spotlight',spotlight)]
 return '<section class="business-explorer" id="business" aria-labelledby="bx-heading"><div class="business-map-inner"><header class="bx-header"><div><h2 id="bx-heading">One customer journey.<br/>Connected marketing decisions.</h2><p>See how I connect audience needs, campaign delivery and conversion across different businesses.</p></div><div class="bx-tabs" role="tablist" aria-label="Marketing context views" hidden>'+''.join(f'<button type="button" id="bx-tab-{key}" role="tab" aria-controls="bx-view-{key}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}">{label}</button>' for i,(key,label,_) in enumerate(panels))+'</div></header>'+''.join(f'<div class="bx-view" id="bx-view-{key}" role="tabpanel" aria-labelledby="bx-tab-{key}" data-bx-view="{key}"><h3 class="bx-fallback-heading">{label}</h3>{content}</div>' for key,label,content in panels)+'<p class="bx-announcement" role="status" aria-live="polite" aria-atomic="true"></p></div></section>'

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
