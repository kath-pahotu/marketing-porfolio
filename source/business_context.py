"""Extend the campaign-led site with business context, without replacing its design."""
from pathlib import Path
from bs4 import BeautifulSoup
from html import escape as e
import hashlib, os, shutil
from content import CASES
from business_explorer import render_explorer, attach_assets

ROOT=Path(os.environ.get('MARKETING_OUTPUT_DIR',Path(__file__).resolve().parent.parent))
SITE=ROOT/'website'
def fragment(s): return BeautifulSoup(s,'html.parser')
def save(p,s): p.write_text(str(s),encoding='utf-8')
def link(slug,label): return f'<a href="/work/{slug}/">{e(label)}</a>'

CONTEXT={
 'golden-owl':('B2B technology services','A software outsourcing agency sells project expertise through a longer, sales-assisted buying process. Relevant enquiries and lead quality matter more than traffic alone.','Search and content create demand; service pages help prospects evaluate the offer; sales feedback determines which audiences deserve more investment.',['conversion-optimization','lead-quality','leaserunner']),
 'the-lab':('Consumer education','Parents in Singapore choose coding and STEM programmes around children’s needs, trust and school-holiday timing. The measured outcome here is an enquiry, not a paid enrolment.','Paid search captures active intent and social builds consideration. Lead quality and enrolment follow-up are the next checks before scaling.',['golden-owl','rokt','campaign-targeting']),
 'leaserunner':('SaaS and online landlord services','Landlords arrive with practical questions about screening, rental processes and local requirements. The website must connect useful resources with a relevant service and signup.','Technical SEO and content architecture bring people in; internal journeys and signup reporting show whether that attention reaches product intent.',['turisvpn','conversion-optimization','lead-quality']),
 'turisvpn':('Consumer software and SaaS','A VPN product attracts both broad information seekers and people with an immediate product need. A download is a useful intent signal, but does not establish activation or retained use.','Content clusters and localization build reach; topic-level download measurement guides editorial priorities and the next product-journey test.',['leaserunner','thelook','rokt']),
 'conversion-optimization':('B2B technology services','An agency website supports a considered purchase. Readers need a path from educational content to service evaluation, contact and a sales conversation.','This is the conversion layer of the Golden Owl demand programme. Acquisition brings visitors; the journey and sales handoff determine whether they become qualified opportunities.',['golden-owl','lead-quality','thelook']),
 'lead-quality':('B2B pipeline and sales collaboration','A lead has commercial value only when its need, market and stage fit the service. Source volume must be read alongside qualification and sales progression.','The reporting loop returns sales feedback to audience selection, campaign allocation and website priorities.',['golden-owl','conversion-optimization','campaign-targeting']),
 'laptop-sgn':('Retail ecommerce and electronics','An electronics retailer needs traffic to become informed product choices, purchases and repeat business. Channel quality, merchandising and funnel friction belong in the same review.','Professional ecommerce analysis connects acquisition with product-to-cart behaviour. TheLook extends those questions into an independent lifecycle and BI study.',['thelook','growth-and-retention','rokt']),
 'campaign-targeting':('Banking and campaign efficiency','A bank’s outbound campaign has limited call capacity. The business choice is which customers to prioritize while protecting reach and customer experience.','Independent propensity analysis supports audience planning. It complements campaign execution but needs a prospective pilot before claiming live improvement.',['the-lab','rokt','promotion-review']),
 'promotion-review':('Digital wallets and promotion economics','Promotions spend money to encourage customer use. A review team needs to understand where credited cost concentrates without treating unusual behaviour as proven abuse.','Independent review prioritization connects budget exposure with operational capacity and customer-impact guardrails. It does not establish saved budget.',['growth-and-retention','campaign-targeting','rokt']),
 'growth-and-retention':('Mobility and delivery marketplaces','A marketplace balances partner scale, customer demand and subsidy intensity. Acquisition is valuable when it supports repeat use and commercially sustainable growth.','This confidential, independent Excel case links growth, retention and channel measurement. Public conclusions are qualitative; forecasts and tests are recommendations.',['laptop-sgn','promotion-review','thelook']),
 'thelook':('Retail ecommerce and lifecycle marketing','Retail growth depends on what happens after the first visit: cart progression, completed purchases, returns and repeat behaviour. TheLook uses synthetic data to examine that journey.','Independent funnel and customer analysis extends the retail questions in Laptop SGN. Segments become testable lifecycle priorities, not claims of launched campaigns.',['laptop-sgn','turisvpn','rokt']),
 'rokt':('Advertising and incrementality','A holdout asks whether advertising creates conversions beyond those that would have happened anyway. It informs an investment decision rather than just a reporting dashboard.','Independent experiment analysis supplies a measurement discipline for paid acquisition and lifecycle tests. Assignment ambiguity must be resolved before sizing rollout.',['the-lab','campaign-targeting','thelook']),
}
by_slug={c['slug']:c for c in CASES}
labels={'conversion-optimization':'Golden Owl conversion','lead-quality':'Golden Owl lead quality','golden-owl':'Golden Owl acquisition','leaserunner':'LeaseRunner SEO','turisvpn':'TurisVPN content'}
for c in CASES:
 p=SITE/'work'/c['slug']/'index.html';s=fragment(p.read_text(encoding='utf-8'))
 domain,model,connection,related=CONTEXT[c['slug']]
 block=f'<section class="business-case" id="business-context"><h2>{e(domain)}: the business behind the work</h2><p>{e(model)}</p><p><strong>How the work connects:</strong> {e(connection)}</p><p class="business-links">'+''.join(link(x,labels.get(x,by_slug[x]['client'])) for x in related)+'</p></section>'
 s.select_one('#challenge').insert_before(fragment(block))
 nav=s.select_one('.case-nav');nav.insert(0,fragment('<a href="#business-context">Business context</a>'))
 related_box=s.select_one('.related');related_box.clear()
 for x in related[:2]:
  other=by_slug[x];related_box.append(fragment(f'<a href="/work/{x}/"><span>{e(other["client"])}</span><h3>{e(other["title"])}</h3></a>'))
 save(p,s)

