PROFILE = {
 'name':'Phan Hoai Thu', 'email':'phanhoaithu114@gmail.com', 'phone':'0817 375 930',
 'linkedin':'https://www.linkedin.com/in/phanhoaithu114/', 'github':'https://github.com/kath-pahotu',
 'site':'https://kathuonmkt.vercel.app', 'location':'Ho Chi Minh City, Vietnam',
 'summary':'Digital marketer with 3+ years across B2B technology, SaaS, education and e-commerce. Combines hands-on Google and Meta campaigns, SEO, conversion optimization and team leadership with GA4, SQL and BI analysis. Uses customer behavior and reliable measurement to improve acquisition, content priorities and the journey from first visit to conversion.'
}

EXPERIENCE = [
 {'company':'Laptop SGN','role':'E-commerce Analyst (Freelance)','dates':'Jul 2025 - Dec 2025',
  'bullets':[
   'Analyzed 100,000+ GA4, channel, product and transaction records using BigQuery, SQL and Excel to guide acquisition, merchandising and customer retention decisions.',
   'Identified product-to-cart conversion of 21.5% as a key funnel constraint; translated segment, device and returning-customer behavior into CRO and CRM recommendations.',
   'Standardized recurring KPI reporting, reducing preparation time by 30%; explained performance findings and recommended channel-allocation priorities.'
  ]},
 {'company':'Golden Owl Solutions','role':'Digital Marketing Analyst / Team Lead','dates':'Apr 2024 - Sep 2025',
  'bullets':[
   'Planned and optimized Google Search, Performance Max and Meta campaigns for B2B technology and education brands, aligning audiences, ad messaging, landing pages and budget pacing.',
   'Reduced Golden Owl Work-with-us campaign CPL from VND 1.6M to VND 736K; used lead quality and geographic performance to shift focus toward Singapore and Australia.',
   'Led SEO and content work as Golden Owl traffic grew from 3,000 to 30,000 monthly visits (Jun 2024 - Jun 2025); supported LeaseRunner growth from 5,600 to 27,500 visits (Dec 2024 - Jun 2025).',
   'Built TurisVPN organic visibility from zero to 45,000 monthly visits in 12 months; used download conversion by content topic to prioritize commercially relevant themes.',
   'Owned GA4/GTM tracking setup and validation; built Looker Studio reporting and delivered 70+ analyses supporting marketing decisions across 15 client businesses.',
   'Worked with developers, designers, content and sales on landing pages, CRO, CMS requirements and lead-quality reporting; coached the digital team and documented workflows.'
  ]},
 {'company':'Canawan Global','role':'Digital Marketing Executive / Team Lead','dates':'Sep 2022 - Apr 2024',
  'bullets':[
   'Led a three-person content team across affiliate and e-commerce projects, including Amazon and Etsy; planned keywords, content priorities, KPIs and reporting schedules.',
   'Conducted market and competitor research, coached on-page SEO and technical auditing, and grew organic traffic by approximately 40% to 15,000 monthly visits.',
   'Connected acquisition, product and revenue reporting across 1,000+ SKUs; automated WooCommerce workflows with n8n and Google Sheets.'
  ]}
]

CASES=[]
def case(slug,client,title,kind,category,intro,metric,metric_label,challenge,actions,findings,decision,limits,tools,images,sources):
 CASES.append(dict(slug=slug,client=client,title=title,kind=kind,category=category,intro=intro,metric=metric,metric_label=metric_label,challenge=challenge,actions=actions,findings=findings,decision=decision,limits=limits,tools=tools,images=images,sources=sources))

