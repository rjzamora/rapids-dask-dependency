# Copyright (c) 2025, NVIDIA CORPORATION.
import sys

from rapids_dask_dependency.loaders import make_vendored_loader

load_module = make_vendored_loader(__name__)
