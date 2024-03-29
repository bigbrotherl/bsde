import numpy as np


class Config(object):
    n_layer = 4
    batch_size = 512
    valid_size = 1024 * 8
    step_boundaries = [2000, 4000]
    num_iterations = 10000
    logging_frequency = 1000
    verbose = True
    y_init_range = [0, 1]


class AllenCahnConfig(Config):
    total_time = 0.3
    num_time_interval = 10
    dim = 100
    lr_values = list(np.array([5e-4, 5e-4]))
    lr_boundaries = [2000]
    num_iterations = 4000
    num_hiddens = [dim, dim + 10, dim + 10, dim]
    y_init_range = [0.3, 0.6]
    
    z_layernum = 10
    z_units = [dim + 20]*z_layernum


class HJBConfig(Config):
    # Y_0 is about 4.5901.
    dim = 100
    total_time = 1.0
    num_time_interval = 10
    lr_boundaries = [400]
    num_iterations = 4000
    lr_values = list(np.array([1e-2, 1e-2]))
    num_hiddens = [dim, dim+10, dim+10, dim]
    y_init_range = [0, 1]
    
    z_layernum = 10
    z_units = [dim + 20]*z_layernum

class EuropeanCallConfig(Config):
    num_iterations = 10000
    dim = 1
    total_time = 1
    num_time_interval = 10
    y_init_range = [6, 12]
    lr_values = list(np.array([1e-3, 1e-3]))
    lr_boundaries = [1000]
    pre_train_num_iteration = 5000
    f_layernum = 20
    z_layernum = 10
    f_units = [dim + 20]*f_layernum
    z_units = [dim + 20]*z_layernum
    ob_num = 82


class PricingOptionConfig(Config):
    dim = 5
    total_time = 0.5
    num_time_interval = 10
    lr_values = list(np.array([5e-3, 5e-3]))
    lr_boundaries = [2000]
    num_iterations = 20000
    
    z_layernum = 10
    z_units = [dim + 20]*z_layernum
    y_init_range = [3, 7]


class PricingDefaultRiskConfig(Config):
    dim = 100
    total_time = 1
    num_time_interval = 40
    lr_values = list(np.array([8e-3, 8e-3]))
    lr_boundaries = [3000]
    num_iterations = 6000
    num_hiddens = [dim, dim+10, dim+10, dim]
    y_init_range = [40, 50]


class BurgesTypeConfig(Config):
    dim = 50
    total_time = 0.2
    num_time_interval = 30
    lr_values = list(np.array([1e-2, 1e-3, 1e-4]))
    lr_boundaries = [15000, 25000]
    num_iterations = 30000
    num_hiddens = [dim, dim+10, dim+10, dim]
    y_init_range = [2, 4]


class QuadraticGradientsConfig(Config):
    dim = 100
    total_time = 1.0
    num_time_interval = 30
    lr_values = list(np.array([5e-3, 5e-3]))
    lr_boundaries = [2000]
    num_iterations = 4000
    num_hiddens = [dim, dim+10, dim+10, dim]
    y_init_range = [2, 4]


class ReactionDiffusionConfig(Config):
    dim = 100
    total_time = 1.0
    num_time_interval = 30
    lr_values = list(np.array([1e-2, 1e-2, 1e-2]))
    lr_boundaries = [8000, 16000]
    num_iterations = 24000
    num_hiddens = [dim, dim+10, dim+10, dim]


def get_config(name):
    try:
        return globals()[name+'Config']
    except KeyError:
        raise KeyError("Config for the required problem not found.")
