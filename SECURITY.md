# Security Policy

## Supported Versions

Only the latest version on the `main` branch of **AutomatedTestingNP** receives security updates and maintenance.

| Version / Branch | Supported          |
| ---------------- | ------------------ |
| `main` (latest)  | :white_check_mark: |
| Older commits    | :x:                |

## Reporting a Vulnerability

We take the security of this repository and its CI/CD workflows seriously. If you discover a security vulnerability, credential exposure, or unsafe configuration:

1. **Do NOT open a public GitHub issue** for sensitive security vulnerabilities.
2. Report the issue privately via [GitHub Private Vulnerability Reporting](https://github.com/oleksandrmyhydiuk/AutomatedTestingNP/security/advisories/new) or by contacting the repository maintainer [@oleksandrmyhydiuk](https://github.com/oleksandrmyhydiuk).
3. Include the following details in your report:
   - A clear description of the issue and its potential impact.
   - Steps to reproduce or proof-of-concept details.
   - Affected files, dependencies, or workflow configurations.
   - Suggested remediation (if available).

### Response Timeline

- **Initial Acknowledgment:** Within **48 hours** of submission.
- **Status Update & Triage:** Within **5 business days**.
- **Resolution / Patch:** Depending on complexity, fixes are typically released within **7–14 days**.

## Security Best Practices for Contributors

When contributing tests, page objects, or workflow changes to this project, please follow these security guidelines:

- **No Sensitive Data or PII:** Never commit real personal data, real customer phone numbers, personal addresses, or active private Nova Poshta tracking numbers (EN). Always use synthetic/mock tracking numbers (e.g., `20450000000000`, `00000000000000`) or environment variables.
- **No Hardcoded Secrets:** Never commit API keys, tokens, cookies, or credentials to the repository. Store sensitive values in `.env` (which is git-ignored) or GitHub Actions Encrypted Secrets.
- **Dependency Hygiene:** Keep third-party packages in `requirements.txt` minimal and pinned to verified versions (`pytest`, `selenium`, `pytest-html`).
- **Artifact Hygiene:** Do not commit locally generated test reports (`report.html`, `reports/`) that could inadvertently capture local environment variables or filesystem paths.
- **CI/CD Least Privilege:** GitHub Actions workflows must scope `GITHUB_TOKEN` permissions strictly to what is required and only publish reports to GitHub Pages from trusted `main` branch pushes.
