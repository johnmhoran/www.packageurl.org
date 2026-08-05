---
id: news
title: News
sidebar_label: News
hide_table_of_contents: true
---

# News

Stay up to date with important news about the PURL and VERS specifications.

### PURL Spec Repo Release v1.1.0
**Date**: July 30, 2026

**Details**: Release v1.1.0 of the [purl-spec](https://github.com/package-url/purl-spec/releases/tag/v1.1.0) implements an important update to the PURL test schema - `schemas/purl-test.schema-0.2.json`. The key updates are:
- Renamed the 'base' and 'advanced' **test groups** to 'required' and 
  ' recommended' to make it more clear that a PURL implementation must pass
  the 'required' test cases to demonstrate conformance with the ECMA-427
  standard. The 'recommended' test cases document common data patterns that 
  need to be remediated (normalized) for a PURL to conform to the standard.
- Renamed the test case property: `expected_failure_reason` to 
  `expected_message` and in order to expand the usage of this property to 
  provide informational test messages beyond the reason for a test case 
  failure.
- Renamed the 'roundtrip' **test type** to 'validate'. The 'validate' 
  **test type** will not require PURL input in canonical form. It is similar
  to the 'parse' **test type** except that the test case output is a PURL 
  string instead of an object containing decoded PURL components for the 
  'parse' **test type**. Roundtrip tests are still recommended but test cases
  are not needed because the premise of a round-trip test is that the output
  equals the input.

The PURL team is planning major upgrades to the PURL test suite with this new
data structure. The test cases based on the `schemas/purl-test.schema-0.1.json`
will remain available in the `purl-spec/tests/` folder under the v1.0.1 
release tag.

### PURL Spec Repo Release v1.0.1
**Date**: July 27, 2026

**Details**: Release v1.0.1 of the [purl-spec](https://github.com/package-url/purl-spec/releases/tag/v1.1.0) 
project includes the registration of 7 new PURL types:
- brew: for Homebrew for macOS and Linux
- chrome-extension: for Chrome browser extensions
- opam: for the OCaml package manager
- vcpkg: for the vcpkg C/C++ package manager.
- vscode-extension: for VS Code extension packages
- yocto: for Yocto project recipes

and many 
