# Get Python six functionality:
from __future__ import \
    absolute_import, print_function, division, unicode_literals


###############################################################################
###############################################################################
###############################################################################


import pytest


from innvestigate.legacy.utils.tests import dryrun

from innvestigate.analyzer import BaselineGradient
from innvestigate.analyzer import Gradient


###############################################################################
###############################################################################
###############################################################################


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__BasicGraphReversal():

    def method1(model):
        return BaselineGradient(model)

    def method2(model):
        return Gradient(model)

    dryrun.test_equal_analyzer(method1,
                               method2,
                               "trivia.*:mnist.log_reg")


@pytest.mark.precommit
def test_precommit__BasicGraphReversal():

    def method1(model):
        return BaselineGradient(model)

    def method2(model):
        return Gradient(model)

    dryrun.test_equal_analyzer(method1,
                               method2,
                               "mnist.*")


# @pytest.mark.fast
# @pytest.mark.precommit
# def test_fast__ContainerGraphReversal():

#     def method1(model):
#         return Gradient(model)

#     def method2(model):
#         Create container execution
#         model = keras.models.Model(inputs=model.inputs,
#                                    outputs=model(model.inputs))
#         return Gradient(model)

#     dryrun.test_equal_analyzer(method1,
#                                method2,
#                                "trivia.*:mnist.log_reg")


# @pytest.mark.precommit
# def test_precommit__ContainerGraphReversal():

#     def method1(model):
#         return Gradient(model)

#     def method2(model):
#         Create container execution
#         model = keras.models.Model(inputs=model.inputs,
#                                    outputs=model(model.inputs))
#         return Gradient(model)

#     dryrun.test_equal_analyzer(method1,
#                                method2,
#                                "mnist.*")


###############################################################################
###############################################################################
###############################################################################


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__AnalyzerNetworkBase_neuron_selection_max():

    def method(model):
        return Gradient(model, neuron_selection_mode="max_activation")

    dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.precommit
def test_precommit__AnalyzerNetworkBase_neuron_selection_max():

    def method(model):
        return Gradient(model, neuron_selection_mode="max_activation")

    dryrun.test_analyzer(method, "mnist.*")


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__AnalyzerNetworkBase_neuron_selection_index():

    class CustomAnalyzer(Gradient):

        def analyze(self, X):
            index = 0
            return super(CustomAnalyzer, self).analyze(X, index)

    def method(model):
        return CustomAnalyzer(model, neuron_selection_mode="index")

    dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.precommit
def test_precommit__AnalyzerNetworkBase_neuron_selection_index():

    class CustomAnalyzer(Gradient):

        def analyze(self, X):
            index = 3
            return super(CustomAnalyzer, self).analyze(X, index)

    def method(model):
        return CustomAnalyzer(model, neuron_selection_mode="index")

    dryrun.test_analyzer(method, "mnist.*")
