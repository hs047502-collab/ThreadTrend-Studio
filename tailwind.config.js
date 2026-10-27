/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        ink: '#111111',
        paper: '#FFFFFF',
        cream: '#F7F5F0',
        beige: '#D8C3A5',
        stone: '#666666',
        line: '#E6E1D8',
        soft: '#EFEAE1',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'sans-serif'],
        display: ['Iowan Old Style', 'Palatino Linotype', 'Palatino', 'Georgia', 'Times New Roman', 'serif'],
      },
      maxWidth: { wrap: '1240px' },
      boxShadow: {
        card: '0 2px 14px rgba(17,17,17,.05)',
        soft: '0 16px 44px rgba(17,17,17,.08)',
      },
      transitionTimingFunction: { smooth: 'cubic-bezier(.22,.61,.36,1)' },
    },
  },
  plugins: [],
}
