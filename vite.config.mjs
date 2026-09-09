import { defineConfig } from "vite";

// Preview the exact Jekyll output; production continues to use GitHub Pages.
export default defineConfig({
  root: "_site",
  appType: "mpa",
  server: {
    host: "0.0.0.0",
    allowedHosts: ["terminal.local"],
  },
});
