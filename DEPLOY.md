# Deploying the docs to AWS Amplify

The site is a plain static VitePress build, so Amplify only has to run the build and
serve the output directory. Three files in this repo drive it:

| File | Purpose |
| --- | --- |
| `amplify.yml` | Build spec: `npm ci`, `npm run docs:build`, publish `satori_help/docs/.vitepress/dist` |
| `customHttp.yml` | Security headers, immutable caching for `/assets/**`, revalidation for HTML |
| `.nvmrc` | Pins Node 20 (VitePress 1.6 requires Node 18+) |

## Create the app (console)

1. Open **AWS Amplify** in the region you want (for example `us-east-1`) and choose
   **Create new app → Deploy your app**.
2. Pick **GitHub** and authorize the AWS Amplify GitHub App. Install it on the
   `satorici` organization and grant access to the `satori-docs` repository.
3. Select repository `satorici/satori-docs` and the branch you want to publish
   (`v2` for the CLI v2 docs, `main` once it is merged).
4. Amplify detects `amplify.yml` automatically. Confirm the build settings show:
   - build command `npm run docs:build`
   - output directory `satori_help/docs/.vitepress/dist`
   Do **not** let the console overwrite the spec with an auto-generated one.
5. Leave the app as a static web app. No environment variables or server-side
   compute are needed, and the build needs no secrets.
6. Review and **Save and deploy**. The first build takes a couple of minutes.

## Serve the right 404 page

Amplify's default rule sends unmatched paths to `index.html`. This site is
multi-page, not a single-page app, and VitePress emits its own `404.html`.

In **Hosting → Rewrites and redirects**, delete the default `/<*>` rule and add:

| Source | Target | Type |
| --- | --- | --- |
| `/<*>` | `/404.html` | 404 (Not Found) |

All internal links are generated with an `.html` extension and every one maps to a
real file, so no clean-URL rewrite is required.

## Custom domain

Under **Hosting → Custom domains**, add `docs.satori.ci` and follow the DNS
instructions. The domain is currently served by GitHub Pages, so cut over
deliberately:

1. Add the domain in Amplify and wait for the certificate to be issued.
2. Repoint the DNS record for `docs.satori.ci` at the Amplify domain.
3. Disable `.github/workflows/static.yml` so GitHub Pages stops publishing and
   there is only one source of truth.

`sitemap.hostname` in `satori_help/docs/.vitepress/config.mjs` is already
`https://docs.satori.ci`, so it needs no change if the domain is kept.

## Create the app from the CLI (alternative)

Connecting a repository without the console requires a GitHub personal access token
with `repo` scope.

```sh
aws amplify create-app \
  --name satori-docs \
  --repository https://github.com/satorici/satori-docs \
  --oauth-token "$GITHUB_TOKEN" \
  --platform WEB \
  --custom-rules '[{"source":"/<*>","target":"/404.html","status":"404"}]'

aws amplify create-branch --app-id <APP_ID> --branch-name v2 --enable-auto-build
aws amplify start-job --app-id <APP_ID> --branch-name v2 --job-type RELEASE
```

`--build-spec` is not needed because `amplify.yml` is committed to the repository.

## Verifying a build locally

Amplify runs exactly these commands, so reproduce a failure with:

```sh
rm -rf node_modules satori_help/docs/.vitepress/dist
npm ci
npm run docs:build
```

The build fails on broken internal links, which makes it a useful check before
pushing documentation changes.
