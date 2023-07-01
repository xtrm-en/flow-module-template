# -*- coding: utf-8 -*-

from argparse import ArgumentParser, Namespace
from fart.commands import create
from fart.utils import success


def __exec(_: ArgumentParser, __: Namespace) -> None:
    success("Created your first subcommand!")


create("hello", "your first subcommand", lambda _: None, __exec)
