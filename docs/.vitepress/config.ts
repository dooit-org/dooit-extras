import { defineConfig } from "vitepress"

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Dooit Bar Utils",
  description: "Bar utils for Dooit",
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
    }
  }
})
