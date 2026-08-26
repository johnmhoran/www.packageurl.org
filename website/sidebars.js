/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
    purl: [
        'purl/introduction',
        {
            type: 'category',
            label: 'Specification',
            link: {
                type: 'doc',
                id: 'purl/specification-folder', // The doc to display
            },
            collapsed: false,
            items: [
                'purl/spec-placeholder',
                'purl/common-qualifiers',
                'purl/how-to-build',
                'purl/how-to-parse',
            ],
        },
        {
            type: 'category',
            label: 'Tests',
            link: {
                type: 'doc',
                id: 'purl/tests-folder', // The doc to display
            },
            collapsed: false,
            items: [
                'purl/test-overview',
                'purl/test-suite',
                'purl/test-schema-changes',
            ],
        },
        'purl/purl-types',
        'purl/schemas',
    ],
    vers: [
        'vers/introduction',
        {
            type: 'category',
            label: 'Specification',
            link: {
                type: 'doc',
                id: 'vers/specification-folder', // The doc to display
            },
            collapsed: false,
            items: [
                'vers/specification',
                'vers/how-to-parse',
            ],
        },
        {
            type: 'category',
            label: 'Tests',
            link: {
                type: 'doc',
                id: 'vers/tests-folder', // The doc to display
            },
            collapsed: false,
            items: [
                'vers/test-overview',
                'vers/test-suite',
                'vers/test-schema-changes',
            ],
        },
        'vers/vers-types',
        'vers/schemas',
        'vers/faq',
    ],
    getting_started: [
        {
            type: 'category',
            label: 'Getting Started',
            link: {
                type: 'doc',
                id: 'getting-started/introduction', // The doc to display
            },
            collapsed: false,
            items: [
                'getting-started/toolgrid',
                'getting-started/specgrid',
            ],
        },
    ],
    participate: [
        'participate/contribute',
        'participate/meetings',
        'participate/events',
    ],
    news: [
        'news/community-news',
        'news/spec-news',
    ],
};

export default sidebars;
