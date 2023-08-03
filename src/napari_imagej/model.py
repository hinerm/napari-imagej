from jpype import JImplements, JOverride

from napari_imagej.java import init_ij, jc


class NapariImageJ:
    """
    An object offering a central access point to napari-imagej's core business logic.
    """

    def __init__(self):
        self._ij = None
        self._repl = None
        self._repl_callbacks = []

    @property
    def ij(self):
        if self._ij is None:
            self._ij = init_ij()
        return self._ij

    @property
    def repl(self) -> "jc.ScriptREPL":
        if self._repl is None:
            ctx = self.ij.context()
            model = self

            @JImplements("java.util.function.Consumer")
            class REPLOutput:
                @JOverride
                def accept(self, t):
                    s = str(t)
                    for callback in model._repl_callbacks:
                        callback(s)

            self._repl = jc.ScriptREPL(ctx, "jython", REPLOutput())
            self._repl.lang("jython")
        return self._repl

    def add_repl_callback(self, repl_callback) -> None:
        self._repl_callbacks.append(repl_callback)
