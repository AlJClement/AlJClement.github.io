#!/usr/bin/env python3
"""Generate Allison Clement's content pages for the Academic Pages Jekyll template.

Usage:
    python build_academic_website.py /path/to/yourusername.github.io

This creates or replaces only the named content pages and navigation file below.
It does NOT publish a Python application; GitHub Pages hosts the resulting Markdown.
Review the content and add verified publication links before committing.
"""
from pathlib import Path
import argparse

PAGES = {
    'about.md': '''---
layout: single
permalink: /
title: "About"
author_profile: true
---

# Allison Clement

**DPhil Researcher in Computer Science | University of Oxford**

I am a final-year DPhil researcher at the University of Oxford, working at the intersection of **medical image analysis, machine learning, and clinical decision support**. My research explores how image-derived measurements and clinical information can be combined to develop more interpretable AI systems for healthcare, including applications to ultrasound screening.

My background spans mechanical engineering, biomedical engineering, and computer science. Before my DPhil, I worked on research and development in healthcare, including surgical technologies and AI-based cancer applications.

I enjoy interdisciplinary research, teaching, and widening participation in STEM.

**Explore:** [Education](/education/) · [Experience](/experience/) · [Publications](/publications/) · [Teaching](/teaching/) · [Volunteering & Outreach](/volunteering/)

<!-- Add verified Google Scholar, GitHub and LinkedIn URLs here. -->
''',
    'education.md': '''---
layout: single
permalink: /education/
title: "Education"
author_profile: true
---

## University of Oxford
**DPhil in Computer Science** · In progress

Research in medical image analysis, landmark localisation, multimodal learning, uncertainty, and interpretable clinical decision support.

## University of Toronto
**Master of Applied Science in Biomedical Engineering** · 2019

Computational modelling, mechanical testing, and medical image analysis for spine cancer research. Dean's List.

## Queen's University
**Bachelor of Applied Science in Mechanical Engineering** · 2017

Specialisation in biomechanical engineering. Dean's List.
''',
    'experience.md': '''---
layout: single
permalink: /experience/
title: "Work Experience"
author_profile: true
---

## Medical AI Research Assistant — PictureHealth
**March 2022 – present** *(confirm current appointment dates)*

Development and implementation of AI approaches to cancer detection and prediction of clinical outcomes.

## Research Visit — National Institute of Informatics, Japan
**March – June 2025**

Machine learning for feature detection and evaluation in multimodal microscopy images, including scattered- and transmitted-light data.

## Research Engineer — Sunnybrook Research Institute
**September 2019 – April 2022**

Developed medical image analysis and engineering tools for musculoskeletal research and surgical applications, including segmentation, cranial implant design, and operative planning.

## Medventions Innovation Fellowship — Sunnybrook
**September – December 2020**

Worked with a multidisciplinary team to identify clinical needs, interview clinicians, and investigate technical, market, and regulatory considerations for medical technologies.

## Summer Student — Hatch Ltd.
**2015 – 2017**

Specialised engineering analysis and design.
''',
    'publications.md': '''---
layout: single
permalink: /publications/
title: "Publications"
author_profile: true
---

Selected publications and conference papers. **Add DOI, PDF, and code links once checked.**

## Medical AI and image analysis

- **Quantifying Contributions within Multimodal Fusion for Clinical Decisions.** ML-CDS Workshop, MICCAI, 2026. [Paper](https://openreview.net/forum?id=I0g7EaXGAz)
- **Confidence in angle predictions for clinical decision support.** MICCAI, 2025.
- **A handful of data: evaluating few-shot incremental landmark detection.** ICIAP, 2025 (supervising author).
- **Landmark-based screening: femoral head coverage and Graf classification in infant developmental dysplasia of the hip.** ECCV, 2024.
- **Improving Automated Ultrasound Infant Hip Screening Using an Integrated Clinical Classification Loss.** MIUA, 2024.
- **Towards Clinical Applicability and Computation Efficiency in Automatic Cranial Implant Design.** AutoImplant Challenge, 2021.

## Biomedical engineering and other research

- **Establishment and Image Based Evaluation of a New Preclinical Rat Model of Osteoblastic Bone Metastases.** Clinical & Experimental Metastasis, 2022.
- **Automated segmentation of osteoblastic vertebral metastasis: a radiomics approach.** Computer Methods in Biomechanics and Biomedical Engineering: Imaging & Visualization, 2021.
- **Biomechanical Properties of Metastatically Involved Osteolytic Bone.** Osteoporosis Reports, 2020.
- **Image Based and Biomechanical Characterization of Osteoblastic Vertebral Metastases.** University of Toronto, 2019.
- **Thermal Bending in Blast Furnace Copper Staves.** AISTech, 2017 (Josef S. Kapitan Best Paper Award).
- **Blast Furnace Hearth Thermal Assessment and Identification of Wear Zone.** AISTech, 2016.

<!-- Check final bibliographic details and authorship before publishing. -->
''',
    'teaching.md': '''---
layout: single
permalink: /teaching/
title: "Teaching"
author_profile: true
---

I enjoy helping students explore technical ideas through hands-on exercises, open questions, and real-world applications.

## University teaching

Teaching assistant, lecturer, and assessment support across the **University of Oxford, University of Toronto, and Queen's University**. Courses and dates can be added here.

## Girls Who ML

Delivered machine learning teaching and outreach activities, making technical concepts accessible to younger learners.

## Academic taster sessions

Interested in introducing students to **AI in medicine**, engineering design, and the research process—from framing a question to interpreting results. Sessions can combine computer vision examples, hands-on prediction activities, and discussion of the opportunities and limitations of medical AI.
''',
    'volunteering.md': '''---
layout: single
permalink: /volunteering/
title: "Volunteering & Outreach"
author_profile: true
---

I care about widening access to STEM and building environments where people feel confident exploring unfamiliar subjects.

## Academic leadership and inclusion

- **President, Oxford Women in Computer Science (2024–2025):** community-building and opportunities for women in computing.
- **Member, Department of Computer Science Equality, Diversity and Inclusion Board (2026):** supporting inclusive departmental initiatives.
- **Girls Who ML:** teaching and outreach in machine learning.
- **Oxbridge conference executive (2023–2024):** conference organisation.

## STEM outreach

- **Discovery Program — Physics Director (University of Toronto, 2017–2019):** developed curricula and led weekly sessions guiding secondary school students through a research project from initial idea to completion.
- **Engineer-in-Residence Outreach Program (2021–2022):** introduced primary school pupils to engineering through interactive activities.
- **Computing tutor, women's shelter in Canada (2020–2022):** supported accessible computing education.

## Earlier involvement

Activities have included Women in Science and Engineering, the Biomedical Engineering Students Association, university engineering clubs, and other community programmes.
''',
    'cv.md': '''---
layout: single
permalink: /cv/
title: "CV"
author_profile: true
---

An overview of my academic and professional experience is available throughout this website:
[Education](/education/) · [Experience](/experience/) · [Publications](/publications/) · [Teaching](/teaching/) · [Volunteering](/volunteering/).

<!-- Optional: upload an up-to-date PDF to files/Allison_Clement_CV.pdf
     and replace this note with [Download my CV](/files/Allison_Clement_CV.pdf). -->
''',
}

