import { defineConfig } from "vitepress"

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Dooit Bar Utils",
  description: "Bar utils for Dooit",
  base: '/dooit-bar-utils/',
  themeConfig: {
    nav: [
      { text: "Home", link: "/" },
      { text: "Widgets", link: "/widgets" },
      { text: "Bars", link: "/bars" },
    ],
    socialLinks: [
      { icon: "github", link: "https://github.com/dooit-org/dooit-bar-utils" },
      { icon: "discord", link: "https://discord.com/invite/WA2ER9MBWa" },
      { icon: "twitter", link: "https://twitter.com/kraanzu" },
    ],
    search: {
      provider: "local"
    },
    sidebar: [
      {
        text: 'Getting Started',
        items: [
          { text: 'Introduction', link: '/introduction' },
          { text: 'Installation', link: '/introduction/installation' },
        ]
      },

      {
        text: 'Built-in Widgets',
        items: [
          { text: 'Introduction', link: '/widgets' },
          { text: 'Mode', link: '/widgets/mode' },
          { text: 'Workspace Progress', link: '/widgets/workspace_progress' },
        ]
      },

      {
        text: 'Built-in Bars',
        items: [
          { text: 'Introduction', link: '/bars' },
        ]
      },

    ]
  }
})
