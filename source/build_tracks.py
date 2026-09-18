"""Build either public portfolio. Existing private routes/assets are left intact.

Usage: python source/build_tracks.py --track marketing --root .
All required images and PDFs live in website/assets/revamp and website/documents.
"""
import argparse, json, shutil
from pathlib import Path
from html import escape as e
from revamp_content import PROFILE as P, TRACKS, CASES, EXPERIENCE, SKILLS, EDUCATION

def case_path(key, track):
    return ('/projects/' if track=='data' else '/work/')+CASES[key][track+'_slug']+'/'

def library_path(track): return '/projects.html' if track=='data' else '/work/'
def cv_path(track): return '/documents/'+TRACKS[track]['cv']+'.pdf'
def tags(items): return '<div class="method-tags">'+''.join('<span>'+e(x)+'</span>' for x in items)+'</div>'
def button(label,url,secondary=False):return f'<a class="button{" secondary" if secondary else ""}" href="{e(url)}">{e(label)}</a>'

def shell(title,desc,body,track,path='/'):
    t=TRACKS[track]; alternate='marketing' if track=='data' else 'data'
    nav=f'<a href="{library_path(track)}">Case studies</a><a href="/#domains">'+('Domains' if track=='data' else 'Capabilities')+'</a><a href="/#experience">Experience</a><a href="/#contact">Contact</a>'+f'<a class="cv-nav" href="{cv_path(track)}">Download CV</a>'
    schema={'@context':'https://schema.org','@type':'ProfilePage','mainEntity':{'@type':'Person','name':P['name'],'url':t['site'],'sameAs':[P['linkedin'],P['github']]}}
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)} | Phan Hoai Thu</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{t['site']+path}"><meta property="og:title" content="{e(title)} | Phan Hoai Thu"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{t['site']+path}"><meta property="og:type" content="website"><meta property="og:image" content="{t['site']}/assets/revamp/share-{track}.png"><meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#15324b"><link rel="icon" href="/assets/revamp/favicon.svg"><link rel="stylesheet" href="/assets/revamp/revamp.css"><script src="/assets/revamp/revamp.js" defer></script><script type="application/ld+json">{json.dumps(schema)}</script></head><body class="{track}"><a class="skip" href="#main">Skip to content</a><header class="header"><div class="wrap header-inner"><a class="brand" href="/" aria-label="Phan Hoai Thu home"><span class="monogram">KAThu</span><span class="brand-sub">Phan Hoai Thu<br>{'Data & BI' if track=='data' else 'Marketing analytics'}</span></a><button class="menu-button" aria-expanded="false" aria-controls="site-nav">Menu</button><nav id="site-nav" class="nav" aria-label="Main navigation">{nav}</nav></div></header><main id="main">{body}</main><footer class="footer"><div class="wrap footer-inner"><div>Phan Hoai Thu · {e(t['role'])}<br>Ho Chi Minh City, Vietnam</div><div><a href="{P['linkedin']}">LinkedIn</a> &nbsp; <a href="{P['github']}">GitHub</a> &nbsp; <a href="{TRACKS[alternate]['site']}">View {'marketing' if alternate=='marketing' else 'data / BI'} portfolio</a></div></div></footer></body></html>'''

def card(key,track):
    c=CASES[key]; path=case_path(key,track)
    metric,label=('58.0%','cart abandonment in synthetic retail data') if track=='marketing' and key=='thelook' else (c['metric'],c['metric_label'])
    cats='|'.join([c['domain'],c['capability']]+(['Growth and retention'] if key=='mobility' else []))
    return f'''<article class="project-card" data-categories="{e(cats)}"><div class="card-top"><span class="card-domain">{e(c['domain'] if track=='data' else c['capability'])}</span><h3><a href="{path}">{e(c['name'])}</a></h3><p>{e(c[track+'_intro'])}</p><p class="card-result"><strong>{e(metric)}</strong><span>{e(label)}</span></p></div><div class="card-bottom"><p class="card-tools">{e(' / '.join(c['tools']))}</p><a class="text-link" href="{path}">Read the {'public summary' if key=='mobility' else 'case study'}</a></div></article>'''

