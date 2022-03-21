'use strict'

const prefixer = require('postcss-prefix-selector')
const autoprefixer = require('autoprefixer')
const rtlcss = require('rtlcss')

module.exports = ctx => {
  return {
    map: ctx.file.dirname.includes('examples') ?
      false :
      {
        inline: false,
        annotation: true,
        sourcesContent: true
      },
    plugins: [
      prefixer({
        prefix: 'scbs-',
        transform: function (prefix, selector) {
          let newSelector = ''
          for (let part of selector.split(/(?=[.])/g)) {
            if (part.startsWith('.')) part = '.' + prefix + part.substring(1)
            newSelector += part
          }
          return newSelector
        },
      }),
      autoprefixer({
        cascade: false
      }),
      ctx.env === 'RTL' ? rtlcss() : false,
    ]
  }
}
