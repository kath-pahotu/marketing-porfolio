"""Ordered project collections with distinct business context and supporting experience."""
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
HEADING = 'Different markets. A full body of work.'
INTRO = 'Explore campaign strategy and delivery, then the conversion, measurement and independent analysis that inform the next marketing decision.'
DOMAINS = [{'key': 'saas',
  'name': 'B2B & SaaS',
  'icon': 'saas',
  'angle': 'Demand, content & conversion',
  'title': 'Make expertise lead to a relevant next step.',
  'why': 'The message, content and offer need to meet a problem the buyer recognizes. Campaign delivery '
         'comes first; measurement sharpens the next move.',
  'decision': 'Connect useful content and service offers with qualified demand.',
  'groups': [{'title': 'Campaign strategy & delivery',
              'intro': 'Integrated acquisition first, followed by dedicated organic-growth programmes.',
              'projects': [{'name': 'Golden Owl demand generation',
                            'url': '/work/golden-owl/',
                            'kind': 'Professional campaign leadership',
                            'summary': 'An integrated acquisition programme connecting paid campaigns, SEO, '
                                       'newsletters, landing pages and sales feedback.',
                            'methods': 'Google Ads, Meta Ads, SEO, campaign planning',
                            'scope': 'I translated business objectives into project KPIs, planned '
                                     'service-led campaigns, allocated resources and guided delivery across '
                                     'content, media and conversion work.',
                            'limit': 'Traffic and lead results cover different reporting windows; the case '
                                     'keeps those measures separate.'},
                           {'name': 'TurisVPN organic growth',
                            'url': '/work/turisvpn/',
                            'kind': 'Professional SaaS client campaign',
                            'summary': 'SEO launch, content clusters and localization build visibility '
                                       'around relevant product needs.',
                            'methods': 'SEO, content strategy, localization, GA4',
                            'scope': 'I led content planning and delivery, with topic-level engagement and '
                                     'download reviews informing what to prioritize next.',
                            'limit': 'A download indicates intent; it does not establish activation, '
                                     'retention or revenue.'},
                           {'name': 'LeaseRunner search & signup journey',
                            'url': '/work/leaserunner/',
                            'kind': 'Professional SaaS client campaign',
                            'summary': 'Technical SEO, content architecture and navigation connect search '
                                       'discovery with the path to signup.',
                            'methods': 'Technical SEO, content planning, Looker Studio',
                            'scope': 'I planned the work and coordinated delivery across site structure, '
                                     'content and reporting, using search and signup evidence to guide '
                                     'priorities.',
                            'limit': 'Signups indicate a next step; they do not establish activation or '
                                     'revenue.'}]},
             {'title': 'Conversion & measurement',
              'intro': 'The work that improves the path to enquiry and closes the feedback loop.',
              'projects': [{'name': 'Golden Owl conversion roadmap',
                            'url': '/work/conversion-optimization/',
                            'kind': 'Professional conversion strategy',
                            'summary': 'Landing pages, forms and content paths are brought into an '
                                       'eight-part plan for turning interest into enquiries.',
                            'methods': 'GA4, Hotjar, HubSpot',
                            'scope': 'Blog-to-service progression, landing pages and forms are reviewed '
                                     'together to identify conversion constraints and prioritize changes.',
                            'limit': 'Observed conversion changes overlap with other activities and are not '
                                     'isolated causal effects.'},
                           {'name': 'Golden Owl lead-quality feedback',
                            'url': '/work/lead-quality/',
                            'kind': 'Professional campaign measurement',
                            'summary': 'CRM and acquisition reporting bring country, source and sales '
                                       'follow-up into the next marketing decision.',
                            'methods': 'Looker Studio, GA4, CRM data, Excel',
                            'scope': 'Reporting aligns lead definitions and sales feedback so marketing can '
                                     'distinguish enquiry volume from lead quality.',
                            'limit': 'Professional reporting used Looker Studio, not Power BI. This is '
                                     'lead-quality evidence, not a causal attribution study.'}]}],
  'context_title': 'My role at Golden Owl',
  'context': 'Apr 2024–Sep 2025. I owned project planning, KPI breakdown, resource allocation and team '
             'guidance across the agency and client work. Each case shows the delivery and evidence in more '
             'detail.',
  'context_url': '/#experience'},
 {'key': 'commerce',
  'name': 'Retail & marketplaces',
  'icon': 'commerce',
  'angle': 'Product choice & customer value',
  'title': 'Connect the reason to visit with a reason to buy again.',
  'why': 'Marketplace operations give me the commercial foundation. Professional retail analysis and '
         'independent studies deepen how I read purchase friction and repeat behaviour.',
  'decision': 'Improve the customer journey before assuming more traffic is the answer.',
  'groups': [{'title': 'Professional retail analysis',
              'intro': 'Applied customer insight that supports marketing priorities.',
              'projects': [{'name': 'Laptop SGN retail journey',
                            'url': '/work/laptop-sgn/',
                            'kind': 'Professional retail analysis',
                            'summary': 'Product-funnel and customer-segment analysis identifies where '
                                       'marketing can support purchase and return visits.',
                            'methods': 'BigQuery SQL, GA4, Excel, RFM',
                            'scope': 'A 41-slide analysis traces product discovery through purchase and '
                                     'compares new and returning users to identify practical retail '
                                     'priorities.',
                            'limit': 'Observational findings and recommendations, not measured intervention '
                                     'uplift.'}]},
             {'title': 'Independent analytical depth',
              'intro': 'A complete retail BI system, followed by a connected marketplace-growth case.',
              'projects': [{'name': 'TheLook customer lifecycle',
                            'url': '/work/thelook/',
                            'kind': 'Independent synthetic-data project',
                            'summary': 'A complete retail BI project adds a deeper view of customer '
                                       'segments, conversion and repeat value.',
                            'methods': 'SQL / DuckDB, Python, Power BI',
                            'scope': 'Data validation and ELT, session reconstruction, retail modelling, RFM '
                                     'and funnel analysis connect acquisition, orders and repeat customer '
                                     'value.',
                            'limit': 'Synthetic retail data. The report demonstrates analytical delivery; it '
                                     'does not establish commercial uplift.'},
                           {'name': 'Mobility & delivery growth',
                            'url': '/work/growth-and-retention/',
                            'kind': 'Independent confidential case',
                            'summary': 'Partner growth, customer retention and acquisition efficiency are '
                                       'read together to inform growth priorities.',
                            'methods': 'Excel, cohort analysis, forecasting, CAC / CIR',
                            'scope': 'Partner scale and subsidy intensity, customer cohorts, channel '
                                     'efficiency and directional forecasts feed an action matrix. Open the '
                                     'sanitized public summary.',
                            'limit': 'Independent case work, not employment. Detailed evidence remains '
                                     'password protected; proposed SQL and Python extensions are not '
                                     'delivered work.'}]}],
  'context_title': 'Marketing foundation at Canawan',
  'context': 'Sep 2022–Apr 2024. Etsy and Amazon operations, content planning, SEO and guidance of a '
             'three-person content team grounded my understanding of product discovery and marketplace '
             'delivery.',
  'context_url': '/#experience'},
 {'key': 'consumer',
  'name': 'Consumer acquisition',
  'icon': 'education',
  'angle': 'Education campaigns & ad effectiveness',
  'title': 'Plan for the buying moment, then question the result.',
  'why': 'The Lab shows how I deliver a seasonal education campaign. A separate advertising study adds depth '
         'to how I evaluate paid-media evidence.',
  'decision': 'Match the campaign to audience timing and judge what the spend achieved.',
  'groups': [{'title': 'Campaign strategy & delivery',
              'intro': 'Professional audience planning and media execution.',
              'projects': [{'name': 'The Lab education campaign',
                            'url': '/work/the-lab/',
                            'kind': 'Professional paid-acquisition campaign',
                            'summary': 'A three-month Singapore campaign connects parent audiences, '
                                       'school-holiday demand and a coordinated media plan.',
                            'methods': 'Google Search, Performance Max, Meta Ads',
                            'scope': 'May–Jul 2025: audience and keyword research, budget pacing, project '
                                     'KPIs and team coordination supported the June holiday decision window.',
                            'limit': 'Enquiries and cost per lead are intermediate outcomes, not confirmed '
                                     'paid enrolments.'}]},
             {'title': 'Independent measurement depth',
              'intro': 'A transferable advertising method, separate from The Lab campaign.',
              'projects': [{'name': 'Rokt advertising incrementality',
                            'url': '/work/rokt/',
                            'kind': 'Independent advertising study',
                            'summary': 'A holdout review asks whether advertising added conversions and how '
                                       'certain the recommendation can be.',
                            'methods': 'Python, statistical testing, experiment audit',
                            'scope': 'Event-level and user-cohort analyses are compared before making a '
                                     'conditional rollout recommendation. The assignment grain is treated as '
                                     'a material uncertainty.',
                            'limit': 'Supplied experiment data. This was not a campaign I operated, and the '
                                     'result depends on unresolved assignment assumptions.'}]}],
  'context_title': 'Delivery and study are separate',
  'context': 'I led The Lab’s project planning, KPI allocation and team coordination. Rokt is an independent '
             'analysis of a supplied holdout dataset, not a campaign I managed.',
  'context_url': None},
 {'key': 'finance',
  'name': 'Banking & fintech',
  'icon': 'finance',
  'angle': 'Audience & promotion priorities',
  'title': 'Focus limited budget and attention where they can matter.',
  'why': 'These solo studies extend my marketing toolkit into capacity-aware targeting and promotion '
         'economics.',
  'decision': 'Propose a testable campaign or review priority, with customer safeguards.',
  'groups': [{'title': 'Independent analytical depth',
              'intro': 'Audience modelling first, followed by promotion rules and BI reporting.',
              'projects': [{'name': 'Bank audience prioritization',
                            'url': '/work/campaign-targeting/',
                            'kind': 'Independent targeting study',
                            'summary': 'A pre-contact model turns historical response patterns into a '
                                       'practical proposal for a limited campaign pilot.',
                            'methods': 'SQL, Python, scikit-learn',
                            'scope': 'Model comparison and capacity evaluation: the top 20% of the '
                                     'historical contact list captured 51.8% of responders. The '
                                     'recommendation is a controlled campaign pilot.',
                            'limit': 'Offline predictive performance, not implemented campaign uplift.'},
                           {'name': 'ZaloPay promotion-cost review',
                            'url': '/work/promotion-review/',
                            'kind': 'Independent promotion study',
                            'summary': 'Promotion behaviour and cost exposure are connected with the team’s '
                                       'review capacity and customer-impact safeguards.',
                            'methods': 'T-SQL, Python, Power BI',
                            'scope': 'User-level reconciliation and explainable rules balance credited-cost '
                                     'coverage, review workload and customer-impact guardrails.',
                            'limit': 'Review signals are not confirmed fraud, and credited-cost exposure is '
                                     'not recovered savings.'}]}],
  'context_title': 'Research that supports marketing judgement',
  'context': 'These cases demonstrate end-to-end independent analysis, not financial-sector employment. '
             'Offline response lift and promotion-review signals are kept separate from implemented campaign '
             'results.',
  'context_url': None}]


