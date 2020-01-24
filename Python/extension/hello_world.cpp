#include <Python.h>
#include <iostream>

static PyObject *method_hello(PyObject *self, PyObject *args) {
     char *str = NULL;
     int bytes_copied = -1;

     /* Parse arguments */
     if(!PyArg_ParseTuple(args, "s", &str)) {
         return NULL;
     }
 
     std::cout << "Hello World" << std::endl;
 
     return PyLong_FromLong(0);
 }

static PyMethodDef FExtMethods[] = {
    // pe: python extension
    {"pe_hello", method_hello, METH_VARARGS, "Python interface for C++ function which prints Hello World"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef fpemodule = {
    PyModuleDef_HEAD_INIT,
    "fei_pe",
    "Python interface for fei's C++ extension library functions",
    -1,
    FExtMethods};

PyMODINIT_FUNC PyInit_fei_pe(void) {
    return PyModule_Create(&fpemodule);
}
