'use strict'
const path = require('path')
function resolve(dir) {
    return path.join(__dirname, dir)
}
module.exports = {
    publicPath: '/',
    outputDir: 'dist',
    assetsDir: 'static',
    // lintOnSave: process.env.NODE_ENV === 'development',
    lintOnSave: true,
    productionSourceMap: false,
    devServer: {
        port: 8080,
        open: false,
        overlay: {
            warnings: false,
            errors: true
        },
    },
    configureWebpack: {
        // provide the app's title in webpack's name field, so that
        // it can be accessed in index.html to inject the correct title.
            name: 'dogs-web',
            resolve: {
                alias: {
                    '@': resolve('src'),
                }
            }
        },
}