import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react-swc';
import path from 'path';

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  build: {
    rollupOptions: {
      input: {
        main: path.resolve(__dirname, 'index.html'),
        checkout: path.resolve(__dirname, 'checkout.html'),
        'checkout-premium': path.resolve(__dirname, 'checkout-premium.html'),
        'checkout-demo': path.resolve(__dirname, 'checkout-demo.html'),
      },
    },
  },
});
