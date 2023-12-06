# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(((((((((((#######%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(//////(//////((((((########%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#/***/***/*//////*///(((((((((#####%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%#**/***,,,,,,,******///(((((((((((#(#####%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%#/****,*,.....,,,,,,,,,,*///////(/(((((#####(##%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%##**,*,........,.,......*,**********///(((#####(###%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%##(*,,,.    ..,.,**,,,,,,,,*,*/////**//(((((####(((#%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%##/,,,.., ...,,,,,,,,,,,*********/////((/(((####((((%%%%%%
# %%%%%%%%%%%%%%#%########/,,,..   ....,,,,,,,,,,********///(((((#####%%#(((##%%%%
# %%%%%%%%%%%%############(,,..........,,,,,,,,,,,******////(((((####%%%#(((#####%
# %%%%%%%%#%%%#############,,,.......,,,,,,,,,,,********////((((###%%#%%#(((#####%
# %%%%####################(,,,,,,,,,,,,,,,,,,,,,,****////////(((####%%%%%#########
# %%%###################(*,,,,,..,,,,,,,,,,,,,,,,,***/////*///((((###%%%%#########
# %%####################,,,.,,,.,,,****,***************//*////((((####%%%#########
# ######################,*,..,,,,,********,***///(///****//((((#####%%%%%%########
# ######################,,,**.,,,***,,**/(((#(#((((/(*,**/#&%##%%#((##%%#&########
# ######################,***..,,****,,,***,,,*/((((/****/(%&%%######%&%%%&########
# ######################(,*,,/,*****,,,*,*//*/*///******/(%%%%#####%%%%%%%########
# ########################,,,,,*****,,,,,,,*************/(%%%########%%%%#########
# #########################/,,******,,,,,,,,,**///****,*/(#%&%#((((###%%##########
# ###########################*******,***,,,*/(#(*****,,*//(%%%%#(((##%%###########
# ###########################******,,,,,*/(*/***********//(%%%%##((##%%###########
# ########################&@&*******,,,*/(//////*****/((((#%%%%####(#%############
# ######################&&@@%*,******,,,**(/***/(,*,**((##%&&&%#((/(#%############
# ####################&%&%@@/*,,*****,*****/*******((((((##%%%##(/(#%#############
# ##################&&&&&@@&/***,*******************///((###%%####%###############
# ################&&%&&&&&@&/*,*,,**********,*******///(((#####%%%################
# ##############%@%%&&&&&&&@#*****,************,*****//(((####%###(###############
# ############&%#%&&&&&&&@&@&/,**************/*******////((#%%#(##(###############
# ########%@@@&&@&#&@#(%&%#&&%*,*****//******/////((((/((#%&@@@&##((##############
# ###%@&@@%&%&%%@&&%@@%&%&#%&&#***********,****////((###%@@@@@@@@@@@@#############
# &&&%%%&%&%%@@&&&&@&&&&%%%&%%%#/*****************//((#%@@@@@@@@&@@@@@@@@@&#######

import re
from pathlib import Path
from typing import Tuple, Callable

paragraphs = lambda t: t.split('\n\n')
lines = str.splitlines


def mapt(function: Callable, *sequences) -> tuple:
    return tuple(map(function, *sequences))


def mapl(function: Callable, *sequences) -> list:
    return list(map(function, *sequences))


def ints(text: str) -> Tuple[int]:
    """A tuple of all the integers in text, ignoring non-number characters."""
    return mapt(int, re.findall(r'-?[0-9]+', text))


txt = Path('./input.txt').read_text()
seeds, *nums = paragraphs(txt)
seeds = ints(seeds)

nums = mapl(lines, nums)
nums = mapl(lambda l: l[1:], nums)
maps = mapl(lambda x: mapl(ints, x), nums)

# mapt(ints,nums.split('\n'))
