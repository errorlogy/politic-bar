# Security Policy

## Reporting a vulnerability

Open a [GitHub issue](https://github.com/errorlogy/politic-bar/issues) with the **security** label,
or contact the maintainers via https://errorlogy.com. Do not commit secrets or live credentials
in issues or pull requests.

## Secrets and environment variables

- **Never commit** `.env`, API keys, OAuth client secrets, or credential files.
- Set `ANTHROPIC_API_KEY` in your local environment only when running the v0.6 sketch pipeline.
- If a key was ever stored on disk outside environment variables, **rotate/revoke** it with the
  provider immediately — even if the file was gitignored.

| Variable | Risk if leaked |
|----------|----------------|
| `ANTHROPIC_API_KEY` | LLM provider billing / abuse |

## Pipeline safety

The v0.6 sketch pipeline (`politic_bar/`, `run.py`) sends source bundles to the Anthropic API.
Do not point it at confidential documents without reviewing data-handling policy.

Seed cases in `cases/` are public historical governance records — treat new source bundles the
same way: no PII, no unreleased classified material, no credentials embedded in text.

## Supported versions

Security fixes are applied on `main`. Older tags may not receive backports.

## Related repositories

- Engine and API hardening: [errorlogy/errorlogy](https://github.com/errorlogy/errorlogy) → `SECURITY.md`
- Institutional contracts: [errorlogy/ai-native-gov](https://github.com/errorlogy/ai-native-gov)
