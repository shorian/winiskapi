const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  mode: "development",
  entry: "./winiskapi/static/src/index.js",
  output: {
    path: path.resolve(__dirname + "/winiskapi/static/dist"),
    filename: "bundle.js",
  },
  watch: true,
  watchOptions: {
    ignored: "./node_modules",
  },
  plugins: [new MiniCssExtractPlugin()],
  module: {
    rules: [
      {
        test: /\.(scss)$/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader,
          },
          {
            loader: "css-loader",
            options: {
              sourceMap: false,
            },
          },
          {
            loader: "postcss-loader",
            options: {
              sourceMap: false,
              postcssOptions: {
                plugins: () => {
                  [require("autoprefixer")];
                },
              },
            },
          },
          {
            loader: "sass-loader",
            options: {
              sourceMap: false,
            },
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