case('golden-owl','Golden Owl Solutions','Connecting B2B demand to qualified enquiries','Professional work','Acquisition',
 'Google and Meta campaigns, SEO, newsletter content and a better website journey for an international software outsourcing business.',
 '10×','monthly visits over 12 months',
 'Build visibility and qualified demand in a competitive B2B market with a long buying cycle. The website, paid campaigns and content needed to support the same service propositions.',
 ['Planned campaigns around Mobile Development, MVP for Startups and Healthcare App Development, matching the service and audience to Google Search or Meta.',
  'Managed campaign budgets, keyword and audience choices, UTM conventions and conversion tracking; reviewed the quality of leads alongside cost.',
  'Built an SEO roadmap around service intent, technical improvements and content clusters; partnered with content and design on newsletter and landing-page assets.',
  'Defined a clearer sitemap and CMS requirements for drafts, author roles, revisions and campaign content; coordinated implementation with developers.'],
 [('Organic growth','Monthly visits grew from 3,000 in June 2024 to 30,000 in June 2025.'),
  ('Paid efficiency','The Work-with-us campaign CPL fell from VND 1.6M to VND 736K, approximately 54%. The source review also reports a 7.06% CTR.'),
  ('Market focus','Lead-quality reviews supported reallocating spend toward Singapore and Australia, rather than relying on the total number of enquiries.'),
  ('Search visibility','The May 2025 ranking table contains 7,574 keywords in the top 100, including 228 in the top 5.')],
 'Make service-specific demand the organizing principle: align ad intent with the landing page, review qualified leads with sales, and use SEO and newsletters to support the longer buying journey.',
 'Traffic, paid campaign and ranking results cover different reporting windows. They are not one combined campaign result. Targets of 55 leads and 16 MQLs shown in the planning slide are not treated as achieved outcomes. Newsletter and CMS work have no isolated measured uplift.',
 ['Google Ads','Meta Ads','SEO','GA4','GTM','Looker Studio','CMS planning'],
 [('gos-seo.webp','SEO growth and keyword evidence from the marketing portfolio, page 11'),('cms.webp','CMS requirements and publishing workflow, page 14'),('email.webp','Newsletter designs from the marketing portfolio, page 16')],
 [('Marketing portfolio','Supplied PDF, pages 5–16'),('Company website','https://goldenowl.asia/')])

case('the-lab','The Lab Singapore','Reaching parents at the right moment','Professional work','Acquisition',
 'A paid acquisition plan for STEM and coding courses that combined search intent with audience-led discovery.',
 '≈43%','lower Meta CPL, May to June 2025',
 'Parents compare education options before committing. The campaign had to capture active searches and build consideration among parents of children aged 5–14+ in Singapore.',
 ['Organized keywords around coding classes, DSA preparation, holiday courses and extracurricular STEM learning.',
  'Used Google Search and Performance Max to capture demand, and Meta to introduce the education offer to relevant parents.',
  'Maintained a media plan, spend pacing and KPI tracker, adapting activity around the June school-holiday period.',
  'Read results by platform so changes in channel mix were not mistaken for improvements in the same campaign.'],
 [('Meta efficiency','May: SG$951.50 spend and 9 leads. June: SG$849.10 spend and 14 leads. Calculated CPL declined from SG$105.72 to SG$60.65.'),
  ('June search activity','Google Search and Performance Max generated 20 leads on combined spend of SG$1,735.47, approximately SG$86.77 per lead.'),
  ('Combined June result','The detailed table totals 34 leads on SG$2,584.57 spend, approximately SG$76.02 blended CPL.')],
 'Keep search and social roles distinct, compare platform-level lead quality, and plan budget pacing around the parent decision cycle and seasonal demand.',
 'The older summary slide reports 39 leads and SG$51 CPL, which conflicts with the detailed table. This case uses the detailed table and explicit calculations. The data establishes lead acquisition, not paid enrolment or incremental revenue.',
 ['Google Search','Performance Max','Meta Ads','Audience research','Media planning'],
 [('thelab-strategy.webp','Audience and keyword plan, page 18'),('thelab-results.webp','Platform-level campaign results, page 19')],
 [('Marketing portfolio','Supplied PDF, pages 17–20')])

