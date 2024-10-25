import { defineConfig } from "vitepress"

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Dooit Extras",
  description: "A collection of items to customize your dooit!",
  base: '/dooit-extras/',
  lastUpdated: true,
  themeConfig: {
    repo: 'dooit-org/dooit-extras',
    docsDir: 'site/docs',
    editLink: {
      pattern: 'https://github.com/dooit-org/dooit-extras/edit/main/site/docs/:path',
      text: 'Edit this page on GitHub'
    },
    nav: [
      { text: "Home", link: "/" },
      { text: "Get Started", link: "/introduction" },
    ],
    socialLinks: [
      { icon: "github", link: "https://github.com/dooit-org/dooit-extras" },
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
          { text: 'Widgets', link: '/introduction/widgets' },
          { text: 'Bars', link: '/introduction/bars' },
        ]
      },
      {
        text: 'Formatters',
        collapsible: true,
        collapsed: true,
        items: [
          { text: 'Description', link: '/formatters/description' },
          { text: 'Due', link: '/formatters/due' },
          { text: 'Status', link: '/formatters/status' },
          { text: 'Recurrence', link: '/formatters/recurrence' },
          { text: 'Urgency', link: '/formatters/urgency' },
        ]
      },

      {
        text: 'Widgets',
        collapsible: true,
        collapsed: true,
        items: [
          { text: 'Clock', link: '/widgets/clock' },
          { text: 'Current Workspace', link: '/widgets/current_workspace' },
          { text: 'Custom', link: '/widgets/custom' },
          { text: 'Date', link: '/widgets/date' },
          { text: 'Mode', link: '/widgets/mode' },
          { text: 'Platform', link: '/widgets/platform' },
          { text: 'Powerline', link: '/widgets/powerline' },
          { text: 'Spacer', link: '/widgets/spacer' },
          { text: 'TextBox', link: '/widgets/text_box' },
          { text: 'Ticker', link: '/widgets/ticker' },
          { text: 'Workspace Progress', link: '/widgets/workspace_progress' },
        ]
      },

      {
        text: 'Bars',
        collapsible: true,
        collapsed: true,
        items: [
          { text: 'Default', link: '/bars/default' },
        ]
      },

    ]
  }
})
