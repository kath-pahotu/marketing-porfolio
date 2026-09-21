"""Visual, progressively enhanced workflow, evidence and capability sections."""
from pathlib import Path
from html import escape as e
import hashlib
import os
import shutil
from bs4 import BeautifulSoup

ROOT = Path(os.environ.get('MARKETING_OUTPUT_DIR', Path(__file__).resolve().parent.parent))
SITE = ROOT / 'website'


def icon(key):
    paths = {
        'goal': '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3"/><path d="m14 10 7-7M17 3h4v4"/>',
        'plan': '<path d="M5 4h14v17H5zM9 2h6v4H9zM8 10h8M8 14h5M8 18h7"/>',
        'team': '<circle cx="12" cy="7" r="3"/><path d="M6 21v-3a6 6 0 0 1 12 0v3M4 5a3 3 0 0 0 0 6m16-6a3 3 0 0 1 0 6M2 20v-3a5 5 0 0 1 3-4m17 7v-3a5 5 0 0 0-3-4"/>',
        'learn': '<path d="M4 4v16h17M8 16v-4m5 4V8m5 8V5"/>',
        'acquire': '<path d="m3 10 16-6v16L3 14zM7 15l2 6h4l-2-5M21 9v6"/>',
        'convert': '<path d="M3 4h18l-7 9v7l-4-2v-5z"/>',
        'understand': '<circle cx="10" cy="10" r="6"/><path d="m15 15 6 6M7 11l2-3 2 4 2-3"/>',
        'deliver': '<path d="M4 6h16v15H4zM8 3v6m8-6v6M8 15l3 3 5-6"/>',
        'repeat': '<path d="M20 8a8 8 0 0 0-14-3L3 8m0-5v5h5M4 16a8 8 0 0 0 14 3l3-3m0 5v-5h-5"/>',
        'cost': '<circle cx="12" cy="12" r="9"/><path d="M15 8h-4a2 2 0 0 0 0 4h2a2 2 0 0 1 0 4H9m3-10v12"/>',
    }
    return f'<svg class="mx-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[key]}</svg>'


def case_link(slug, label):
    return f'<a class="mx-case-link" href="/work/{slug}/">{e(label)}</a>'


WORKFLOW = [
    dict(key='goal', label='Frame the goal', short='Business goal → clear brief', title='Make the goal usable.',
         body='I turn the objective from management into a clear audience, project KPIs and smaller milestones the team can act on.',
         actions=['Define the audience and the action we want them to take.', 'Agree the measures and milestones before assigning work.'],
         output='A campaign brief', nodes=[('Business goal', 'What needs to change?'), ('Audience & offer', 'Who needs it, and why?'), ('KPI & milestone', 'What will progress look like?')],
         proof=[('the-lab', 'The Lab: audience and seasonal planning'), ('golden-owl', 'Golden Owl: service-led demand')]),
    dict(key='plan', label='Build the plan', short='Message → channel → next step', title='Connect every part of the journey.',
         body='I connect the message, channel, content and landing page, then allocate resources around the work that needs to happen.',
         actions=['Match search intent and audience needs to the offer.', 'Plan media, content and website work as one connected path.'],
         output='A connected campaign plan', nodes=[('Message', 'A relevant reason to care'), ('Channel & content', 'The right place to reach them'), ('Landing page', 'A clear next action')],
         proof=[('golden-owl', 'Golden Owl: channels and landing pages'), ('leaserunner', 'LeaseRunner: content-to-signup paths')]),
    dict(key='team', label='Guide delivery', short='Owners → milestones → feedback', title='Give the team clarity to deliver.',
         body='I assign work, coach contributors and coordinate with content, design, developers and sales. I stay accountable for project KPI progress.',
         actions=['Break the plan into owners, smaller goals and delivery milestones.', 'Guide the team, review the work and resolve handoff gaps.'],
         output='A shared delivery structure', nodes=[('Allocate', 'People and resources'), ('Guide', 'Training and review'), ('Coordinate', 'Feedback and handoffs')],
         proof=[('golden-owl', 'Golden Owl: campaign and CMS coordination'), ('turisvpn', 'TurisVPN: multilingual content delivery')]),
    dict(key='learn', label='Learn & adjust', short='Evidence → decision → next cycle', title='Bring the result into the next plan.',
         body='I review tracking, spend, conversion and lead quality with the business goal in view, then turn the evidence into a practical next step.',
         actions=['Check KPI progress alongside lead quality and customer behaviour.', 'Recommend what to improve, test or prioritize in the next cycle.'],
         output='A decision and feedback loop', nodes=[('Measure', 'Tracking and KPI progress'), ('Interpret', 'Customer and sales context'), ('Adjust', 'The next campaign priority')],
         proof=[('lead-quality', 'Golden Owl: marketing–sales feedback'), ('the-lab', 'The Lab: platform-level campaign review')]),
]

