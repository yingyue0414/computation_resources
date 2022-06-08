#! /bin/bash
pip install nbconvert
echo Enter path:
read var_path
find $var_path -name '*.ipynb' -exec jupyter nbconvert --to script {} \;
find $var_path -name '*.ipynb' -exec rm -f {} \;
