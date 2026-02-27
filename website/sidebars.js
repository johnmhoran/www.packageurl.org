/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
    purl: [
        'purl/purl-spec-introduction',
        {
            type: 'category',
            label: 'Specification',
            link: {
                type: 'doc',
                id: 'purl/purl-spec-folder-page', // The doc to display
            },
            collapsed: false,
            items: [
                'purl/specification',
                'purl/common-qualifiers',
                'purl/how-to-build',
                'purl/how-to-parse',
                'purl/tests',
            ],
        },
        'purl/purl-spec-purl-types',
        'purl/purl-spec-schemas',
        // 'purl/purl-spec-adopters',
    ],
    vers: [
        'vers/vers-spec-introduction',
        'vers/vers-spec-specification',
        'vers/vers-spec-schemas',
        // 'vers/vers-spec-adopters',
    ],
    // adopters: [
    //     'adopters/adopters-intro',
    //     'adopters/specgrid',
    //     'adopters/toolgrid',
    // ],

    getting_started: [
        {
            type: 'category',
            label: 'Getting Started',
            link: {
                type: 'doc',
                id: 'getting-started/getting-started-intro', // The doc to display
            },
            collapsed: false,
            items: [
                'getting-started/toolgrid',
                'getting-started/specgrid',
            ],
        },
    ],

    participate: [
        'participate/participate-contribute',
        'participate/participate-meetings',
        'participate/participate-events',
    ],
};

export default sidebars;
