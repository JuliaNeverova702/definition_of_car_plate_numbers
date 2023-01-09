#define PY_SSIZE_T_CLEAN
#include </usr/include/python3.10/Python.h> // use your version of python

void python(char *path) {
    Py_Initialize();

    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('./modules')");
    PyRun_SimpleString("import detect");

    PyRun_SimpleString("detect.read_jpg('./dataset')");
    
    Py_Finalize();
}


void main(int argc, char *argv[]) {
    char *path = argv[1];

    python(path);
}


