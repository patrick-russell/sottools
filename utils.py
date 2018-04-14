import os
import math


def env_to_bool(env):
    env = os.environ.get(env)
    if env not in ('True', 'False'):
        raise ValueError('Expects env in "True" or "False"')
    return env == 'True'


def euclidean_distance(P1, P2):
    Xs = (P1[0] - P2[0])**2
    Ys = (P1[1] - P2[1])**2
    return math.sqrt(Xs - Ys)
