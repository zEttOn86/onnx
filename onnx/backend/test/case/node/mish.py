# SPDX-License-Identifier: Apache-2.0

import numpy as np  # type: ignore

import onnx
from ..base import Base
from . import expect


class Mish(Base):

    @staticmethod
    def export() -> None:
        node = onnx.helper.make_node(
            'Mish',
            inputs=['X'],
            outputs=['Y']
        )

        input_data = np.linspace(-10, 10, 10000, dtype=np.float32)

        # Calculate expected output data
        expected_output = input_data * np.tanh(np.log1p(np.exp(input_data)))

        expect(node, inputs=[input_data], outputs=[expected_output],
               name='test_mish')