ANALYSIS = [
    dict(key='retail', icon='convert', label='Fix the funnel', client='Laptop SGN', provenance='Professional retail analysis',
         title='Where does traffic stop converting?',
         insight='The weak point appeared before checkout. Product-page and cart decisions deserved a closer look.',
         decision='Improve product and cart decision support, then test changes by device and customer segment.',
         limit='Observed rates from 8 Aug–7 Sep. Each rate uses the preceding stage as its denominator; recommendations are not measured uplift.', slug='laptop-sgn'),
    dict(key='bank', icon='goal', label='Prioritize outreach', client='Bank marketing', provenance='Independent targeting study',
         title='Who should a limited campaign reach first?',
         insight='Ranking contacts concentrated historical responders into a smaller audience for a potential pilot.',
         decision='Pilot the prioritized audience against existing targeting, measuring conversions, cost and customer impact.',
         limit='Untouched historical test set. Predictive lift is not causal campaign lift, and the contact reduction was not implemented.', slug='campaign-targeting'),
    dict(key='promo', icon='cost', label='Review promotion cost', client='ZaloPay study', provenance='Independent promotion analysis',
         title='Where does promotion cost concentrate?',
         insight='A small share of scored users was associated with a much larger share of credited promotion cost.',
         decision='Start with manual review, collect outcomes and check customer harm before automating any action.',
         limit='Both shares describe the same score-based group. Flags are review signals, not confirmed fraud or recovered savings.', slug='promotion-review'),
    dict(key='mobility', icon='repeat', label='Grow repeat use', client='Mobility & delivery', provenance='Independent confidential case · Public summary',
         title='Is growth supported by repeat use?',
         insight='Partner scale, customer return and subsidy intensity need to be read together to assess growth.',
         decision='Test targeted incentives with a holdout and evaluate activated, retained users alongside cost.',
         limit='This public view is qualitative and sanitized. Proposed tests and forecasts are not realized results.', slug='growth-and-retention'),
    dict(key='lifecycle', icon='team', label='Plan lifecycle offers', client='TheLook ecommerce', provenance='Independent study · Synthetic data',
         title='What follows the first purchase?',
         insight='Customer groups turn a broad retention question into distinct priorities for relationship-building and reactivation.',
         decision='Design different treatments for valuable repeat, developing and lapsed customers; evaluate tests against net value.',
         limit='Synthetic-data analysis, not client campaign results. The study does not establish ROAS or causal uplift.', slug='thelook'),
    dict(key='experiment', icon='learn', label='Test advertising value', client='Rokt holdout', provenance='Independent experiment analysis',
         title='Did the advertising add conversions?',
         insight='Two analysis views pointed to a positive effect, but the estimated size changed with the comparison.',
         decision='Confirm the randomization unit and identity overlap before sizing a rollout.',
         limit='Analysis of a supplied dataset, not a campaign I operated. Assignment ambiguity remains unresolved.', slug='rokt'),
]

