# packageurl.org integrations and workflow

The www.packageurl.org website hosts the primary documentation for the PURL
and VERS specifications and for the Package-URL community which maintains the
specifications and some of the software packages that implement PURL or VERS
or both.

This document covers the flow of information into the `www.packageurl.org`
repository and how that information is deployed to the staging and production
instances of www.packageurl.org.

## Documentation sources

### Documents

The `website/docs/` folder contains a sub-folder for each major section of
the website:

| Folder                      | Content Summary                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------ |
| getting-started             | \`.mdx\` files for the Tools and Spec cards                                                |
| news                        | Markdown files that are maintained in the www.packageurl.org repo                          |
| participate                 | Markdown files that are maintained in the www.packageurl.org repo                          |
| purl-spec/types/definitions | Copies of the PURL type definition markdown files from \`purl-spec/docs/types/definitions\`|
| purl                        | Markdown files where some are copied from `purl-spec/docs/specification` and others are maintained in the www.packageurl.org repo |
| vers                        | Markdown files where some are copied from `vers-spec/docs/specification` and others are maintained in the www.packageurl.org repo |

The current set of files that are copied from the `purl-spec` or `vers-spec`
repo to the `wwww.packageurl.org` repo are:

| `www.packageurl.org` File    | Copied from                       |
| ---------------------------- | --------------------------------- |
| website/docs/purl/common-qualifiers.md   | purl-spec/main/docs/specification/common-qualifiers.md |
| website/docs/purl/how-to-build.md        | purl-spec/main/docs/specification/how-to-build.md      |
| website/docs/purl/how-to-parse.md        | purl-spec/main/docs/specification/how-to-parse.md      |
| website/docs/purl/test-overview.md       | purl-spec/main/docs/tests/test-overview.md             |
| website/docs/purl/test-suite.md          | purl-spec/main/docs/tests/test-suite.md                |
| website/docs/purl/test-schema-changes.md | purl-spec/main/docs/tests/test-schema-changes.md       |
| website/docs/vers/faq.md                 | vers-spec/main/docs/faq.md                             |
| website/docs/vers/how-to-parse.md        | vers-spec/main/docs/specification/how-to-parse.md      |
| website/docs/vers/introduction.md        | vers-spec/main/docs/specification/introduction.md      |
| website/docs/vers/specification.md       | vers-spec/main/docs/specification/specification.md     |
| website/docs/vers/test-overview.md       | vers-spec/main/docs/tests/test-overview.md             |
| website/docs/vers/test-suite.md          | vers-spec/main/docs/tests/test-suite.md                |
| website/docs/vers/test-schema-changes.md | vers-spec/main/docs/tests/test-schema-changes.md       |
| website/docs/vers/vers-types.md          | vers-spec/main/docs/types/vers-types.md                |

This mapping of `www.packageurl.org` repo document files to their `purl-spec`
or `vers-spec` repo origin is kept in the file: `website/docusaurus.config.js`.
The files are copied to the `www.packageurl.org` repo with a "pull" style
GitHub Action [Sync markdown docs from purl-spec and vers-spec](https://github.com/package-url/www.packageurl.org/actions/workflows/sync_md_docs.yml)
from the `wwww.packageurl.org` repo. The GH pull Action runs automatically on
a daily basis or on demand manually.

This mapping is expected to change as we update the website.

### PURL and VERS type definition files

The (generated) markdown versions of PURL `type` definition files are copied to
the `www.packageurl.org` repo with a "pull" style GitHub Action
[Sync purl-spec Type Definitions](https://github.com/package-url/www.packageurl.org/actions/workflows/sync-types-definitions.yml)
from the `wwww.packageurl.org` repo. The GH pull Action runs automatically on
a daily basis or on demand manually.

Clicking on a PURL `type` card on the PURL Types grid opens the corresponding
markdown file on the website (not a new browser tab)

We will probably create a similar GitHub Action to pull VERS `type` definition
files (markdown versions) from the `vers-spec` repo after we complete an
initial set set of VERS `type` definitions. There will be an additional
challenge for VERS `types` because the JSON `type` definition files need to be
augmented by additional "how-to" information for each `type`.

### Schema definition files

The primary sources for the PURL and VERS schema definition files are:
- `purl-spec/schemas/`
- `vers-spec/schemas/`

where each file is versioned according to the patterns:
- `purl-type-definition.schema-<major>.<minor>.json`
- `vers-type-definition.schema-<major>.<minor>.json`

There are copies of the of PURL and VERS (JSON) Schema files in the folder
`website/static/schemas` for display on the website. These files are currently
updated manually because:
- The volume and rate of change for these schema files are much less than for
  the PURL `type` definition files (now) and VERS `type` definition files (in
  the near future).
- we need to stage any changes to the schema definitions with TC54 approval
  cycles.

For the PURL and VERS test schemas we may want to automate updates from the
`purl-spec` or `vers-spec` repos, but the rate of change may not warrant
automation.

### Schema and `type` definition folders on www.packageurl.org

We need to host copies of the PURL and VERS schema definition files and the
`type` definition files on the production (Dreamhost) instance of
www.packageurl.org in folders that match the URLs documented in the '$schema'
or '$id' fields in the schema and ` type` definition files. The current lists
are:

#### PURL & VERS schema files
- `wwww.packageurl.org/purl-schemas/`:
  - `purl-test.schema-0.2.json`
  - `purl-type-definition.schema-1.1.json`
- `wwww.packageurl.org/schemas/`:
  - `purl-test.schema-0.1.json`
  - `purl-type-definition.schema-1.0.json`
  - `purl-types-index.schema-1.0.json`
  - `vers-test.schema-0.1.json`
- `wwww.packageurl.org/vers-schemas/`:
  - `vers-test.schema-0.2.json`
  - `vers-type-definition.schema-1.0.json`
  - `vers-types-index.schema-1.0.json`

#### PURL & VERS `type` definition files
- `wwww.packageurl.org/purl-types/`: All PURL `type` definition files using
  `purl-type-definition.schema-1.1`.json`
- `wwww.packageurl.org/types/`: All URL `type` definition files using
  `purl-type-definition.schema-1.0.json`
- `wwww.packageurl.org/vers-types/`: All VERS `type` definition files

*Change required*

With the current workflows for managing www.package.url we will need to keep
copies of all of the PURL & VERS schema and `type` definition files in the
`www.packageurl.org` repo because the current deployment approach for the
production (Dreamhost) website is a complete replacement of the files based on
the latest docusaurus build. We do this already for the files in the
`wwww.packageurl.org/schemas` folder but not for any of the other cases. For
PURL `type` definitions we have copies of the generated markdown PURL `type`
definition files in the folder `website/purl-spec/types/definitions/` but we
need to add copies of the "source" JSON format PURL `type` definition files.

## Deployment

### Staging

The "staging" version of the website is at: https://package-url.github.io/www.packageurl.org. The 
staging website is updated by the GitHub Action [Build & Deploy Docusaurus Site](https://github.com/package-url/www.packageurl.org/actions/workflows/A-B-deployment.yml)
whenever a PR is merged in the `www.packageur.org` repo. A PR push triggers a workflow to 
rebuild the Docusaurus Site, but a PR push does not update the staging website.

### Production

The current "production" version of the website is at: https://www.packageurl.org
which is hosted at Dreamhost under the nexB account. There is currently no
automatic deployment for the production website. An update deployment is
initiated by a manual invocation of the GitHub Action [Build & Deploy Docusaurus Site](https://github.com/package-url/www.packageurl.org/actions/workflows/A-B-deployment.yml)
which a target of 'dreamhost' instead of the default 'gh'.