homepath=SITE/'index.html';home=fragment(homepath.read_text(encoding='utf-8'))
home.select_one('.hero-lede').string='I lead paid campaigns, SEO and conversion work across B2B technology, SaaS and ecommerce. I set the plan, guide delivery and use customer evidence to improve the next decision.'
home.select_one('meta[name="description"]')['content']='Phan Hoai Thu’s digital marketing portfolio: paid campaigns, SEO, conversion and project leadership, supported by analytics across SaaS, ecommerce and consumer acquisition.'
selected=home.select_one('#work')
selected.select_one('.section-heading > p').string='Campaign strategy, channel execution and team leadership come together here. Each case connects the customer journey to a business goal and the evidence behind the result.'
selected.append(fragment('''<div class="campaign-followthrough"><h3>Carry demand through to conversion</h3><div class="campaign-links">
<article><h4>LeaseRunner: organic growth</h4><p>Connect landlord resources, technical SEO and service pages with a clearer path to signup.</p><a href="/work/leaserunner/">Explore SEO and website strategy</a></article>
<article><h4>Golden Owl: conversion</h4><p>Help educational content lead to service evaluation, enquiries and useful sales conversations.</p><a href="/work/conversion-optimization/">Explore the conversion work</a></article>
<article><h4>Golden Owl: lead quality</h4><p>Bring sales feedback into channel reviews so lead volume can be judged against commercial relevance.</p><a href="/work/lead-quality/">Explore the marketing–sales loop</a></article>
</div></div>'''))
# The complete-work link belongs after the campaign collection.
selected.append(selected.select_one('.all-work-link').extract())
ecosystem=render_explorer()
selected.insert_after(fragment(ecosystem))
support='''<section class="section wrap supporting-work" id="analytics"><div class="section-heading"><div><h2>Analytics behind the next marketing decision.</h2></div><p>Professional retail analysis and five solo studies deepen my measurement toolkit. They support campaign judgement, with the data source and limits stated in every case.</p></div><div class="supporting-links">'''
support_items=[('laptop-sgn','Where does retail traffic stop converting?','Professional work · Retail ecommerce'),('campaign-targeting','Who should a limited campaign reach first?','Independent study · Banking'),('promotion-review','Where does promotion cost concentrate?','Independent study · Digital wallets'),('growth-and-retention','Is growth supported by repeat use?','Independent confidential case · Marketplace'),('thelook','What follows the first purchase?','Independent synthetic-data study · Ecommerce'),('rokt','Did the advertising add conversions?','Independent holdout analysis · Experimentation')]
for slug,title,label in support_items:
 c=by_slug[slug];support+=f'<article><small>{e(label)}</small><h3><a href="/work/{slug}/">{e(title)}</a></h3><p>{e(c["intro"])}</p></article>'