case('leaserunner','LeaseRunner','Rebuilding an organic growth engine','Professional work','SEO & content',
 'Technical SEO, content architecture, website planning and a shared marketing dashboard for a US tenant-screening service.',
 '4.9×','monthly visits in six months',
 'An established site had plateaued despite years of SEO investment. The opportunity was to make service pages, legal resources and blog content easier to discover and connect to signup.',
 ['Audited technical SEO and content, then reorganized the sitemap around screening services, landlord resources, state laws and support.',
  'Worked on page and navigation redesigns, with internal links connecting information-seeking visitors to service pages.',
  'Planned backlink and partnership activity alongside on-site improvements.',
  'Built a Looker Studio dashboard joining GA4 acquisition, Search Console visibility, page groups and signup paths for recurring reviews.'],
 [('Organic growth','Monthly visits increased from 5,600 in December 2024 to 27,500 in June 2025: 4.9× the baseline, or approximately 391% growth.'),
  ('Acquisition mix','The June GA4 view attributes 81% of sessions to organic search.'),
  ('Content-to-signup gap','Service pages converted toward signup more efficiently than high-traffic blog pages, pointing to a need for stronger internal conversion paths.'),
  ('Landing-page diagnosis','Direct traffic had a 71.1% bounce rate, making landing-page relevance a useful investigation priority.')],
 'Protect the organic base, refresh pages with declining clicks, and route relevant blog and legal-resource traffic toward high-intent services. Read signup performance alongside traffic.',
 'Search Console clicks and GA4 sessions use different definitions. Report snapshots have inconsistent totals, so they are not combined. The source table shows top-3 keywords rising from 150 to 167, not the 65% claimed on a summary slide. Signup does not establish activation or revenue.',
 ['Technical SEO','Content strategy','Looker Studio','GA4','Search Console','Website planning'],
 [('leaserunner-seo.webp','Traffic growth, page 22'),('leaserunner-design.webp','Website redesign comparisons, page 26'),('leaserunner-dashboard.png','Published marketing dashboard'),('partnerships.webp','Partnership and backlink work, page 27')],
 [('Marketing portfolio','Supplied PDF, pages 21–27'),('Original analytics case','https://kathuatwork.com/projects/marketing-analytics/leaserunner/index.html')])

case('turisvpn','TurisVPN','Growing content that leads to downloads','Professional work','SEO & content',
 'An SEO launch, multilingual content program and topic-level conversion review for a Singapore VPN product.',
 '45K','monthly visits reached in 12 months',
 'Start with an empty site, grow search visibility, then determine which content themes bring people closer to using the product.',
 ['Developed on-page SEO and content clusters, tracking rankings across Singapore, Malaysia and global searches.',
  'Reviewed localization performance, including Portuguese and Malay pages.',
  'Mapped URLs into 11 content themes and compared sessions with download events by organic, direct and referral traffic.',
  'Used median engagement and distribution checks to avoid treating a few unusually long sessions as proof of content quality.'],
 [('Organic growth','The marketing portfolio reports zero monthly visits in June 2024 and 45,000 by June 2025.'),
  ('Commercial intent','Organic VPN content converted to download at 2.15%, compared with 0.26% for Streaming. Browsing converted at 1.73%.'),
  ('High-intent opportunity','IP content had a 4.01% organic download rate, with a much smaller traffic base of 474 sessions.'),
  ('Engagement quality','Browsing had a median session duration of 160 seconds. Distribution checks provided a better editorial signal than the average alone.')],
 'Prioritize VPN and Browsing content, test expansion of high-intent IP themes, and add relevant product paths to high-volume discovery articles. Evaluate localization using conversion as well as traffic.',
 'Download events are a proxy; activation and retention are outside scope. The topic analysis covers 1 April–7 July 2025 and uses manually assigned categories. Low-volume topics need further validation. Some source narrative says zero conversions where the table contains small nonzero counts; the table takes precedence.',
 ['SEO','Content strategy','Localization','GA4','Search Console','Excel'],
 [('turis-seo.webp','Organic growth evidence, page 29'),('turis-localization.webp','Market rankings and translated-page performance, page 30'),('turis-conversion.webp','Content topic conversion table, page 31'),('turis-quality.jpg','Engagement-time distributions from the original analysis')],
 [('Marketing portfolio','Supplied PDF, pages 28–34'),('Original analytics case','https://kathuatwork.com/projects/marketing-analytics/turis-vpn/index.html')])

