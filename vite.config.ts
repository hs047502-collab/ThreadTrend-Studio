import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { fileURLToPath, URL } from 'node:url'

export default defineConfig({
  // Absolute base = clean URLs and correct asset paths on deep routes when
  // deployed at a domain root. The offline single-file build inlines everything,
  // so it does not depend on this setting.
  base: '/',
  plugins: [react()],
  resolve: { alias: { '@': fileURLToPath(new URL('./src', import.meta.url)) } },
  server: { host: '0.0.0.0', port: 3000, strictPort: true, allowedHosts: true },
  preview: { host: '0.0.0.0', port: 3000, strictPort: true, allowedHosts: true },
  build: { outDir: 'dist', sourcemap: false },
})
