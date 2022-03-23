'use strict'

const path = require('path')
const { babel } = require('@rollup/plugin-babel')
const { nodeResolve } = require('@rollup/plugin-node-resolve')
const replace = require('@rollup/plugin-replace')
const banner = require('./banner.js')

const BUNDLE = process.env.BUNDLE === 'true'
const ESM = process.env.ESM === 'true'

let fileDest = `bootstrap-carousel${ESM ? '.esm' : ''}`
const external = ['@popperjs/core']
const plugins = [
  replace({
    include: ['node_modules/bootstrap/js/src/carousel.js'],
    preventAssignment: true,
    values: {
      'CLASS_NAME_CAROUSEL': '"scbs-carousel"',
      'CLASS_NAME_ACTIVE': '"scbs-active"',
      'CLASS_NAME_SLIDE': '"scbs-slide"',
      'CLASS_NAME_END': '"scbs-carousel-item-end"',
      'CLASS_NAME_START': '"scbs-carousel-item-start"',
      'CLASS_NAME_NEXT': '"scbs-carousel-item-next"',
      'CLASS_NAME_PREV': '"scbs-carousel-item-prev"',
      'CLASS_NAME_POINTER_EVENT': '"scbs-pointer-event"',
      'SELECTOR_ACTIVE': '".scbs-active"',
      'SELECTOR_ACTIVE_ITEM': '".scbs-active.scbs-carousel-item"',
      'SELECTOR_ITEM': '".scbs-carousel-item"',
      'SELECTOR_ITEM_IMG': '".scbs-carousel-item img"',
      'SELECTOR_NEXT_PREV': '".scbs-carousel-item-next, .scbs-carousel-item-prev"',
      'SELECTOR_INDICATORS': '".scbs-carousel-indicators"',
    }
  }),
  babel({
    // Only transpile our source code
    exclude: /node_modules\/(?!bootstrap\/).*/,
    // Include the helpers in the bundle, at most one copy of each
    babelHelpers: 'bundled'
  })
]
const globals = {
  '@popperjs/core': 'Popper'
}

if (BUNDLE) {
  fileDest += '.bundle'
  // Remove last entry in external array to bundle Popper
  external.pop()
  delete globals['@popperjs/core']
  plugins.push(
    replace({
      'process.env.NODE_ENV': '"production"',
      preventAssignment: true
    }),
    nodeResolve()
  )
}

const rollupConfig = {
  input: path.resolve(__dirname, `../js/index.${ESM ? 'esm' : 'umd'}.js`),
  output: {
    banner,
    file: path.resolve(__dirname, `../dist/js/${fileDest}.js`),
    format: ESM ? 'esm' : 'umd',
    globals,
    generatedCode: 'es2015'
  },
  external,
  plugins
}

if (!ESM) {
  rollupConfig.output.name = 'bootstrap-carousel'
}

module.exports = rollupConfig
