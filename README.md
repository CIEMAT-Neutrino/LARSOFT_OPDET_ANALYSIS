# LARSOFT_OPDET_ANALYSIS

Repository used to analyse ideal, raw and deco optical wvfs from larsoft.

Currently the notebook expects raw data (output of the digitizer module) and deconvolved data (output of the deconvolution module):

- The raw data should be a file named opdetraw_hist.root and contain the folders opdigi and opdigiana.
- The deco data should be two files named deconv_*_hist.root and contain the folder opdecoana. Remember to change name and label in the import section of the notebook accordingly.

## Installation

The repository is meant to be used as an extension to larsoft's analysis modules. To install it, follow the instructions below:

```bash
pip install -r requirements.txt
```

## Usage

- Currently the notebooks expect 8 files:
  - 2 raw digitized wvfs (one for the ideal SiPM response and one for the real XArapuca response) + 2 deconvolved wvfs.
  - 4 files containing the ophitfinder output for the 4 different wvfs.
- To produce the files, follow the instructions below:
    1. Run the digitizer module on the raw data. This will produce the file opdetraw_hist.root.
    2. Run the deconvolution module on the opdetraw_gen.root data. This will produce the files deconv_*_hist.root.
    3. Run the ophitfinder module on the opdetraw_gen.root and deconv_gen.root data. This will produce the file ophit_hist.root files.

The repository contains a jupyter notebook that can be used to analyse the data. To run it, simply type:

```bash
jupyter notebook
```

There are additional notebooks that can be used to visualize the tamples and make wvf simulations.

Include a gif of the notebook here.

## TODO

- [ ] Add a gif of the notebook to the README.md document.
- [ ] Make the wvfs input more flexible to include any given number of data files.
- [ ] Add a notebook to simulate wvfs.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors

- **Sergio Manthey Corchado** - *Initial work* - [mantheys](https://github.com/mantheys)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.