def domain_sections(track):
    if track=='data':
      bands=[('Ecommerce','Commercial reporting, customer journeys and marketplace decisions.',
        'Operational context','Canawan brings Etsy/Amazon and dropshipping knowledge; Laptop SGN adds retail acquisition, merchandising and customer analysis.',
        ['thelook','mobility'],['ELT and data modeling','Funnel and cohort retention','Marketplace economics']),
       ('Bank and fintech','Customer propensity and cost-aware risk review, demonstrated through independent projects.',
        'Project-based domain experience','Bank Marketing supports outreach prioritization. ZaloPay connects behavioral signals with manual-review workload and promotion-cost exposure. These are independent studies, not banking employment.',
        ['bank','zalopay'],['PR-AUC and targeting lift','Leakage controls','Rule-based review']),
       ('SaaS and technology','Agency experience with software clients, supported by disciplined marketing measurement.',
        'Professional context','At Golden Owl, I connected client website, campaign and lead data with acquisition and funnel decisions. The Rokt study demonstrates a transferable experimentation method; it is not a subscription analytics project.',
        ['rokt'],['GA4 and Looker Studio','Product-intent funnels','Experiment sensitivity'])]
    else:
      bands=[('Acquisition and channel measurement','Look past traffic volume to activation, lead quality and commercial value.',
        'Professional context','Golden Owl campaign work combined audience planning, channel reporting and geographic lead-quality analysis. The marketplace case extends that approach to acquisition and downstream value.',
        ['mobility'],['Channel efficiency','CAC and CIR','Measurement guardrails']),
       ('Campaign targeting and promotion efficiency','Decide who to contact and where promotion review deserves attention.',
        'Decision focus','Connect campaign capacity with historical response capture, then compare promotion-cost coverage with review workload. Validate outcomes before applying a live policy.',
        ['bank','zalopay'],['Propensity targeting','Offline lift','Promotion-cost review']),
       ('Growth and retention','Connect acquisition with the customer journey after the first visit.',
        'Professional context','Laptop SGN contributes retail funnel and returning-customer analysis. Golden Owl SaaS client work connects content to signup or download intent; independent cases add cohort and subsidy analysis.',
        ['thelook','mobility'],['Funnel diagnosis','Cohort retention','Lifecycle hypotheses']),
       ('Experimentation','Make the causal question and the quality of assignment explicit.',
        'Analytical evidence','The Rokt ad-holdout study compares treatment with control, audits repeat-user assignment and checks how the result changes under alternative counting units.',
        ['rokt'],['Ad incrementality','Confidence intervals','Sensitivity analysis'])]
    return ''.join(f'<article class="domain-band"><div><h3>{e(title)}</h3><p>{e(intro)}</p>{tags(methods)}</div><div class="domain-evidence"><strong>{e(label)}</strong><p>{e(text)}</p><div class="case-links">'+''.join(f'<a href="{case_path(k,track)}">{e(CASES[k]["name"])}</a>' for k in keys)+'</div></div></article>' for title,intro,label,text,keys,methods in bands)

def experience(track):
    jobs=EXPERIENCE if track=='marketing' else [EXPERIENCE[1],EXPERIENCE[0],EXPERIENCE[2]]
    out=''
    for j in jobs:
      out+=f'<article id="{j["id"]}" class="job"><div><h3>{e(j["company"])}</h3><p class="job-meta">{e(j["role"])}<br>{e(j["dates"])}<br>{e(j["domain"])}</p></div><div class="job-body"><p>{e(j["intro"])}</p><ul>'+''.join('<li>'+e(v)+'</li>' for v in j[track])+'</ul><details class="experience-details"><summary>More about my contribution</summary>'+''.join('<p><strong>'+e(a)+':</strong> '+e(b)+'</p>' for a,b in j['web'])+'</details></div></article>'
    return out

