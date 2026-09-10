
import cmdstanpy
from cmdstanpy import CmdStanModel

model = CmdStanModel(stan_file=str(stan_file))


from pathlib import Path

stan_dir = Path("/Users/hannahmcnulty/Documents/github/Bayesian Stats/cmdstan/stan")

print(list(stan_dir.glob("*.stan")))


# Testing sampling
model = CmdStanModel(stan_file=str(stan_file))

fit = model.sample(
    data={"N": 7, "K": 3},
    chains=2,
    parallel_chains=2,
    iter_warmup=250,
    iter_sampling=250,
    seed=6300,
    show_progress=False,
)

print("Stan screen test passed.")