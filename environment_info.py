# stan = probabilistic programming language (PPL)
# get a model specification THEN an executable that maps X to samples
# make new environment for bayesian stats course
# conda create --name bays
# conda activate bays

# download stan for course in bays environment
# pip install -e git+https://github.com/stan-dev/cmdstanpy@develop#egg=cmdstanp
# conda install -c conda-forge cmdstan
# git clone https://github.com/stan-dev/cmdstan.git --recursive for updating to the newest version from git

#pip install -q cmdstanpy==1.3.0 downloading so it can talk with python





from pathlib import Path
import shutil
import urllib.request

import cmdstanpy
print(cmdstanpy.__version__)
print(cmdstanpy.cmdstan_path())


from cmdstanpy import CmdStanModel

print("CmdStan:", cmdstanpy.cmdstan_path())


stan_file = Path("/Users/hannahmcnulty/.cmdstan/cmdstan-2.39.0")

model = CmdStanModel(stan_file=str(stan_file))


# stan_dir = Path("/Users/hannahmcnulty/Documents/github/Bayesian Stats/cmdstan/stan")
# print(list(stan_dir.glob("*.stan")))
## this returns [] so there is no stan file yet

# project = Path("/Users/hannahmcnulty/Documents/github/Bayesian Stats")
# print(list(project.rglob("*.stan")))
## check for a stan file in all of it, so far i only have the example one

stan_file = Path(
    "/Users/hannahmcnulty/Documents/github/Bayesian Stats/"
    "src/cmdstanpy/test/data/bernoulli.stan"
)

model = CmdStanModel(stan_file=str(stan_file))




# this is how you load from python to stan
#stan_code = r"""
#data {
#  int N;
#  int K;
#}
#parameters {
#  real rho;
#}
#model {
#  rho ~ beta(1.5, 1.5);
#  K ~ binomial(N, rho);
#}
#"""

#stan_file = Path("/content/globe_toss.stan")
#stan_file.write_text(stan_code)
#print(stan_code)



# SOOO for the globe toss example

#data {
#  int<lower=0> N;
#  int<lower=0, upper=N> K;
#}
#parameters {
#  real<lower=0, upper=1> rho;
#}
#model {
#  rho ~ beta(1.5, 1.5);
#  K ~ binomial(N, rho);
#}