def home(track):
    t=TRACKS[track]
    title='<h1 class="data-role">Data Analyst / BI Analyst</h1><p class="rotator" data-rotate>Reproducible pipelines and trusted BI</p>' if track=='data' else '<h1>Marketing decisions, backed by evidence.</h1>'
    body=f'''<div class="wrap"><section class="hero"><div><p class="byline">Phan Hoai Thu · {e(t['role']) if track=='marketing' else 'Ecommerce, fintech and SaaS'}</p>{title}<p class="hero-voice">{e(P['voice'])}</p><p class="lede">{e(t['lede'])}</p><div class="actions">{button('Explore selected work','#work')}{button('Download '+('Data / BI' if track=='data' else 'Marketing')+' CV',cv_path(track),True)}</div><p class="hero-meta">3+ years in ecommerce and digital marketing · Ho Chi Minh City<br>Open to Vietnam / SEA and remote opportunities</p></div><figure class="portrait"><img src="/assets/revamp/portrait-{'data' if track=='data' else 'marketing'}.webp" width="720" height="860" alt="Phan Hoai Thu" fetchpriority="high"><figcaption>Business context, clear methods and decisions you can explain.</figcaption></figure></section></div>
<section id="work" class="section tinted"><div class="wrap"><div class="section-head"><div><h2>{'Selected analytical work' if track=='data' else 'Selected marketing analysis'}</h2><p>{'Reproducible systems, explicit methods and results with their limits attached.' if track=='data' else 'Who to reach, where growth breaks down and whether the ads worked.'}</p></div><a href="{library_path(track)}">Explore all 5 case studies</a></div><div class="card-grid featured-grid">{''.join(card(k,track) for k in t['featured'])}</div><p class="ownership">All five case studies were completed independently, from question and data preparation to analysis, reporting and recommendations. Professional experience is shown separately below.</p></div></section>
<section id="domains" class="section"><div class="wrap"><div class="section-head"><div><h2>{'Three domains, connected by business questions' if track=='data' else 'Marketing capabilities with evidence behind them'}</h2><p>{'Professional context and independent project evidence, clearly distinguished.' if track=='data' else 'Campaign experience gives the analysis context. Data helps decide what to do next.'}</p></div></div>{domain_sections(track)}</div></section>
<section id="experience" class="section tinted"><div class="wrap"><div class="section-head"><div><h2>Professional experience</h2><p>I led project planning, translated goals into KPIs, guided contributors and owned progress against the agreed targets.</p></div></div><div class="experience-list">{experience(track)}</div><p class="ownership">Power BI is demonstrated in independent projects. Golden Owl reporting used GA4 and Looker Studio.</p></div></section>
<section id="about" class="section"><div class="wrap about-grid"><div><h2>How I approach the work</h2><p>I start with the decision and its constraints, then define the metric and validate the data behind it. A useful recommendation explains what the evidence supports and what needs another test.</p><p>My professional background is in ecommerce operations, digital marketing and software-agency client work. My fintech experience comes from independent project analysis.</p><div class="education">{''.join('<p>'+e(v)+'</p>' for v in EDUCATION)}</div></div><dl class="skill-list">{''.join('<div><dt>'+e(a)+'</dt><dd>'+e(b)+'</dd></div>' for a,b in SKILLS[track])}</dl></div></section>
<section id="contact" class="section tinted"><div class="wrap contact-panel"><div><h2>Let’s discuss the decision behind the role.</h2><p>{e(P['email'])}<br>{e(P['phone'])} · {e(P['location'])}</p></div><div class="actions">{button('Email Thu','mailto:'+P['email'])}{button('Download CV',cv_path(track),True)}</div></div></section>'''
    if track=='marketing':
      preview='<section class="experience-preview"><div class="wrap"><p><strong>Campaign experience at Golden Owl Solutions</strong><br>Paid acquisition, SEO and conversion work, supported by GA4 and Looker Studio. 70+ analyses across 15 client businesses.</p><a href="/#golden-owl">Explore my contribution</a></div></section>'
      body=body.replace('<section id="work"',preview+'<section id="work"',1)
    return shell(t['role']+' portfolio',t['summary'],body,track)

