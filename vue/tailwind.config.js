module.exports = {
  mode: 'JIT',
  prefix: 'tw-',
  content: ['./index.html','./src/**/*.{js,ts,vue}'],
  plugins: [require('daisyui')],
  daisyui: {
    theme: true
  },
  purge: {
    enabled: true,
    content: ['./src/**/*.{js,ts,vue}']
  }
}
