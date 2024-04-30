# install python version 3.7 

!sudo apt-get install python3.8

!sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1

!sudo update-alternatives --config python3

!sudo apt install python3-pip

!sudo apt-get install python3.7-distutils

# Check version pip and python

!pip --version
!python --version

# Upgrade setuptools and pip
!pip install --upgrade pip setuptools

!pip debug --verbose

# Load nanopolish 
!git clone --recursive https://github.com/jts/nanopolish.git
!pip install -r requirements_nanopolish.txt
!cd nanopolish
!make
!export PATH=$PATH:/path/to/nanopolish

# Install Whatshap
!pip download --no-deps whatshap
!pip install -r requirements_whatshap.txt
!pip install git+https://github.com/whatshap/whatshap
!whatshap --version

# Install pycoMeth
!pip download --no-deps pycoMeth
!pip install -r requirements_pycometh.txt
!pip install pycoMeth
!pycoMeth --version
!pycoMeth CpG_Aggregate --help

# Basic usage of pycometh 
! pycoMeth CpG_Aggregate \
    -i ./data/nanopolish_sample_1.tsv \
    -f ./data/ref.fa \
    -b ./results/CpG_Aggregate_sample_1_CLI.bed \
    -t ./results/CpG_Aggregate_sample_1_CLI.tsv \
    -s sample_1 \
    --progress

! head ./results/CpG_Aggregate_sample_1_CLI.bed
! head ./results/CpG_Aggregate_sample_1_CLI.tsv

! pycoMeth Interval_Aggregate\
    -i ./data/CpG_Aggregate_sample_1.tsv \
    -f ./data/ref.fa \
    -b ./results/Interval_Aggregate_sample_1_CLI.bed \
    -t ./results/Interval_Aggregate_sample_1_CLI.tsv \
    --interval_size 500 \
    --min_cpg_per_interval 5 \
    -s sample_1 \
    --progress

!head ./results/Interval_Aggregate_sample_1_CLI.bed
!head ./results/Interval_Aggregate_sample_1_CLI.tsv
