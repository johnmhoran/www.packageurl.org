---
name: 'Add Tool '
about: Add a tool that supports PURL or VERS
title: 'Add Tool:'
labels: ''
assignees: ''

---

This is an issue template for the data we need to add your Software Tool to the Package-URL website homepage to show your support for the PURL or VERS specification or both. Each Software Tool card has a main card displayed in the grid and a modal card displaying all fields with data.
- Please provide the data that are relevant for your software tool. Empty fields will not be displayed.
- The fields displayed on the main card are shown in the list with '(main)'

If you want to create a pull request you can propose adding an entry to https://github.com/package-url/www.packageurl.org/blob/main/website/src/data/tools.json. 

Name (main:) 
*The short name for your tool. If the name is 'purl' or 'vers' please append your repo name for uniqueness.*
Publisher: 
*The name of the organization or person who publishes the tool.*
Description: 
*Short description of what your tool does.*
Homepage URL (main): 
*This will usually be the URL for your code repository. We will add a link to this URL to the Name displayed on the main card.*
Source Download URL: 
*URL for downloading source releases or if different from the Homepage URL,*
Package Download URL: 
*URL for downloading a software package for your tool at Maven, npm, PyPI or other package repository.*
Documentation URL: 
*URL for documentation if different from your Homepage URL.*
Base Language (main): 
*The primary language(s) for the source code. Separate multiple languages with a comma.*
Software License (main): 
*SPDX License Identifier or License Expression. See [ScanCode LicenseDB](https://scancode-licensedb.aboutcode.org/) for a list of 2500 SPDX-compliant License Identifiers.*
Data License: 
*SPDX License Identifier or License Expression if your tool provides data under a different license than the software.*
Service License: 
*SPDX License Identifier or License Expression if your tool provides a public API or other service under a different license than the software.*
Type: 
*Current values are: 'Application', 'CLI Utility', 'Library' or 'Service'*
Platform: 
*Current values are:'Container', 'Linux', 'MacOS', 'Windows' or other. Separate multiple platforms with a comma.*
Standards (main): 
*Current values are: 'PURL v1.0' or 'VERS'. Separate with a comma if your tool supports both.*
Notes: 
*Additional information about your tool - as needed.*
Icon: 
*URL to an icon that you want displayed on the main card.*
