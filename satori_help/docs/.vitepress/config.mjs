import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
    title: "Satori CI Documentation",
    description:
        "Satori CI is an Automated Testing platform that asserts the behavior of command executions. Testing software and systems using our Playbook marketplace or by defining your own playbooks",
    sitemap: { hostname: "https://docs.satori.ci" },
    themeConfig: {
        // https://vitepress.dev/reference/default-theme-config
        search: { provider: "local" },
        nav: [],
        sidebar: [
            { text: "Intro", link: "/README" },
            {
                text: "Getting Started",
                link: "/getting-started/install",
                items: [
                    { text: "Installation", link: "/getting-started/install" },
                    {
                        text: "What are Satori Playbooks?",
                        link: "/getting-started/playbooks",
                    },
                    {
                        text: "Examine the results",
                        link: "/getting-started/execution-data",
                    },
                ],
            },
            {
                text: "Playbooks",
                link: "/playbooks/language",
                items: [
                    { text: "Executions", link: "/playbooks/execution" },
                    { text: "Asserts", link: "/playbooks/asserts" },
                    { text: "Inputs", link: "/playbooks/inputs" },
                    { text: "Settings", link: "/playbooks/settings" },
                ],
            },
            {
                text: "Execution modes",
                link: "/modes/modes",
                items: [
                    { text: "Run", link: "/modes/run" },
                    {
                        text: "CI",
                        items: [
                            { text: "GitHub", link: "/modes/ci/github" },
                            { text: "GitHub Action", link: "/modes/ci/action" },
                            { text: "GitLab", link: "/modes/ci/gitlab" },
                            { text: "Jenkins", link: "/modes/ci/jenkins" },
                        ],
                    },
                    { text: "Monitor", link: "/modes/monitor" },
                    { text: "Scan", link: "/modes/scan" },
                ],
            },
            { text: "Repositories", link: "/repo" },
            { text: "Teams", link: "/teams" },
        ],

        socialLinks: [
            { icon: "github", link: "https://github.com/satorici/satori-cli" },
        ],
    },
});