case('conversion-optimization','Golden Owl Solutions','Helping readers become prospects','Professional work','Conversion & CRM',
 'A conversion roadmap connecting content, service pages, forms and sales follow-up.',
 '0.10%','blog-to-service navigation rate diagnosed',
 'A large blog audience was not reaching the pages that help prospects evaluate services and make contact.',
 ['Combined GA4 page paths, Hotjar click and scroll maps and HubSpot lead context.',
  'Identified weak routes from articles to service pages, heavily clicked service tiles without links and forms abandoned after partial completion.',
  'Specified contextual article CTAs, simpler forms, clearer service navigation and stronger portfolio proof.',
  'Translated recommendations into CMS requirements so the content team could test copy and visuals.'],
 [('Funnel gap','In the January–July 2025 source analysis, 94.8% of organic sessions landed on blog content. Only about 0.10% of blog sessions continued to service pages.'),
  ('Observed improvement','The existing case reports lead conversion moving from approximately 0.6% to 2.1% after the wider roadmap and concurrent marketing activity.'),
  ('Actionable UX evidence','Heatmaps revealed dead clicks and useful content placed below the depth many visitors reached.')],
 'Create clear routes from relevant content into services, reduce contact friction, and test the journey step by step with a consistent lead definition.',
 'The reported before-and-after conversion change is observational and cannot be attributed to one change. Traffic definitions and time windows differ from the SEO growth case. Lead-level screenshots and personal contact data are excluded.',
 ['CRO','GA4','Hotjar','HubSpot','Landing pages','A/B testing'],
 [('gos-cro.jpg','Published Hotjar heatmap showing homepage service interactions'),('gos-sitemap.jpg','Proposed sitemap from the conversion roadmap')],
 [('Original case and methodology','https://kathuatwork.com/projects/marketing-analytics/gos-cro/index.html')])

case('lead-quality','Golden Owl Solutions','Giving marketing and sales a shared lead view','Professional work','Conversion & CRM',
 'A conversion dashboard linking acquisition source and market fit with sales outcomes.',
 '3','teams working from a shared view',
 'Lead volume alone could not explain which enquiries were useful or whether follow-up was working.',
 ['Connected CRM lead records to acquisition source and grouped outcomes by country and sales owner.',
  'Documented the qualified-lead stage and reporting definitions.',
  'Designed a recurring review surface for marketing, sales and business development.'],
 [('Source quality','The view made differences between high-volume and high-quality sources visible.'),('Market fit','Country-level outcomes helped identify enquiries that were poorly matched to the service offer.'),('Shared accountability','Sales-owner cuts helped separate lead-quality questions from follow-up questions.')],
 'Allocate attention using qualified outcomes, agree one lead definition, and discuss acquisition and follow-up in the same review.',
 'The original case contains estimated impact ranges, not controlled results. Those ranges are not presented as measured improvements here. CRM quality depends on consistent stage updates; only the published aggregate image is reused.',
 ['CRM','Lead qualification','Dashboard design','Stakeholder reporting'],
 [('gos-conversion.png','Aggregate customer conversion dashboard from the published portfolio')],
 [('Original analytics case','https://kathuatwork.com/projects/marketing-analytics/gos-conversion-dashboard/index.html')])

case('laptop-sgn','Laptop SGN','Finding growth between the visit and the next purchase','Professional work','Conversion & CRM',
 'Customer segmentation, product-funnel diagnosis and retention priorities for a Vietnamese e-commerce retailer.',
 '21.5%','product-page visitors reaching cart',
 'Explain whether growth should come from more acquisition, a better shopping journey or more valuable repeat behavior.',
 ['Analyzed about 100,000 GA4 rows across sessions, users, items and transactions using BigQuery, SQL and Excel.',
  'Compared channel quality and revenue per session by device and customer segment.',
  'Mapped the product-to-purchase funnel and created recency, frequency and monetary-value (RFM) segments for retention planning.'],
 [('Mid-funnel constraint','Only 21.46% of product-page visitors reached the cart; cart-to-checkout was 27.47%, while checkout-to-purchase was 63.46%.'),
  ('Customer value','Returning users converted at 2.50%, compared with 1.07% for new users.'),
  ('Audience priorities','The 18–24 group supplied 51.5% of sessions, while 25–34 users had the highest revenue per session.'),
  ('Channel review','Desktop organic traffic weakened while mobile acquisition grew, supporting a device-specific diagnosis.')],
 'Improve product and cart decision support, review paid channels against revisit value, and use RFM segments to test relevant retention offers.',
 'This is observational analysis of a 30-day back-to-school period, 8 August–7 September. Recommendations are not measured revenue gains. Revenue-unit inconsistencies in the source are omitted; conversion rates remain attached to their denominators.',
 ['GA4','BigQuery','SQL','Excel','Funnel analysis','RFM'],
 [('laptop-rfm.png','RFM segmentation from the published e-commerce case'),('laptop-retention.png','Repeat-purchase behavior from the original analysis')],
 [('Original analytics case','https://kathuatwork.com/projects/marketing-analytics/laptop-sgn/index.html')])

