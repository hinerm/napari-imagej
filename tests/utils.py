"""
A module containing testing utilities
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from jpype import JImplements, JOverride
from scyjava import JavaClasses

from napari_imagej.java import NijJavaClasses

if TYPE_CHECKING:
    from typing import Dict, List


class JavaClassesTest(NijJavaClasses):
    """
    Here we override JavaClasses to get extra test imports
    """

    @JavaClasses.java_import
    def ArrayImg(self):
        return "net.imglib2.img.array.ArrayImg"

    @JavaClasses.java_import
    def ArrayImgs(self):
        return "net.imglib2.img.array.ArrayImgs"

    @JavaClasses.java_import
    def Axes(self):
        return "net.imagej.axis.Axes"

    @JavaClasses.java_import
    def BoolType(self):
        return "net.imglib2.type.logic.BoolType"

    @JavaClasses.java_import
    def ByteType(self):
        return "net.imglib2.type.numeric.integer.ByteType"

    @JavaClasses.java_import
    def ClassesSearcher(self):
        return "org.scijava.search.classes.ClassesSearcher"

    @JavaClasses.java_import
    def ClassSearchResult(self):
        return "org.scijava.search.classes.ClassSearchResult"

    @JavaClasses.java_import
    def DefaultMutableModuleItem(self):
        return "org.scijava.module.DefaultMutableModuleItem"

    @JavaClasses.java_import
    def DefaultMutableModuleInfo(self):
        return "org.scijava.module.DefaultMutableModuleInfo"

    @JavaClasses.java_import
    def DoubleArray(self):
        return "org.scijava.util.DoubleArray"

    @JavaClasses.java_import
    def EuclideanSpace(self):
        return "net.imglib2.EuclideanSpace"

    @JavaClasses.java_import
    def FloatType(self):
        return "net.imglib2.type.numeric.real.FloatType"

    @JavaClasses.java_import
    def Frame(self):
        return "java.awt.Frame"

    @JavaClasses.java_import
    def IllegalArgumentException(self):
        return "java.lang.IllegalArgumentException"

    @JavaClasses.java_import
    def ImageDisplay(self):
        return "net.imagej.display.ImageDisplay"

    @JavaClasses.java_import
    def IntType(self):
        return "net.imglib2.type.numeric.integer.IntType"

    @JavaClasses.java_import
    def ItemIO(self):
        return "org.scijava.ItemIO"

    @JavaClasses.java_import
    def ItemVisibility(self):
        return "org.scijava.ItemVisibility"

    @JavaClasses.java_import
    def ModuleSearchResult(self):
        return "org.scijava.search.module.ModuleSearchResult"

    @JavaClasses.java_import
    def OpSearchResult(self):
        return "net.imagej.ops.search.OpSearchResult"

    @JavaClasses.java_import
    def ScriptInfo(self):
        return "org.scijava.script.ScriptInfo"

    @JavaClasses.java_import
    def ShortType(self):
        return "net.imglib2.type.numeric.integer.ShortType"

    @JavaClasses.java_import
    def System(self):
        return "java.lang.System"

    @JavaClasses.java_import
    def UnsignedByteType(self):
        return "net.imglib2.type.numeric.integer.UnsignedByteType"

    @JavaClasses.java_import
    def UnsignedShortType(self):
        return "net.imglib2.type.numeric.integer.UnsignedShortType"

    @JavaClasses.java_import
    def UnsignedIntType(self):
        return "net.imglib2.type.numeric.integer.UnsignedIntType"

    @JavaClasses.java_import
    def UnsignedLongType(self):
        return "net.imglib2.type.numeric.integer.UnsignedLongType"

    @JavaClasses.java_import
    def WindowEvent(self):
        return "java.awt.event.WindowEvent"


jc = JavaClassesTest()


@JImplements("org.scijava.search.Searcher", deferred=True)
class DummySearcher:
    """
    Implementation of org.scijava.search.Searcher used for testing
    """

    def __init__(self, title: str):
        self._title = title

    @JOverride
    def search(self, text: str, fuzzy: bool):
        pass

    @JOverride
    def title(self) -> str:
        return self._title

    @JOverride
    def getClass(self):
        return jc.Searcher


class DummySearchEvent:
    """
    A mock of org.scijava.search.search.SearchEvent
    """

    def __init__(self, searcher: "jc.Searcher", results: List["jc.SearchResult"]):
        self._searcher = searcher
        self._results = results

    def searcher(self):
        return self._searcher

    def results(self):
        return self._results


class DummySearchResult(object):
    def __init__(self, info: "jc.ModuleInfo" = None, properties: Dict = {}):
        self._info = info
        self._properties = properties

    def name(self):
        return "This is not a Search Result"

    def info(self):
        return self._info

    def iconPath(self):
        return None

    def getClass(self):
        return None

    def properties(self):
        return self._properties

    def set_properties(self, props: Dict):
        self._properties = props


class DummyModuleInfo:
    """
    A mock of org.scijava.module.ModuleInfo that is created much easier
    Fields can and should be added as needed for tests.
    """

    def __init__(self, title="Dummy Module Info", inputs=[], outputs=[]):
        self._title = title
        self._inputs = inputs
        self._outputs = outputs

    def getTitle(self):
        return self._title

    def outputs(self):
        return self._outputs


class DummyModuleItem:
    """
    A mock of org.scijava.module.ModuleItem that is created much easier
    Fields can and should be added as needed for tests.
    """

    def __init__(
        self,
        name="",
        jtype=None,
        isRequired=True,
        isInput=True,
        isOutput=False,
        default=None,
    ):
        self._name = name
        self._jtype = jtype if jtype is not None else jc.String
        self._isRequired = isRequired
        self._isInput = isInput
        self._isOutput = isOutput
        self._default = default
        self._style = ""

    def getName(self):
        return self._name

    def getType(self):
        return self._jtype

    def isRequired(self):
        return self._isRequired

    def isInput(self):
        return self._isInput

    def isOutput(self):
        return self._isOutput

    def getDefaultValue(self):
        return self._default

    def getMaximumValue(self):
        return self._maximumValue

    def setMaximumValue(self, val):
        self._maximumValue = val

    def getMinimumValue(self):
        return self._minimumValue

    def setMinimumValue(self, val):
        self._minimumValue = val

    def getStepSize(self):
        return self._stepSize

    def setStepSize(self, val):
        self._stepSize = val

    def getLabel(self):
        return self._label

    def setLabel(self, val):
        self._label = val

    def getDescription(self):
        return self._description

    def setDescription(self, val):
        self._description = val

    def getChoices(self):
        return self._choices

    def setChoices(self, val):
        self._choices = val

    def getWidgetStyle(self):
        return self._style

    def setWidgetStyle(self, val):
        self._style = val