NAVIGATION = '''# Academic Pages top navigation
main:
  - title: "About"
    url: /
  - title: "Education"
    url: /education/
  - title: "Experience"
    url: /experience/
  - title: "Publications"
    url: /publications/
  - title: "Teaching"
    url: /teaching/
  - title: "Volunteering"
    url: /volunteering/
  - title: "CV"
    url: /cv/
'''

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('repository', nargs='?', default='.', help='Academic Pages repository directory (default: current directory)')
    parser.add_argument('--force', action='store_true', help='Replace existing generated page/navigation files')
    args = parser.parse_args()
    root = Path(args.repository).expanduser().resolve()
    if not (root / '_config.yml').exists():
        parser.error(f'{root} does not look like an Academic Pages checkout (_config.yml is missing)')
    files = {root / '_pages' / name: body for name, body in PAGES.items()}
    files[root / '_data' / 'navigation.yml'] = NAVIGATION
    existing = [path for path in files if path.exists()]
    if existing and not args.force:
        parser.error('These files already exist: ' + ', '.join(str(x.relative_to(root)) for x in existing) + '. Re-run with --force after reviewing your changes.')
    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')
        print('Wrote', path.relative_to(root))
    print('\nNext: edit _config.yml (author name, bio, links), review content, then commit and push.')

if __name__ == '__main__':
    main()
