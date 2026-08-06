---
id: spec-news
title: Specification News
sidebar_label: Specifications
hide_table_of_contents: true
---

# Specification News

Stay up to date with important news about the PURL and VERS specifications.

## PURL Test Schema v0.2
**Date**: August 4, 2026

**Details**: We implemented a very important update to the PURL test schema - 
`schemas/purl-test.schema-0.2.json`. The key updates are:
- Renamed the PURL **test groups** from 'base' and 'advanced' to 'required' 
  and ' recommended' to make it more clear that a PURL implementation must 
  pass the 'required' test cases to demonstrate conformance with the ECMA-427
  standard. The 'recommended' test cases document common data patterns that 
  need to be normalized for a PURL to conform to the standard.
- Renamed the 'roundtrip' **test type** to 'validate'. The 'validate' 
  **test type** will not require PURL input in canonical form. It is similar
  to the 'parse' **test type** except that the test case output is a canonical
  PURL string instead of an object containing decoded PURL components for the 
  'parse' **test type**. "Round-trip" tests are still recommended, but 
  specific test cases are not needed because the premise of a round-trip test 
  is that the output equals the input.
- Renamed the test case property: `expected_failure_reason` to 
  `expected_message` in order to expand the usage of this property to 
  provide informational test messages beyond the reason for a test case 
  failure.

The PURL team is planning major upgrades to the PURL test suite with this new
data structure. 
- The test cases based on the `schemas/purl-test.schema-0.1.json` will remain
  available in the `purl-spec/tests/` folder under the v1.0.1 release tag.
- The PURL team is in the process of applying the `purl-test.schema-0.2.json`
  changes to all existing test case files. We will publish PURL Spec Release 
  1.1.0 after the test cases are updated to match the new schema.


## VERS Spec Release v1.0.0
**Date**: August 4, 2026
**Details**: Release v1.0.0 of the [vers-spec](https://github.com/package-url/vers-spec/releases/tag/v1.0.0) is the first release for VERS.


## PURL Spec Release v1.0.1
**Date**: August 3, 2026

**Details**: Release v1.0.1 of the [purl-spec](https://github.com/package-url/purl-spec/releases/tag/v1.0.1) project includes the registration of 7 new PURL 
types:
- brew: for Homebrew for macOS and Linux
- chrome-extension: for Chrome browser extensions
- opam: for the OCaml package manager
- otp: for BEAM/OTP applications written in Elixir, Erlang, Gleam or other 
  BEAM languages
- vcpkg: for the vcpkg C/C++ package manager.
- vscode-extension: for VS Code extension packages
- yocto: for Yocto project recipes

and an important change to the 'cpan' PURL **type** to make the **namespace**
PURL component optional.

