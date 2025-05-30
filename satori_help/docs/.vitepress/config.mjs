import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
    title: "Satori CI Documentation",
    description:
        "Satori CI is an Automated Testing platform that asserts the behavior of command executions. Testing software and systems using our Playbook marketplace or by defining your own playbooks",
    sitemap: { hostname: "https://docs.satori.ci" },
    themeConfig: {
        // https://vitepress.dev/reference/default-theme-config
        logo: "https://satori.ci/img/logo.svg",
        search: { provider: "local" },
        nav: [
            { text: 'Plans', link: 'https://satori.ci/#plans' },
            { text: 'Public', link: 'https://satori.ci/public' },
            { text: 'Playbooks', link: 'https://satori.ci/playbooks' }
        ],
        sidebar: [
            { text: "Intro", link: "/README" },
            {
                text: "Getting Started",
                link: "/getting-started/install",
                items: [
                    {
                        text: "Installation",
                        link: "/getting-started/install",
                    },
                    {
                        text: "Polyglot Hello World Test",
                        link: "/getting-started/hello_world",
                    },
                    {
                        text: "Satori Playbooks",
                        link: "/getting-started/playbooks",
                    },
                    {
                        text: "Results",
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
                            { text: "GitHub Application", link: "/modes/ci/github" },
                            { text: "GitLab", link: "/modes/ci/gitlab" },
                            { text: "Jenkins", link: "/modes/ci/jenkins" },
                        ],
                    },
                    { text: "Monitor", link: "/modes/monitor" },
                    { text: "Scan", link: "/modes/scan" },
                    { text: "Shards", link: "/modes/shards" },
                ],
            },
            { text: "Repositories", link: "/repo" },
            {
                text: "Notifications",
                link: "/notifications",
                items: [
                    { text: "Slack", link: "/notifications#slack" },
                    { text: "Discord", link: "/notifications#discord" },
                    { text: "Email", link: "/notifications#email" },
                    { text: "Telegram", link: "/notifications#telegram" },
                    { text: "Datadog", link: "/notifications#datadog" },
                ],
            },
            { text: "Teams", link: "/teams" },
            { text: "Cheatsheet", link: "/cheatsheet" },
        ],

        socialLinks: [
            { icon: "github", link: "https://github.com/satorici/satori-cli" },
        ],
    },
});
