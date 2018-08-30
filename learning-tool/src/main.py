#!/usr/bin/env python
# -*- coding: utf-8 -*-
from experiment import Experiment


def reload_all_modules():
    from importlib import reload

    import experiment
    import data_loader
    import trainer

    reload(experiment)
    reload(data_loader)
    reload(trainer)


def main():
    exp = Experiment()
    exp.run()
    return


if __name__ == "__main__":
    reload_all_modules()
    main()