case('growth-and-retention','Mobility & delivery','Making promotion spend work beyond acquisition','Independent case study','Growth analytics',
 'A sanitized overview of connected work on partner growth, customer retention and channel measurement.',
 '3','connected growth decisions',
 'Distinguish sustainable growth from subsidy dependence and connect acquisition spend to activation, repeat use and commercial value.',
 ['Partner growth: compared scale, subsidy intensity and directional forecasts; built an action matrix and corrected false-positive alert logic.',
  'Retention: decomposed first-month retention by source, city, service and persona, then examined app re-entry and checkout friction.',
  'Measurement: investigated install-to-activation divergence and designed channel scorecards, lag-aligned comparisons and CAC/CIR guardrails.'],
 [('Promotion strategy','Total discount and GMV can rise together because larger partners operate at greater scale; discount intensity needs a separate view.'),
  ('Customer journey','Re-entry and checkout can constrain retention even when promotion spending is substantial.'),
  ('Acquisition quality','Install volume alone does not show whether users activate, transact or return.')],
 'Test targeted incentives with a holdout, define success using activated and retained users, and monitor commercial outcomes before expanding spend.',
 'This is an analytical case study, not employment at the business or a launched growth program. Client identifiers, partner names, sensitive figures and original screenshots are omitted from this public summary. Forecasts and proposed tests are not realized uplift.',
 ['Growth strategy','Retention','Excel','CAC','CIR','Experiment design'],[],
 [('Source context','Data CV and existing portfolio; confidential detail retained outside the public website')])

case('rokt','Rokt holdout analysis','Knowing when an experiment is ready to scale','Independent case study','Growth analytics',
 'An experiment review that keeps marketing opportunity and measurement uncertainty together.',
 '+13.9%','primary relative uplift estimate',
 'Assess whether ad exposure improved conversion, while checking whether duplicates and changing group assignment altered the interpretation.',
 ['Audited campaign-event data and removed exact duplicates before additive calculations.',
  'Compared treatment and holdout conversion using confidence intervals and a two-proportion test.',
  'Checked the answer at different units of analysis and turned the result into rollout conditions.'],
 [('Primary result','The brief-defined comparison estimated +13.9% relative uplift, with a 95% interval of +9.1% to +19.0%.'),('Sensitivity','A user-cohort view estimated +5.5% uplift (p = 0.016). Cross-group identity overlap limited confidence in the headline magnitude.')],
 'Confirm the randomization unit before sizing a rollout; use segment signals to design follow-up tests.',
 'Independent analysis of a supplied experiment dataset, not a campaign I operated for Rokt. Historical analysis does not establish realized revenue. The unit-of-randomization question remains unresolved.',
 ['A/B testing','Python','Conversion analysis','Experiment interpretation'],
 [('rokt-dashboard.png','Aggregate experiment results and measurement caveats')],
 [('Original case','https://kathuatwork.com/projects/rokt-experiment/index.html'),('Code and methodology','https://github.com/kath-pahotu/au_rokt')])

case('campaign-targeting','Bank marketing','Prioritizing outreach when capacity is limited','Independent case study','Growth analytics',
 'A historical targeting study translated into a practical campaign pilot.',
 '51.8%','historical responders captured in top 20%',
 'Identify which customers to contact first without using information only available after the contact.',
 ['Built and compared pre-contact models using 45,211 historical contacts.',
  'Separated training and test data and excluded post-contact information.',
  'Compared response capture at different campaign capacities and specified pilot measures.'],
 [('Offline targeting','On the untouched test set, the top 20% of ranked contacts captured 51.8% of historical responders.'),('Response efficiency','That band converted at 30.3%, a 2.59× lift versus the historical baseline; it represents 80% fewer contacts in an offline scenario.')],
 'Pilot the prioritized band against the existing targeting approach and measure incremental conversions, contact cost, customer complaints and opt-outs.',
 'This UCI dataset analysis is an independent project. Historical predictive lift is not causal campaign lift, and the contact reduction was not implemented. Production use needs appropriate feature review, customer identifiers and time-based validation.',
 ['Customer targeting','SQL','Python','Campaign planning'],
 [('bank-targeting.png','Historical conversion and responder capture by contact capacity')],
 [('Original case','https://kathuatwork.com/projects/bank-marketing/index.html'),('Code and methodology','https://github.com/kath-pahotu/bank_marketing_campaign_analysis')])

