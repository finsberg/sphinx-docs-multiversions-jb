# Build documentation using multiple versions of a pacakage.

This repo is a playground for experimenting with building Sphinx documentation
for multiple versions of a package.


It uses the the [version-switcher](https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/version-dropdown.html) feature of the
[pydata-sphinx-theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/) to provide a version
selector in the documentation.


To build the documentation, a GitHub Actions workflow is used. The workflow builds the
documentation for multiple versions of a dummy package, and uploads the built documentation
as a GitHub Pages site. The devlopment version of the documentation is built from the `main` branch, and placed in the root of the site.
Other versions are built from Git tags, and placed in subdirectories named after the tag.
All the page artifacts are then combined into a single GitHub Pages site, with a version switcher
to select between the different versions.

The version switcher is configured to use a JSON file hosted on GitHub Pages to
provide the version information. The JSON file is manually created and committed to the
repository in the `_static` directory of the documentation source.



## License
MIT
