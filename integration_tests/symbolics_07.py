from lpython import ccall, CPtr
import os

@ccall(header="symengine/cwrapper.h", c_shared_lib="symengine", c_shared_lib_path=f"{os.environ['CONDA_PREFIX']}/lib")
def basic_new_heap() -> CPtr:
    pass

@ccall(header="symengine/cwrapper.h", c_shared_lib="symengine", c_shared_lib_path=f"{os.environ['CONDA_PREFIX']}/lib")
def basic_const_pi(x: CPtr) -> None:
    pass

@ccall(header="symengine/cwrapper.h", c_shared_lib="symengine", c_shared_lib_path=f"{os.environ['CONDA_PREFIX']}/lib")
def basic_str(x: CPtr) -> str:
    pass

def main0():
    x: CPtr = basic_new_heap()
    basic_const_pi(x)
    s: str = basic_str(x)
    print(s)
    assert s == "pi"

main0()