def icon(kind):
    paths = {
        'commerce': '<path d="M5 7h14l1 14H4L5 7Z"/><path d="M8 7V6a4 4 0 0 1 8 0v1"/>',
        'saas': '<path d="m12 3 10 5-10 5L2 8l10-5Zm-10 9 10 5 10-5M2 16l10 5 10-5"/>',
        'finance': '<path d="m2 8 10-5 10 5H2Zm2 3v7m5-7v7m6-7v7m5-7v7M2 21h20"/>',
        'education': '<path d="m2 9 10-5 10 5-10 5-10-5Zm4 2v6c3 3 9 3 12 0v-6M22 9v8"/>',
        'experiment': '<path d="M9 3h6m-5 0v6L4 19a1 1 0 0 0 1 2h14a1 1 0 0 0 1-2L14 9V3M7 15h10"/>',
    }
    return f'<svg class="bc-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[kind]}</svg>'


def render_project(project, featured=False):
    p = project
    cls = 'bc-project bc-project-featured' if featured else 'bc-project'
    return (f'<li class="{cls}"><article><p class="bc-kind">{e(p["kind"])}</p>'
            f'<h5><a href="{e(p["url"], quote=True)}">{e(p["name"])}</a></h5>'
            f'<p class="bc-project-description">{e(p["summary"])}</p>'
            f'<details class="bc-evidence"><summary>Methods &amp; evidence<span class="bc-sr-only"> for {e(p["name"])}</span></summary>'
            f'<div><p class="bc-methods">{e(p["methods"])}</p><p>{e(p["scope"])}</p>'
            f'<p class="bc-limit">{e(p["limit"])}</p></div></details></article></li>')