CAPABILITIES = [
    dict(key='acquire', label='Acquire', tagline='Bring the right people in', title='Build demand around a relevant offer.',
         body='I connect audience and keyword research with paid campaigns, search visibility and useful content.',
         tools=['Google Ads', 'Meta Ads', 'SEO', 'Audience research', 'Content planning'],
         scope='Professional campaign and organic-growth work.', proof=[('the-lab', 'The Lab: paid acquisition'), ('turisvpn', 'TurisVPN: organic growth')]),
    dict(key='convert', label='Convert', tagline='Make the next step clearer', title='Carry interest through to action.',
         body='I connect landing-page strategy, customer journeys and sales feedback so acquisition has somewhere useful to lead.',
         tools=['Landing-page strategy', 'CRO', 'Creative testing', 'Lead quality'],
         scope='Professional website and marketing–sales work.', proof=[('conversion-optimization', 'Golden Owl: conversion'), ('leaserunner', 'LeaseRunner: signup journey')]),
    dict(key='understand', label='Understand', tagline='Give decisions a sound basis', title='Read the customer behind the metric.',
         body='I use tracking, reporting, SQL and customer segmentation to make channel and journey decisions more specific.',
         tools=['GA4 & GTM', 'Looker Studio', 'Excel', 'SQL', 'Segmentation'],
         scope='Power BI and Python extend this toolkit in independent projects. Golden Owl reporting used GA4 and Looker Studio.',
         proof=[('laptop-sgn', 'Laptop SGN: retail behaviour'), ('lead-quality', 'Golden Owl: lead insight')]),
    dict(key='deliver', label='Deliver', tagline='Turn the plan into team action', title='Own the plan and guide the work.',
         body='I turn management goals into project KPIs, allocate resources, train contributors and coordinate delivery across the team.',
         tools=['KPI planning', 'Team coaching', 'Resource allocation', 'CMS workflows', 'Cross-functional coordination'],
         scope='Project leadership and KPI accountability across professional work.',
         proof=[('golden-owl', 'Golden Owl: project delivery'), ('turisvpn', 'TurisVPN: content programme')]),
]


def controls(group, items, label):
    buttons = []
    for i, d in enumerate(items):
        detail = d.get('short', d.get('client', d.get('tagline')))
        buttons.append(f'<button type="button" role="tab" id="mx-{group}-tab-{d["key"]}" aria-controls="mx-{group}-{d["key"]}" aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}">{icon(d.get("icon", d["key"]))}<span><strong>{e(d["label"])}</strong><small>{e(detail)}</small></span></button>')
    return f'<div class="mx-controls mx-controls--{group}" role="tablist" aria-label="{label}" data-mx-controls hidden>'+''.join(buttons)+'</div>'


def panel_open(group, d):
    return f'<div class="mx-panel" id="mx-{group}-{d["key"]}" role="tabpanel" aria-labelledby="mx-{group}-tab-{d["key"]}" tabindex="0" data-mx-panel>'


def render_workflow():
    content = '''<section class="mx-section mx-workflow" id="approach" aria-labelledby="mx-workflow-heading"><div class="wrap" data-mx-explorer><header class="mx-heading"><div><p class="mx-kicker">How I work</p><h2 id="mx-workflow-heading">A clear plan.<br>Shared ownership.<br>Continuous learning.</h2></div><p>I lead the work from the business goal to the next decision. Explore each stage to see what I own and what the team works from.</p></header>'''
    content += controls('workflow', WORKFLOW, 'Campaign delivery stages')
    for i, d in enumerate(WORKFLOW):
        content += panel_open('workflow', d)+f'<div class="mx-work-sheet"><div class="mx-work-copy"><span class="mx-stage-label">Stage {i+1} of 4</span><h3>{e(d["title"])}</h3><p>{e(d["body"])}</p><ul class="mx-actions">'+''.join(f'<li>{e(a)}</li>' for a in d['actions'])+'</ul></div>'
        content += f'<div class="mx-work-output"><p class="mx-output-label">{e(d["output"])}</p><ol class="mx-deliverable">'+''.join(f'<li><strong>{e(title)}</strong><span>{e(desc)}</span></li>' for title, desc in d['nodes'])+'</ol></div>'
        content += '<div class="mx-proof"><span>In practice</span>'+''.join(case_link(*p) for p in d['proof'])+'</div></div></div>'
    return content+'</div></section>'