case('thelook','TheLook e-commerce','Turning customer segments into lifecycle priorities','Independent synthetic-data project','Growth analytics',
 'A retail analytics project reframed around loyalty, reactivation and conversion opportunities.',
 '3','customer groups for lifecycle planning',
 'Create a consistent view of acquisition, conversion and customer value from disconnected retail data.',
 ['Connected seven files using SQL and Python and built a seven-page Power BI report.',
  'Created customer segments using recency, frequency and monetary value.',
  'Compared channel funnels and separated gross sales from cancellations and returns.'],
 [('Lifecycle opportunity','The synthetic data contains 19,550 Champions, 12,977 New/Developing customers and 33,688 Hibernating customers.'),('Funnel friction','Cart abandonment was 58%, with similar rates across channels, pointing toward an onsite test rather than an automatic media-budget shift.'),('Commercial reporting','Cancellations and returns represented 25% of gross sales in this dataset.')],
 'Design different retention treatments for valuable repeat customers, developing customers and lapsed customers; evaluate tests against net value.',
 'TheLook is a synthetic dataset. These figures demonstrate analytical work and are not results delivered for a real client. Marketing spend and experiment assignment are unavailable, so ROAS and causal uplift are not claimed.',
 ['Customer segmentation','RFM','SQL','Power BI','Python'],
 [('thelook-customer.png','Customer and cohort dashboard from the synthetic retail project')],
 [('Original case','https://kathuatwork.com/projects/thelook-ecommerce/index.html'),('Code and methodology','https://github.com/kath-pahotu/the-look-ecommerce-data-analysis')])

case('promotion-review','ZaloPay promotion analysis','Understanding where promotion cost concentrates','Independent case study','Growth analytics',
 'Promotion-budget analysis that connects customer behavior, review capacity and cost exposure.',
 '26.94%','credited cost linked to 4.26% of scored users',
 'Determine where a promotion team should focus review effort without treating unusual behavior as confirmed abuse.',
 ['Analyzed approximately 254,000 transactions with SQL, Python and Power BI.',
  'Combined six behavioral signals, reconciled calculations and simulated review rules.',
  'Designed an explainable report showing cost concentration and the trade-off between review workload and coverage.'],
 [('Cost concentration','4.26% of scored users were associated with 26.94% of credited promotion cost.'),('Review design','Threshold simulation showed how changing the rule affects workload and exposed cost coverage.')],
 'Start with manual shadow-mode review, collect outcomes, and evaluate customer harm as well as potential budget recovery before automating any action.',
 'Independent portfolio analysis, not employment at ZaloPay or a deployed policy. There are no confirmed fraud labels, measured savings or campaign-attributed retention results. Flags indicate review priority only.',
 ['Promotion analytics','SQL','Python','Power BI','Rule simulation'],
 [('zalopay-exec.png','Published aggregate promotion-cost analysis')],
 [('Original case','https://kathuatwork.com/projects/zalopay-promo-abuse/index.html'),('Code and methodology','https://github.com/kath-pahotu/zalopay-promo-abuse-detection')])

case('glassdoor','Glassdoor job-market analysis','Researching a market through unstructured data','Independent case study','Research',
 'A supporting research project showing how I turn messy information into a usable market view.',
 'SQL + BI','research and communication toolkit',
 'Explore how skills, location and seniority relate to opportunities in a job-listing dataset.',
 ['Cleaned and standardized job descriptions, company attributes and salary fields with SQL.',
  'Used Python to explore requested skills and segment listings.',
  'Built a Power BI dashboard with filters for location, job level and company characteristics.'],
 [('Research skill','The workflow shows structured market segmentation, data cleaning and clear visual communication.')],
 'Use segmentation and a consistent taxonomy to turn a broad research question into comparisons people can explore.',
 'Supporting analytics project rather than a marketing campaign. The source does not establish sampling coverage or current labor-market estimates; no hiring or salary forecast is claimed.',
 ['Market research','SQL','Python','Power BI'],
 [('glassdoor.webp','Power BI modeling and dashboard work from the marketing portfolio, page 38')],
 [('Marketing portfolio','Supplied PDF, pages 35–38')])

