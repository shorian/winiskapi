const path = require('path');

module.exports = {
    mode: "development",
    entry: "winiskapi/static/src",
    output: {
        path:path.resolve(__dirname, "winiskapi/static/dist"),
        filename: "bundle.js"
    },
    watch: true,
    watchOptions: {
        ignored: "./node_modules"
    },
    module: {
        rules: [
            {
                test: /\.(jsx|js)$/,
                include: path.resolve(__dirname, 'src'),
                exclude: /node_modules/,
                use: [{
                    loader: 'babel-loader',
                    options: {
                        presets: [
                            ['@babel/preset-env', {
                                "targets": "defaults"
                            }],
                            '@babel/preset-react'
                        ]
                    }
                }]
            }
        ]
    }
}