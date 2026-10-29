"""Build CV.pdf: pip install "reportlab<4.5"; python3 scripts/build_cv.py."""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
INK = colors.HexColor('#262c29')
GREEN = colors.HexColor('#345d44')
MUTED = colors.HexColor('#555d57')
styles = {
    'name': ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=25, leading=29, textColor=INK, spaceAfter=6),
    'contact': ParagraphStyle('contact', fontName='Helvetica', fontSize=9, leading=13, textColor=GREEN),
    'section': ParagraphStyle('section', fontName='Helvetica-Bold', fontSize=10, leading=13, textColor=GREEN, spaceBefore=14, spaceAfter=8),
    'role': ParagraphStyle('role', fontName='Helvetica-Bold', fontSize=10.5, leading=14, textColor=INK),
    'date': ParagraphStyle('date', fontName='Helvetica', fontSize=9, leading=12, textColor=MUTED, spaceAfter=5),
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=9.5, leading=13, textColor=INK, spaceAfter=4),
    'bullet': ParagraphStyle('bullet', fontName='Helvetica', fontSize=9.5, leading=13, textColor=INK, leftIndent=10, firstLineIndent=-10, spaceAfter=4),
}

def p(text, style='body'):
    return Paragraph(text, styles[style])

def role(title, dates, bullets):
    return KeepTogether([p(title, 'role'), p(dates, 'date')] + [p('•  ' + text, 'bullet') for text in bullets] + [Spacer(1, 7)])

story = [
    p('Dan Cristian Octavian', 'name'),
    p('<a href="mailto:dan@danoctavian.com">dan@danoctavian.com</a>  ·  <a href="https://danoctavian.com">danoctavian.com</a>  ·  <a href="https://github.com/danoctavian">github.com/danoctavian</a>', 'contact'),
    p('<a href="https://twitter.com/danoctavian_">twitter.com/danoctavian_</a>  ·  <a href="https://www.linkedin.com/in/dan-octavian-415a6680/">LinkedIn</a>', 'contact'),
    Spacer(1, 11),
    HRFlowable(width='100%', thickness=0.6, color=colors.HexColor('#daddd3')),
    p('EXPERIENCE', 'section'),
    role('CTO / Co-founder | YieldNest', 'January 2024 – Present', [
        'Co-founded YieldNest and led protocol architecture and smart contract engineering for DeFi products that reached nine-figure Total Locked Value.',
        'Designed and built modular tokenized vault infrastructure for YieldNest MAX vaults, yield and restaking strategies, lending and liquidity pool integrations, and withdrawal and redemption mechanisms.',
        'Led the engineering team while remaining hands-on with Solidity development, security reviews, multichain deployments, and production operations.',
    ]),
    role('Core Contributor | Nexus Mutual', 'May 2020 – November 2023', [
        'Developed smart contracts and backend services enabling DeFi users to buy cover against smart contract hacks on Ethereum.',
        'Improved the staking mechanism, helping grow Total Locked Value 70× from seven figures to nine figures; launched the first tradable insurance product using NFTs and refined the Nexus Mutual V1 bonding curve.',
    ]),
    role('Head of Backend Engineering | qiibee', 'June 2018 – May 2020', [
        'Led brand integration for a blockchain-based loyalty points platform.',
        'Built the API, SDK, and bridges connecting the loyalty chain to Ethereum mainnet and Binance Chain. Supported hundreds of thousands of rewards and thousands of dollars in redemptions, helping one brand expand its programme from 5 to 50 locations.',
    ]),
    role('Software Engineer | QuanticMind', 'March 2015 – June 2018', [
        'Built backend systems to exchange millions of advertising records with Google, Bing, and other platforms. Integrated call tracking, bringing in two additional customers, and bridged the US and Argentina teams.',
        'Improved large-upload pipeline performance by 60%, achieving 2× the performance of standard AdWords tools. Transitioned the internal architecture to microservices and implemented service authentication.',
    ]),
    p('EARLIER EXPERIENCE', 'section'),
    p('<b>King</b> · Data Scientist Intern · July–September 2014<br/>'
      '<b>Amazon</b> · Software Development Engineer Intern · April–September 2013<br/>'
      '<b>Bloomberg LP</b> · Systems Team Software Developer Intern · June–September 2012'),
    p('EDUCATION', 'section'),
    p('<b>Imperial College London</b> · MEng Computing · First Class Honours<br/>October 2010 – June 2014'),
    p('CORE EXPERTISE', 'section'),
    p('Engineering leadership · DeFi protocol architecture · Solidity Smart contracts · Smart contract security<br/>'
      'Tokenized vaults &amp; yield strategies'),
    p('<b>Languages:</b> English (native fluency)'),
]

doc = SimpleDocTemplate(str(ROOT / 'CV.pdf'), pagesize=A4, rightMargin=42, leftMargin=42,
                        topMargin=34, bottomMargin=32, title='Dan Cristian Octavian — CV',
                        author='Dan Cristian Octavian')
doc.build(story)
