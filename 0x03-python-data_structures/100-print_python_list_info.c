#include <Python.h>
#include <stdio.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p);

/**
 * print_python_list_info - Get information about the len and data type
 * @p: Contains the information of the python objects
 *
 */
void print_python_list_info(PyObject *p)
{
	PyObject *type = NULL;
	int len = (int)PyList_Size(p);
	int i;

	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", (int)((PyListObject *)(p))->allocated);

	for (i = 0; i < len; ++i)
	{
		type = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, (char *)Py_TYPE(type)->tp_name);
	}
}
