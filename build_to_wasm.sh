#!/usr/bin/env bash

set -e
set -x

emcmake cmake \
    -DCMAKE_BUILD_TYPE=Debug \
    -DCMAKE_CXX_FLAGS_DEBUG="-Wall -Wextra -fexceptions" \
    -DWITH_LLVM=no \
    -DLPYTHON_BUILD_ALL=yes \
    -DLPYTHON_BUILD_TO_WASM=yes \
    -DWITH_STACKTRACE=no \
    -DWITH_LSP=no \
    -DWITH_LFORTRAN_BINARY_MODFILES=no \
    -DCMAKE_PREFIX_PATH="$CMAKE_PREFIX_PATH_LFORTRAN;$CONDA_PREFIX" \
    -DCMAKE_INSTALL_PREFIX=`pwd`/inst \
    .
cmake --build . -j16
