PYTHON_VERSION := $(shell python --version 2>&1)
# print_spectrum_help := $(shell print_spectrum -h 2>&1)
varquest_help := $(shell varquest.py -h 2>&1)
varquest_path := $(shell which varquest.py 2>&1)

varquest_dir := $(shell dirname $(varquest_path))

# SHELL := /bin/bash
CWD := $(shell cd -P -- '$(shell dirname -- "$0")' && pwd -P)

# echo CWD
# Install and run example of NRPminer 
# Run test example for NRPminer.
# checking independencies 
.PHONY: all

all:
ifdef PYTHON_VERSION
	@echo "Found Python version $(PYTHON_VERSION)"
else
	@echo "python not in PATH.";	exit 1;
endif
ifdef varquest_help
	@echo "varquest found :"  $(varquest_dir) 
else
	@echo $(varquest_help)
	@echo "varquest. NPDTools binaries must be in PATH.";	exit 1;
endif
	@echo "NRPminer in " $(CWD)
	chmod a+wrx nrpminer.py	
	@echo "Running NRPminer tests ..."; 
	#unzip zipped_test_data.zip
	python nrpminer.py -s $(CWD)/test_data/antismash5_data/B2626_R8.mgf --antismash_resgbk $(CWD)/test_data/antismash5_data/GCA_000721045.1_ASM72104v1_genomic/JOEO01000025.1.region001.gbk --derepdir $(varquest_dir) --maxmod 150 -o $(CWD)/test_data/test_output_antismash5 --threads 12 --pvalue 1.0e-30 --nrpspks_predictions_txt $(CWD)/test_data/antismash5_data/GCA_000721045.1_ASM72104v1_genomic/nrpspks_predictions_txt 
