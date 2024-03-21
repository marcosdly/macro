import { defineConfig } from "vite";
import preact from "@preact/preset-vite";

export default defineConfig({
  plugins: [preact()],
  // assetsInclude: "./vendor/**/*",
  server: {
    open: true,
  },
  build: {
    assetsDir: "",
    copyPublicDir: true,
  },
});