def bars(rows):
    return '<div class="mx-bars">'+''.join(f'<div class="mx-bar-row"><div><span>{e(label)}</span><strong>{value}%</strong></div><div class="mx-bar-track" aria-hidden="true"><i style="width:{value}%"></i></div></div>' for label, value in rows)+'</div>'


def analysis_visual(key):
    if key == 'retail':
        return '<figure class="mx-evidence-figure"><figcaption>Conversion between funnel stages</figcaption>'+bars([('Product page → cart', 21.46), ('Cart → checkout', 27.47), ('Checkout → purchase', 63.46)])+'</figure>'
    if key == 'bank':
        return '<figure class="mx-evidence-figure"><figcaption>Historical targeting concentration</figcaption>'+bars([('Share of contacts prioritized', 20), ('Share of responders captured', 51.8)])+'<p class="mx-figure-note">Top-ranked contacts in the untouched test set.</p></figure>'
    if key == 'promo':
        return '<figure class="mx-evidence-figure"><figcaption>One group, two shares</figcaption>'+bars([('Share of scored users', 4.26), ('Share of credited promotion cost', 26.94)])+'<p class="mx-figure-note">Concentration directs a review; it does not confirm abuse.</p></figure>'
    if key == 'mobility':
        return '<figure class="mx-evidence-figure"><figcaption>Three checks on the quality of growth</figcaption><div class="mx-growth-map">'+''.join(f'<div>{icon(i)}<strong>{t}</strong><span>{d}</span></div>' for i, t, d in [('acquire','Acquire','Activation after install'),('repeat','Retain','Return and transact'),('cost','Sustain','Subsidy and value')])+'</div><p class="mx-figure-note">Read all three together before increasing spend.</p></figure>'
    if key == 'lifecycle':
        return '<figure class="mx-evidence-figure"><figcaption>Different relationships, different priorities</figcaption><div class="mx-lifecycle">'+''.join(f'<div><span>{e(a)}</span><strong>{e(b)}</strong></div>' for a, b in [('New / developing','Build the next habit'),('Champions','Nurture repeat value'),('Hibernating','Test reactivation')])+'</div><p class="mx-figure-note">Proposed lifecycle priorities, illustrated with synthetic data.</p></figure>'
    return '''<figure class="mx-evidence-figure"><figcaption>How the estimate changes with the analysis</figcaption><div class="mx-estimates"><div><span>Primary comparison</span><strong>+13.9%</strong><small>Relative uplift estimate<br>95% interval: +9.1% to +19.0%</small></div><div><span>User-cohort sensitivity</span><strong>+5.5%</strong><small>Relative uplift estimate<br>Different comparison grain</small></div></div><p class="mx-figure-note">A positive signal; the rollout size still needs validation.</p></figure>'''