def library(track):
    t=TRACKS[track]; filters=['All','Ecommerce','Bank and fintech','Experimentation'] if track=='data' else ['All','Acquisition and measurement','Campaign targeting','Growth and retention','Experimentation','Promotion efficiency']
    body=f'<section class="section"><div class="wrap"><div class="page-intro"><h1>Completed case studies</h1><p>Five independent projects. Each starts with a business decision and keeps the method, evidence and limitations visible.</p></div><div class="filters" role="group" aria-label="Filter case studies">'+''.join(f'<button class="filter" data-filter="{e(v)}" aria-pressed="{str(i==0).lower()}">{e(v)}</button>' for i,v in enumerate(filters))+'</div><p class="result-count" role="status" aria-live="polite">5 completed case studies</p><div class="card-grid">'+''.join(card(k,track) for k in t['order'])+'</div><p class="ownership">Sole contributor on each project. Approximate durations are shown within each case. Fintech cases represent project experience; professional experience is in ecommerce and marketing.</p></div></section>'
    return shell('Completed case studies',t['summary'],body,track,library_path(track))

def architecture():
    steps=[('7 source files','Users, orders, items, products, events, inventory and distribution centers'),('Raw and staging','Source-preserving ingestion, safe types and event-derived sessions'),('Core model','Conformed dimensions and facts at explicit grains'),('Decision marts','Funnel, commercial, customer and operations views'),('Power BI','Validated exports and a seven-page report')]
    return '<figure class="architecture"><figcaption>From source evidence to business reporting</figcaption><ol class="pipeline">'+''.join('<li><b>'+e(a)+'</b>'+e(b)+'</li>' for a,b in steps)+'</ol><p class="pipeline-note">Validation spans every layer: source counts, session lineage, key/grain checks and KPI reconciliation. Python supports repeatable builds and advanced analysis.</p></figure>'

def case_page(key,track):
    c=CASES[key]; t=TRACKS[track]
    evidence='<div class="evidence-grid'+(' qualitative' if key=='mobility' else '')+'">'+''.join('<div class="evidence-stat"><strong>'+e(a)+'</strong><span>'+e(b)+'</span></div>' for a,b in c['results'])+'</div>'
    image=''
    if c['image']:
      image=f'<figure class="case-figure"><a href="/assets/revamp/{c["image"]}" aria-label="Open {e(c["name"])} evidence image at full size"><img src="/assets/revamp/{c["image"]}" loading="lazy" alt="{e(c["chart_caption"])}"></a><figcaption>{e(c["chart_caption"])} Select the image for a larger view.</figcaption></figure>'
    links=button('Code and methodology',c['repo']) if c['repo'] else button('Open detailed case with password','https://kathuatwork.com/private/mobility/')+button('Request access','mailto:'+P['email'],True)
    body=f'''<div class="wrap"><header class="case-hero"><a class="back" href="{library_path(track)}">Back to case studies</a><p class="byline">{e(c['domain'] if track=='data' else c['capability'])} · {e(c['name'])}</p><h1>{e(c[track+'_title'])}</h1><p class="case-intro">{e(c[track+'_intro'])}</p><div class="case-meta"><span><strong>My role</strong><br>Independent analyst; sole contributor</span><span><strong>Duration</strong><br>{e(c['duration'])}</span><span><strong>Context</strong><br>{e(c['provenance'])}</span></div>{tags(c['tools'])}</header><nav class="case-nav" aria-label="On this page"><a href="#decision">Business decision</a><a href="#method">Method</a><a href="#evidence">Results</a><a href="#limits">Limits</a><a href="#review">Review the work</a></nav><div class="case-main"><section id="decision" class="case-section"><h2>The decision</h2><p>{e(c['problem'])}</p><p class="scope-note"><strong>My contribution:</strong> I framed the question, prepared and validated the data, performed the analysis, built the reporting output and wrote the recommendations.</p></section><section id="method" class="case-section"><h2>How I approached it</h2><div class="case-methods">{''.join('<article><h3>'+e(a)+'</h3><p>'+e(b)+'</p></article>' for a,b in c['methods'])}</div>{architecture() if key=='thelook' else ''}</section><section id="evidence" class="case-section"><h2>{'What the analysis supports' if key=='mobility' else 'Results and interpretation'}</h2>{evidence}<p>{e(c['findings'])}</p>{image}</section><section class="case-section"><h2>What I recommended</h2><p>{e(c['decision'])}</p></section><section id="limits" class="case-section"><div class="limits"><h2>What the evidence does not establish</h2><p>{e(c['limits'])}</p></div></section><section id="review" class="case-section"><h2>Review the work</h2><div class="actions">{links}</div><p class="source-note">{e(c['source_note'])}</p></section><div class="related"><a href="{library_path(track)}">Browse the other case studies</a><a href="{cv_path(track)}">Download the {e(t['role'])} CV</a></div></div></div>'''
    return shell(c[track+'_title'],c[track+'_intro'],body,track,case_path(key,track))

