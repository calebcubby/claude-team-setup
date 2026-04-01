# Deployment Guide

## Cloudflare (Native)

### 1. Deploy Static Site

```bash
wrangler pages deploy . --project-name=your-team-setup
```

Or connect a GitHub repo for auto-deploy on push.

### 2. Set Up Auth (Optional)

Use Cloudflare Access to gate the setup page to your company's SSO.

### 3. Set Up Admin Panel

The admin panel at `/admin/` manages per-tab access (Cowork, Code tabs). It requires:
- Cloudflare KV namespace for access lists
- API routes in your Worker (see `admin/index.html` for endpoint specs)

### 4. Share the Install URL

Team members run:

```bash
curl -sL https://your-domain.com/claude-setup/install.sh | bash
```

Then open Claude Code and run `/team-setup`.

---

## Alternative Platforms

### Static Hosting

`index.html` is fully self-contained. Deploy to:
- **Vercel / Netlify / GitHub Pages** - drag and drop
- Any web server that can serve static HTML

### Admin Panel

The admin panel uses Cloudflare KV for storage. Alternatives:
- **Redis** - swap KV calls for Redis commands
- **Supabase** - use a Postgres table
- **File-based** - JSON file on disk (simplest for small teams)

### Auth

Without Cloudflare Access, implement your own:
- **Auth0 / Clerk** - JWT middleware
- **HTTP Basic Auth** - simplest option for internal tools
- **VPN-only access** - no auth needed if behind VPN
