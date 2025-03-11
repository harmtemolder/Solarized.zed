# [Solarized](https://ethanschoonover.com/solarized/) for [Zed](https://zed.dev/)

> Precision colors for machines and people

## Issues

If you have any issues, no matter how small, please open an issue on [GitHub](https://github.com/harmtemolder/Solarized.zed/issues).

## Develop

- (I used `schema.py` to generate a list of properties from `schema.json`, but as long as <https://zed.dev/schema/themes/v0.2.0.json> is used in `solarized.py`, you don't have to repeat this)
  - Note that `accents`, `players` and `syntax` should be a `list`, `list` and `dict` respectively
- Make changes to `solarized.py` as you see fit
- Then run it with `python solarized.py` to generate `themes/solarized.json`
- Don't forget to increment the version number in `extension.toml` before committing
- Then update [the `extensions` repo](https://github.com/zed-industries/extensions) (see [docs](https://zed.dev/docs/extensions/developing-extensions#updating-an-extension))

## Credits

- Based on [Ethan Schoonover's Solarized color palette](https://ethanschoonover.com/solarized/)
- Inspired by Carlo Caione's [NeoSolarized.zed](https://github.com/carlocaione/NeoSolarized.zed), but with coloring closer to the original palette, especially for syntax highlighting