def render_analytics():
    content = '''<section class="mx-section mx-analysis" id="analytics" aria-labelledby="mx-analysis-heading"><div class="wrap" data-mx-explorer><header class="mx-heading"><div><p class="mx-kicker">Analytics that supports marketing</p><h2 id="mx-analysis-heading">A marketing question.<br>A useful next move.</h2></div><p>One professional retail analysis and five independent studies. Choose a question to see the evidence and the decision it supports.</p></header><div class="mx-analysis-layout">'''
    content += controls('analysis', ANALYSIS, 'Choose a marketing question')+'<div class="mx-analysis-content">'
    for d in ANALYSIS:
        content += panel_open('analysis', d)+f'<p class="mx-provenance">{e(d["client"])}<span>{e(d["provenance"])}</span></p><h3>{e(d["title"])}</h3><p class="mx-insight">{e(d["insight"])}</p>'+analysis_visual(d['key'])
        content += f'<div class="mx-next-move"><strong>The next marketing move</strong><p>{e(d["decision"])}</p></div><p class="mx-limit">{e(d["limit"])}</p>'+case_link(d['slug'], f'Read the {d["client"]} case')+'</div>'
    return content+'</div></div><div class="mx-analysis-footer"><p>Want to see the methods, models and technical detail?</p><a class="button secondary" href="https://kathuatwork.com/">Explore my Data / BI portfolio</a></div></div></section>'


def render_about():
    content = '''<section class="mx-section mx-about" id="about" aria-labelledby="mx-about-heading"><div class="wrap"><div class="mx-about-layout"><div class="mx-about-copy"><p class="mx-kicker">A little about me</p><h2 id="mx-about-heading">Marketing leadership.<br>Analytical depth.</h2><p>I’m Thu, also known as Katherine. I turn business objectives into a plan the team can deliver, then use customer evidence to make the next decision clearer.</p><p>My commercial foundation spans SaaS client projects, B2B demand generation, Etsy and Amazon marketplace operations, and electronics retail.</p><a class="mx-case-link" href="https://www.linkedin.com/in/phanhoaithu114/">Meet me on LinkedIn</a></div><div class="mx-capabilities" data-mx-explorer><h3>What I bring to the work</h3><p class="mx-cap-intro">Explore a capability to see how I use it.</p>'''
    content += controls('capability', CAPABILITIES, 'Explore a marketing capability')
    for d in CAPABILITIES:
        content += panel_open('capability', d)+f'<h4>{e(d["title"])}</h4><p>{e(d["body"])}</p><ul class="mx-tools" aria-label="Relevant skills">'+''.join(f'<li>{e(t)}</li>' for t in d['tools'])+'</ul>'
        content += f'<p class="mx-scope">{e(d["scope"])}</p><div class="mx-cap-proof">'+''.join(case_link(*p) for p in d['proof'])+'</div></div>'
    content += '''</div></div><div class="mx-credentials" aria-label="Education and credentials"><div><strong>Business foundation</strong><p>Bachelor of Business Administration</p><span>UEH · 2018–2022</span></div><div><strong>Analytical training</strong><p>TheHau Data Analytics Mentoring Program</p><span>2025</span></div><div><strong>English proficiency</strong><p>IELTS overall 7.5</p><span>2022</span></div></div></div></section>'''
    return content


def update_home():
    path = SITE / 'index.html'
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
    for selector, render in [('#approach', render_workflow), ('#analytics', render_analytics), ('#about', render_about)]:
        current = soup.select_one(selector)
        if current is None:
            raise RuntimeError(f'Missing section {selector}; refusing a partial update')
        current.replace_with(BeautifulSoup(render(), 'html.parser'))
    for filename, tag, attr in [('section-experiences.css', 'link', 'href'), ('section-experiences.js', 'script', 'src')]:
        source = ROOT / 'source' / filename
        shutil.copy2(source, SITE / filename)
        for old in soup.select(f'{tag}[{attr}^="/{filename}"]'):
            old.decompose()
        digest = hashlib.sha256(source.read_bytes()).hexdigest()[:10]
        node = soup.new_tag(tag, **{attr: f'/{filename}?v={digest}'})
        if tag == 'link':
            node['rel'] = 'stylesheet'
            soup.head.append(node)
        else:
            node['defer'] = ''
            soup.body.append(node)
    path.write_text(str(soup), encoding='utf-8')
    print('Updated workflow, supporting analytics and capabilities on the current homepage.')


if __name__ == '__main__':
    update_home()