# Confirmed project ownership and approximate solo-project durations, 15 Sep 2026.
LEAD_OWNERSHIP = 'I led planning and delivery: translated management objectives into project KPIs and milestones, allocated work and resources, trained and guided contributors, and owned progress against the agreed targets.'
SOLO_OWNERSHIP = 'I completed this project independently from end to end: framed the question, prepared and validated the data, performed the analysis, built the reporting output, and wrote the recommendations and limitations.'
PROJECT_ORDER = ['campaign-targeting', 'promotion-review', 'growth-and-retention', 'thelook', 'rokt']
GOALS = {
 'golden-owl':'Build qualified B2B demand by connecting paid acquisition, organic visibility and service-page conversion.',
 'the-lab':'Generate relevant enquiries for STEM and coding courses while controlling acquisition cost and campaign pacing.',
 'leaserunner':'Grow relevant organic traffic and improve the journey from landlord resources to tenant-screening signup.',
 'turisvpn':'Build organic visibility and direct high-intent content readers toward product downloads.',
 'conversion-optimization':'Improve the path from educational content to service discovery, enquiry and sales follow-up.',
 'lead-quality':'Give marketing and sales a consistent view of lead quality, source performance and sales progression.',
 'laptop-sgn':'Identify channel, product-funnel and retention priorities for e-commerce growth.',
 'campaign-targeting':'Prioritize likely responders within a limited outreach capacity and define a controlled validation pilot.',
 'promotion-review':'Prioritize promotion-cost review while balancing investigation workload and customer impact.',
 'growth-and-retention':'Assess subsidy efficiency, retention barriers and acquisition quality to inform allocation decisions.',
 'thelook':'Build reliable retail KPIs and turn customer, return and inventory patterns into operating recommendations.',
 'rokt':'Assess the campaign holdout result and the conditions needed for a defensible rollout decision.',
 'glassdoor':'Structure job-market information into useful comparisons of skills, location and seniority.'
}
for c in CASES:
 c['goal'] = GOALS[c['slug']]
 if c['kind'].startswith('Professional'):
  c['role'] = 'Project lead and planner'
  c['ownership'] = LEAD_OWNERSHIP
  c['period'] = 'May - Jul 2025 · 3 months' if c['slug']=='the-lab' else ('Jul - Dec 2025' if c['slug']=='laptop-sgn' else 'Apr 2024 - Sep 2025')
  c['engagement'] = 'Freelance engagement' if c['slug']=='laptop-sgn' else ('In-house marketing at Golden Owl Solutions' if c['slug'] in ['golden-owl','conversion-optimization','lead-quality'] else 'Project delivered during my Golden Owl Solutions role')
 else:
  c['role'] = 'Independent analyst · Sole contributor'
  c['ownership'] = SOLO_OWNERSHIP
  c['period'] = '2026 · Approximately '+('1 month' if c['slug'] in ['thelook','promotion-review'] else '2 weeks')
  c['engagement'] = 'Self-directed case study; completed individually'
  if c['slug'] in PROJECT_ORDER: c['sequence'] = PROJECT_ORDER.index(c['slug'])+1
CASES[:] = [c for c in CASES if c['kind'].startswith('Professional')] + sorted([c for c in CASES if not c['kind'].startswith('Professional')], key=lambda c:c.get('sequence',6))
EXPERIENCE[1]['bullets'][-1] = 'Led project planning, translated management objectives into KPIs and milestones, allocated resources, trained and guided team members, and owned delivery against agreed targets.'
EXPERIENCE[2]['bullets'][0] = 'Led a three-person content team across affiliate and e-commerce projects; defined KPIs and milestones, allocated work, trained contributors and tracked delivery against management goals.'

# September 2026: professional campaigns lead; only the five approved independent cases follow.
CASES[:] = [c for c in CASES if c['slug'] != 'glassdoor']
EXPERIENCE[1]['role'] = 'Digital Marketing Analyst'
EXPERIENCE[2]['role'] = 'Digital Marketing Executive'
EXPERIENCE[:] = [EXPERIENCE[1], EXPERIENCE[0], EXPERIENCE[2]]
for c in CASES:
 if c['slug'] == 'promotion-review':
  c['findings'].append(('Operational review queue', 'A separate balanced rule selects 1,994 users (2.31%) covering 23.89% of total credited campaign cost. This is a different cohort from the 4.26% score-based group; neither establishes confirmed abuse.'))
