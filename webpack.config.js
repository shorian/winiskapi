const path = require("path");

module.exports = {
  mode: "development",
  entry: "./winiskapi/static/src/index.js",
  output: {
    path: path.resolve(__dirname, "/winiskapi/static/dist"),
    filename: "bundle.js",
  },
  watch: true,
  watchOptions: {
    ignored: "./node_modules",
  },
  module: {
    rules: [
      {
        test: /\.(scss)$/,
        use: [
          {
            loader: "style-loader",
          },
          {
            loader: "css-loader",
          },
          {
            loader: "postcss-loader",
            options: {
              postcssOptions: {
                plugins: () => {
                  [require("autoprefixer")];
                },
              },
            },
          },
          {
            loader: "sass-loader",
          },
        ],
      },
      {
        test: /\.(js|jsx)$/,
        include: path.resolve(__dirname, "winiskapi/static/src"),
        exclude: /node_modules/,
        use: [
          {
            loader: "babel-loader",
            options: {
              presets: [
                [
                  "@babel/preset-env",
                  {
                    targets: "defaults",
                  },
                ],
                "@babel/preset-react",
              ],
              plugins: ["@babel/plugin-proposal-optional-chaining"],
            },
          },
        ],
      },
    ],
  },
};
