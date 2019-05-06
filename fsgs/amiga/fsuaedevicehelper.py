import os
import subprocess

from fsbc import settings
from fsgs.option import Option
from .fsuae import FSUAE

try:
    getcwd = os.getcwdu
except AttributeError:
    getcwd = os.getcwd


class FSUAEDeviceHelper(object):
    @classmethod
    def start_with_args(cls, args, **kwargs):
        print("FSUAE.start_with_args:", args)
        exe = cls.find_executable()
        print("current dir (cwd): ", getcwd())
        print("using fs-uae executable:", exe)
        args = [exe] + args
        print(args)
        env = os.environ.copy()
        if settings.get(Option.FAKE_JOYSTICKS):
            try:
                fake_joysticks = int(settings.get(Option.FAKE_JOYSTICKS))
            except ValueError:
                print(
                    "WARNING: fake_joysticks contains invalid value",
                    repr(settings.get(Option.FAKE_JOYSTICKS)),
                )
            else:
                env["FSGS_FAKE_JOYSTICKS"] = str(fake_joysticks)
        FSUAE.add_environment_from_settings(env)
        process = subprocess.Popen(
            args,
            env=env,
            stdin=subprocess.PIPE,
            stderr=subprocess.PIPE,
            **kwargs
        )
        return process

    @classmethod
    def find_executable(cls):
        return FSUAE.find_executable("fs-uae-device-helper")
