const path = require("path");

module.exports = {
  mode: "development",
  entry: "./src",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "bundle.js",
  },
  watch: true,
  watchOptions: {
    ignored: "./node_modules",
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        include: path.resolve(__dirname, "src"),
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