def render_explorer():
    total = sum(len(g['projects']) for d in DOMAINS for g in d['groups'])
    html = (f'<section class="business-explorer bc-{THEME}" id="{SECTION_ID}" aria-labelledby="bc-heading"><div class="bc-inner">'
            f'<header class="bc-header"><h2 id="bc-heading">{e(HEADING)}</h2><div><p>{e(INTRO)}</p>'
            f'<p class="bc-total">{total} case studies across {len(DOMAINS)} business contexts</p></div></header>'
            '<div class="bc-choices" role="tablist" aria-label="Choose a business context" hidden>')
    for i, d in enumerate(DOMAINS):
        count = sum(len(g['projects']) for g in d['groups'])
        html += (f'<button type="button" id="bc-tab-{d["key"]}" role="tab" aria-controls="bc-panel-{d["key"]}" '
                 f'aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}">{icon(d["icon"])}'
                 f'<span><strong>{e(d["name"])}</strong><small>{count} {"case" if count == 1 else "cases"}</small></span></button>')
    html += '</div>'
    for d in DOMAINS:
        html += (f'<div class="bc-panel" id="bc-panel-{d["key"]}" role="tabpanel" aria-labelledby="bc-tab-{d["key"]}" tabindex="0">'
                 f'<div class="bc-overview"><div class="bc-insight"><p class="bc-basis">{e(d["angle"])}</p>'
                 f'<h3>{e(d["title"])}</h3><p class="bc-why">{e(d["why"])}</p></div>'
                 f'<aside class="bc-decision"><span>Business decision</span><p>{e(d["decision"])}</p></aside></div>')
        for i, g in enumerate(d['groups']):
            heading_id = f'bc-{d["key"]}-group-{i}'
            html += (f'<section class="bc-project-group" aria-labelledby="{heading_id}"><header class="bc-group-heading">'
                     f'<h4 id="{heading_id}">{e(g["title"])}</h4><p>{e(g["intro"])}</p></header>'
                     f'<ol class="bc-projects bc-count-{len(g["projects"])}">')
            for j, project in enumerate(g['projects']):
                html += render_project(project, featured=i == 0 and j == 0)
            html += '</ol></section>'
        html += (f'<aside class="bc-foundation"><div>{icon(d["icon"])}</div><div><h4>{e(d["context_title"])}</h4><p>{e(d["context"])}</p>')
        if d.get('context_url'):
            html += f'<a href="{e(d["context_url"], quote=True)}">View company experience</a>'
        html += '</div></aside></div>'
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
