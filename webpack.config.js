const path = require('path');

module.exports = {
    entry: {
        index: './src/index.js',
        login: './src/login.js',
    },
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, 'app/static/js')
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env', '@babel/preset-react']
                    }
                }
            }
        ]
    },
    resolve: {
        extensions: ['.js', '.jsx'],
    },
};