support+='</div><p class="all-work-link"><a class="button secondary" href="https://kathuatwork.com/">Explore my Data / BI portfolio</a></p></section>'
home.select_one('#approach').insert_after(fragment(support))
about=home.select_one('#about .about-grid > div')
paras=about.find_all('p',recursive=False)
for p in paras:
 if p.get_text().startswith('I enjoy the full process:'):
  p.string='My commercial foundation spans SaaS client projects, B2B demand generation, Etsy/Amazon marketplace operations and electronics retail. Different journeys call for different messages, KPIs and delivery plans.'
home.select_one('.capabilities dd:nth-of-type(3)').string='GA4, GTM, Looker Studio, Excel, SQL and customer segmentation; Power BI and Python in independent projects'
nav=home.select_one('#navigation');nav.select_one('a[href="/#approach"]').insert_before(fragment('<a href="/#business">Business context</a>'))
attach_assets(home)
save(homepath,home)

# Make the two layers explicit in the complete library; keep the original filters.
libpath=SITE/'work/index.html';lib=fragment(libpath.read_text(encoding='utf-8'))
grid=lib.select_one('.work-grid');cards=grid.select('.work-card');grid.clear()
professional=lib.new_tag('div',attrs={'class':'work-grid','data-layer':'professional'})
independent=lib.new_tag('div',attrs={'class':'work-grid','data-layer':'independent'})
for c,card in zip(CASES,cards):
 (professional if c['kind'].startswith('Professional') else independent).append(card)
grid['class']=['work-layers']
grid.append(fragment('<h2 class="library-layer">Campaigns and professional delivery</h2><p class="library-layer-note">Paid acquisition, organic growth, conversion, sales feedback and retail measurement.</p>'));grid.append(professional)
grid.append(fragment('<h2 class="library-layer">Independent analytics supporting marketing</h2><p class="library-layer-note">Five solo studies in targeting, promotion efficiency, marketplace growth, lifecycle behaviour and experimentation.</p>'));grid.append(independent)
for layer in [professional,independent]:
 group=lib.new_tag('section',attrs={'class':'library-group'})
 note=layer.find_previous_sibling('p');heading=note.find_previous_sibling('h2')
 heading.insert_before(group);group.append(heading.extract());group.append(note.extract());group.append(layer.extract())
lib.select_one('.result-count').string=f'{len(CASES)} case studies'
save(libpath,lib)

# Keep the campaign CV primary, and retain the analyst CV at its existing URL.
css=ROOT/'source/business.css';shutil.copy2(css,SITE/'business.css')
digest=hashlib.sha256(css.read_bytes()).hexdigest()[:10]
for p in SITE.rglob('*.html'):
 s=fragment(p.read_text(encoding='utf-8'))
 n=s.select_one('#navigation')
 if n and not n.select_one('a[href="/#business"]'):
  n.select_one('a[href="/#approach"]').insert_before(fragment('<a href="/#business">Business context</a>'))
 if not s.select_one('link[href^="/business.css"]'):
  s.head.append(s.new_tag('link',rel='stylesheet',href=f'/business.css?v={digest}'))
 save(p,s)
# Glassdoor is outside the five independent studies in the current brief.
old=SITE/'work/glassdoor/index.html'
old.write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=/work/"><meta name="robots" content="noindex"><title>Explore marketing work</title></head><body><a href="/work/">Explore marketing work</a></body></html>',encoding='utf-8')
for oldslug,newslug in [('mobility','growth-and-retention'),('zalopay','promotion-review')]:
 p=SITE/'work'/oldslug/'index.html';p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=/work/{newslug}/"><link rel="canonical" href="https://kathuonmkt.vercel.app/work/{newslug}/"><title>Marketing case study</title></head><body><a href="/work/{newslug}/">Read the case study</a></body></html>',encoding='utf-8')
print('Campaign-first homepage, two-layer library and business context updated.')
