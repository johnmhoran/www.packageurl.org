# packageurl.org integrations and workflow

The www.packageurl.org website hosts the primary documentation for the PURL
and VERS specifications and for the Package-URL community which maintains the
specifications and some of the software packages that implement PURL or VERS
or both.

This document covers the flow of information into the www.packageurl.org
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

| www.packageurl.org File                  | Copied from                                            |
| ---------------------------------------- | ------------------------------------------------------ |
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

This mapping of `www.packageurl.org` repo files to their `purl-spec` or
`vers-spec` repo origin is kept in the file: `website/docusaurus.config.js`.
The files are copied to the `www.packageurl.org` repo with a "pull" style
GitHub Action [Sync markdown docs from purl-spec and vers-spec](https://github.com/package-url/www.packageurl.org/actions/workflows/sync_md_docs.yml)
from the `wwww.packageurl.org` repo. The GH pull Action is triggered by ??????

This mapping is expected to change as we update the website.

### PURL and VERS type definition files

The (generated) markdown versions of PURL `type` definition files are copied to
the `www.packageurl.org` repo with a "pull" style GitHub Action
[Sync purl-spec Type Definitions](https://github.com/package-url/www.packageurl.org/actions/workflows/sync-types-definitions.yml)
from the `wwww.packageurl.org` repo. The GH pull Action is triggered by
??????

We will create a similar GitHub Action to pull VERS `type` definition files
(markdown version) from the `vers-spec` repo.

### Schema definition files

There are copies of the of PURL and VERS (JSON) Schema files in the folder
`website/static/schemas` for display on the website. These files are currently
updated manually for several reasons:
- The volume and rate of change for these schema files are much less than for
  the PURL `type` definition files now and VERS `type` definition files in the
  near future.
- For the PURL and VERS `type` definition schemas we need to stage any changes
  with TC54 approval cycles.
- For the PURL and VERS test schemas we may want to automate updates from the
  `purl-spec` or `vers-spec` repos, but the rate of change may not warrant
  automation.

## Deployment

The "staging" version of the website is at: https://package-url.github.io/www.packageurl.org/.
The current "production" version of the website is at: https://www.packageurl.org/.








