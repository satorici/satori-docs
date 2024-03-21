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
      { text: "Intro", link: "/README.md" },
      { text: "Getting Started", link: "/getting-started/install.md" },
      { text: "Playbooks", link: "/playbooks/language.md" },
      { text: "Execution modes", link: "/modes/modes.md" },
      { text: "Repositories", link: "/repo.md" },
      { text: "Teams", link: "/teams.md" },
    ],

    socialLinks: [{ icon: "github", link: "https://github.com/satorici/satori-cli" }],
  },
});
