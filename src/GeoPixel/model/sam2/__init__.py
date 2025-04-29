# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import sys
import os
from hydra import initialize_config_module
from hydra.core.global_hydra import GlobalHydra

from GeoPixel.model import sam2_configs

if GlobalHydra.instance().is_initialized():
    GlobalHydra.instance().clear()

config_dir = os.path.dirname(sam2_configs.__file__)

initialize_config_module(config_dir, version_base="1.2")
