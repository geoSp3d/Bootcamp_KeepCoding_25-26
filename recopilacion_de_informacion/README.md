# Tesco Recon – Clean Technical Export

Clean and shareable technical repository for a scoped reconnaissance and OSINT exercise conducted against `*.tesco.com` as part of a bug bounty / security training workflow.

## Objective

The goal of this repository is to document a structured external assessment of Tesco’s public-facing surface through:

- footprinting
- fingerprinting
- vulnerability-oriented validation
- OSINT and public exposure review

This repository contains only the **clean, reviewable, and shareable subset** of the work. Raw outputs, duplicated data, excessive noise, and auxiliary material have been excluded.

---

## Scope

Primary scope reviewed:

- `*.tesco.com`

Supporting public sources were also reviewed where relevant to OSINT validation, including:

- publicly accessible Tesco-related documents
- public executive and employee references
- external breach intelligence sources
- public infrastructure relationships

---

## Methodology Overview

The workflow followed four main phases:

1. **Footprinting** 
Passive and semi-passive discovery of subdomains, historical URLs, TLS context, and external relationships.

2. **Fingerprinting** 
Validation of live assets, HTTP behavior, technology fingerprinting, visual inspection, WAF/CDN identification, and selective service enumeration.

3. **Vulnerability Validation** 
Focused testing with automation and manual verification of exposed functionality or disclosure points.

4. **OSINT Review** 
Analysis of publicly accessible documents, metadata leakage, personnel/contact exposure, breach intelligence correlation, and external threat context.

---

## Repository Structure

### `footprinting/`

Outputs from the discovery and reconnaissance phase:

- `shuffledns_clean.txt` → subdomains identified via DNS bruteforce
- `ctfr_clean.txt` → subdomains extracted from Certificate Transparency logs
- `gau_domains_scope.txt` → domains and URLs obtained from web archive / cached sources
- `analytics.txt` → Google Analytics pivot attempt (no relevant results)
- `cero.txt` → TLS probing output
- `katana.txt` → basic crawling results

---

### `fingerprinting/`

Outputs related to asset validation, service characterization, and technology analysis:

- `targets_alive.txt` → live hosts
- `targets_alive_code.txt` → live hosts with HTTP status codes
- `targets_200.txt` → subset of hosts returning `200 OK`
- `whatweb_clean.txt` → filtered technology fingerprint inventory
- `waf_results.txt` → initial WAF detection results
- `waf_results_recheck.txt` → WAF revalidation
- `ffuf_final.json` → final fuzzing results
- `masscan_full.txt` → fast port scan results over resolved IPs
- `nmap_94_125_16_17.txt` → targeted validation of non-web ports detected during scanning

---

### `vuln/`

Outputs from automated and manual validation of exposure:

- `nuclei_mhc.txt` → initial Nuclei scan (`0` confirmed findings)
- `nuclei_mhc_recheck.txt` → Nuclei recheck (`0` confirmed findings)
- `subzy.txt` → subdomain takeover check
- additional manual validation notes may be referenced from the final report

---

### `osint/`

Outputs from the public-document and external exposure review:

- `public_docs_index.txt` → index of relevant public documents discovered during dorking
- `book2_summary.txt` → summary of the public contact-directory exposure finding
- `veg_tracker_metadata.txt` → extracted metadata from `veg-tracker.pdf`
- `executive_exposure_sample.txt` → reduced sample of executive/public-email correlation findings
- `hibp_sample_notes.txt` → manual notes from a limited breach-intelligence review
- `maltego_summary.txt` → relevant Maltego pivots (people, emails, MX, NS)
- `infostealer_notes.txt` → contextual observations from stealer-log related sources
- `darkweb_robin_summary.txt` → supplementary external threat-intelligence summary

---

### `screenshots/`

Selected screenshots of relevant web assets and validation steps captured during the assessment.

---

### `notes/`

Auxiliary notes and summarized outputs from supporting tools.

#### `notes/spiderfoot/`

Cleaned SpiderFoot-derived references:

- `spiderfoot_providers_clean.txt` → relevant providers and external dependencies
- `spiderfoot_headers_clean.txt` → useful headers / technology context
- `SpiderFoot.csv` → base export preserved for reference
- `SpiderFoot(4).csv` → email/provider relationship export preserved for reference

---

## Tools Used

### Footprinting
- shuffledns
- ctfr
- gau
- katana
- analyticsrelationships
- cero

### Fingerprinting
- httpx
- gowitness
- whatweb
- wafw00f
- masscan
- nmap

### Vulnerability Validation
- ffuf
- nuclei
- subzy

### OSINT / External Exposure Review
- exiftool
- Maltego
- LinkedIn
- Have I Been Pwned (HIBP)
- public search / dorking
- infostealer intelligence sources
- Robin

### Supporting Analysis
- SpiderFoot

---

## Key Technical Takeaways

The assessed surface showed:

- extensive use of CDN/WAF and edge protection layers
- strong segmentation across services
- multiple third-party dependencies and external providers
- no critical findings confirmed through automated scanning alone
- several items requiring manual validation beyond tool output
- meaningful OSINT value from public document exposure and metadata leakage
- externally correlatable corporate contact data and identity exposure indicators

---

## Consolidated Findings

The broader assessment produced the following main findings:

### H1 — Publicly Exposed Contact Directory 
**Severity:** Medium

A publicly accessible Tesco-related PDF exposed structured contact information, including store-linked names and email addresses. This materially increases the risk of targeted phishing, impersonation, and personnel enumeration.

---

### H2 — Document Metadata Leakage 
**Severity:** Informational / Low

Metadata extracted from a public PDF revealed internal workstation path details, local username references, and document-production tooling. While not directly exploitable, this supports infrastructure and personnel profiling.

---

### H3 — Internal Hostname Disclosure via Public Health Endpoint 
**Severity:** Informational / Low

A public `/health` endpoint on `pbtool.tesco.com` disclosed an internal backend hostname. This represents infrastructure information disclosure and may aid technical reconnaissance.

---

### H4 — External Exposure of Corporate Email Identities 
**Severity:** Informational / Low

A reduced sample of Tesco-related corporate email identities was found to be externally correlatable through public executive information and breach-intelligence-style sources. This does not demonstrate internal compromise, but it increases phishing and impersonation risk.

---

## Notes on Interpretation

This repository should be read as a **clean technical export**, not as a full raw evidence archive.

Important distinctions:

- absence of findings in automated tooling does **not** imply absence of exposure
- several relevant results emerged only through **manual validation**
- OSINT findings are presented conservatively and do not imply compromise of Tesco infrastructure unless explicitly demonstrated

---

## Limitations

- raw scanner outputs and noisy intermediate data have been intentionally excluded
- some external-source findings are included only as contextual intelligence, not as primary evidence
- screenshots and summaries are selective and designed for reviewability rather than exhaustiveness

---

## Reviewer Notes

This repository is intended to support tutor/instructor review of:

- methodology
- technical reasoning
- validation quality
- evidence hygiene
- distinction between weak signals, supporting context, and reportable findings

---

## Disclaimer

This repository documents a scoped educational / research exercise focused on externally observable information and shareable technical outputs only.

No sensitive credentials, full breach datasets, or unnecessary personal data are included.

---

## Status

Current state:

- footprinting completed
- fingerprinting completed
- vulnerability validation completed
- OSINT findings consolidated
- clean export prepared for review

---

## Author

Dani García (alias geoSp)
