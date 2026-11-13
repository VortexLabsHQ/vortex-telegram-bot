# Security Policy

## Reporting a vulnerability

**Do not open a public GitHub issue for a security problem.**

If you find a vulnerability — especially one that could leak API keys,
bot tokens, or user data — please report it privately so we can fix it
before it is discussed in public:

- Open a **private security advisory** on this repository
  (GitHub → Security → Report a vulnerability), or
- Email the maintainers at **security@vortexlabs.example**
  (replace with the real contact address once published).

Please include:

- a description of the issue and what it affects,
- steps to reproduce it (or a minimal proof of concept),
- anything you think might help fix it.

We will acknowledge your report, work on a fix, and credit you in the
release notes if you would like that.

## A note on secrets

Vortex needs real credentials to run (a Telegram bot token, LLM API
keys, image-service keys). **Never commit those to the repository:**

- Keep them in a local `.env` file only — `.env` is gitignored.
- Use `.env.example` as the template; it contains only fake sample values.
- If you accidentally commit a real key or token, **revoke it
  immediately** at the provider, then tell us so we can help clean up
  the history — a committed secret must be treated as compromised even
  after it is removed from the code.

## Supported versions

Only the latest release on the `main` branch receives security fixes.
If you are running an older version, please update first and check
whether the issue still reproduces.