def redirect(target,title='This page has moved'):
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url={e(target)}"><title>{e(title)}</title></head><body><p><a href="{e(target)}">Continue to the updated portfolio</a></p></body></html>'

def build(track,root):
    root=Path(root); site=root/'website'; site.mkdir(parents=True,exist_ok=True)
    asset=site/'assets'/'revamp';asset.mkdir(parents=True,exist_ok=True)
    for name in ['revamp.css','revamp.js']:shutil.copy2(Path(__file__).parent/name,asset/name)
    pages={'/':home(track),library_path(track):library(track)}
    pages.update({case_path(k,track):case_page(k,track) for k in TRACKS[track]['order']})
    for path,html in pages.items():
      file=site/('index.html' if path=='/' else path.lstrip('/')+('index.html' if path.endswith('/') else ''))
      file.parent.mkdir(parents=True,exist_ok=True);file.write_text(html,encoding='utf-8')
    legacy={}
    if track=='data':
      legacy={x+'.html':'/#'+anchor for x,anchor in [('about','about'),('experience','experience'),('expertise','domains'),('contact','contact')]}
      legacy['projects/be-group/index.html']=case_path('mobility',track)
      for slug in ['laptop-sgn','turis-vpn','leaserunner','gos-cro','gos-conversion-dashboard']:
        legacy[f'projects/marketing-analytics/{slug}/index.html']='/#'+('laptop-sgn' if slug=='laptop-sgn' else 'golden-owl')
      legacy['projects/marketing-analytics/index.html']='/#experience'
    else:
      for slug in ['golden-owl','the-lab','leaserunner','turisvpn','conversion-optimization','lead-quality']:
        legacy[f'work/{slug}/index.html']='/#golden-owl'
      legacy['work/laptop-sgn/index.html']='/#laptop-sgn'
      legacy['work/glassdoor/index.html']=library_path(track)
    for path,target in legacy.items():
      file=site/path;file.parent.mkdir(parents=True,exist_ok=True);file.write_text(redirect(target),encoding='utf-8')
    body='<section class="section"><div class="wrap"><h1>Page not found</h1><p>The case may have moved. Explore the updated project collection.</p><div class="actions">'+button('Browse case studies',library_path(track))+'</div></div></section>'
    (site/'404.html').write_text(shell('Page not found','Find the updated portfolio work.',body,track,'/404.html').replace('<meta name="description"','<meta name="robots" content="noindex"><meta name="description"'),encoding='utf-8')
    (site/'robots.txt').write_text('User-agent: *\nAllow: /\nDisallow: /private/\nDisallow: /portfolio-login\nSitemap: '+TRACKS[track]['site']+'/sitemap.xml\n')
    (site/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+TRACKS[track]['site']+p+'</loc></url>' for p in pages)+'</urlset>',encoding='utf-8')
    print(f'{track}: {len(pages)} public pages, {len(legacy)} preserved legacy routes')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--track',choices=TRACKS,required=True);parser.add_argument('--root',type=Path,required=True)
    args=parser.parse_args();build(args.track,args.root)
