# packageurl.org website structure 
**This document was archived for potential future use. It does not include major changes made in July 2026.**

Looking at the links in the website's navbar (defined in `../website/docusaurus.config.js`) ^:

- **www.packageurl.org logo**
    - **link**: website Home (landing page)

- **Home**
    - **link**: website landing page
    - **edit**: submit an issue
    - **structure**: website landing page is defined with a series of nested
      index.js, .css and other files, e.g.:
        - *primary index.js*: `../website/src/pages/index.js`
            - *HomepageHeader*: `../website/src/components/HomepageHeader/index.js`
            - *HomepageContent*: `../website/src/components/HomepageContent/index.js`
                - *HomeInfo*: `../website/src/components/HomepageContent/HomeInfo.mdx`
                - *GeneralInfo*: `../website/src/components/GeneralInfo`

- **PURL**
    - **link**: a group of .md pages organized around a sidebar nav
    - **edit**: each .md has an `Edit this page` link in the lower-left
      corner of the page
    - **structure**:
        - *Introduction*: `..website/docs/purl/introduction.md`
        - *Specification*: `..website/docs/purl/specification-folder.md`
            - *Core Specification*: `..website/docs/purl/specification.md`
            - *PURL qualifiers guidance*: `..website/docs/purl/common-qualifiers.md`
            - *How to build a PURL*: `..website/docs/purl/how-to-build.md`
            - *How to parse a PURL*: `..website/docs/purl/how-to-parse.md`
            - *PURL test overview*: `..website/docs/purl/tests.md`
        - *PURL Types*: `..website/docs/purl/purl-types.mdx`
        - *Schemas*: `..website/docs/purl/schemas.md`

- **VERS**
    - **link**: a group of .md pages organized around a sidebar nav
    - **edit**: each .md has an `Edit this page` link in the lower-left
      corner of the page
    - **structure**:
        - *Introduction*: `..website/docs/vers/introduction.md`
        - *Specification*: `..website/docs/vers/specification-folder.md`
            - *Core Specification*: `..website/docs/vers/specification.md`
            - *How to parse and validate VERS*: `..website/docs/vers/how-to-parse.md`
            - *VERS test overview*: `..website/docs/vers/tests.md`
        - *Version schemes*: `..website/docs/vers/version-schemes.md`
        - *Schemas*: `..website/docs/vers/schemas.md`
        - *FAQ*: `..website/docs/vers/faq.md`

- **Getting Started**
    - **link**: a group of .md pages organized around a sidebar nav
    - **edit**: each .md has an `Edit this page` link in the lower-left
      corner of the page
    - **structure**:
        - *Getting Started*: `..website/docs/getting-started/introduction.mdx`
            - *Tools*: `..website/docs/getting-started/toolgrid.mdx`
            - *Specifications*: `..website/docs/getting-started/specgrid.mdx`

- **Participate**
    - **link**: a group of .md pages organized around a sidebar nav
    - **edit**: each .md has an `Edit this page` link in the lower-left corner
      of the page
    - **structure**:
        - *Contribute*: `..website/docs/participate/contribute.md`
        - *Meetings*: `..website/docs/participate/meetings.md`
        - *Events*: `..website/docs/participate/events.md`

- **GitHub**
    - **link**: https://github.com/package-url/www.packageurl.org
    - **edit**: submit an issue
    - **structure**: a link in `../website/docusaurus.config.js`

- **Slack**
    - **link**: https://cyclonedx.slack.com/
    - **edit**: submit an issue
    - **structure**: a link in `../website/docusaurus.config.js`

- **light/dark toggle**
    - provided by default in `classic` theme
