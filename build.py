from distutils.core import Extension
from distutils.command.build_ext import build_ext
from distutils.errors import CompileError
from subprocess import call


ext_modules = [
    Extension(
        "promqlpy._libpromql",
        include_dirs=["go/*"],
        sources=["libpromql.go"],
    ),
]


class BuildFailed(Exception):
    pass


class GoExtBuilder(build_ext):
    def build_extension(self, ext):
        ext_path = self.get_ext_fullpath(ext.name)
        cmd = ["go", "build", "-buildmode=c-shared", "-o", ext_path]
        cmd += ext.sources
        out = call(cmd, cwd="./go")

        if out != 0:
            raise CompileError("Go build failed")


def build(setup_kwargs):
    """
    This function is mandatory in order to build the extensions.
    """
    setup_kwargs.update(
        {"ext_modules": ext_modules, "cmdclass": {"build_ext": GoExtBuilder}}
    )
