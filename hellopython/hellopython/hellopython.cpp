// hellopython.cpp : ���� DLL Ӧ�ó���ĵ���������
//

#include "stdafx.h"

#define BOOST_PYTHON_STATIC_LIB
#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
#include <boost/python.hpp>


char const* greet() {
	return "hello world";
}

BOOST_PYTHON_MODULE(hello_ext) {
	using namespace boost::python;
	def("greet", greet);
}

