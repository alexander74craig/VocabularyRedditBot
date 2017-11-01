
#include <pybind11/pybind11.h>
#include <pybind11/stl_bind.h>

// stringtrie.h code can be found at https://github.com/lcsfrey/Data_Structures
#include "stringtrie.h"

namespace py = pybind11;

PYBIND11_MAKE_OPAQUE(std::vector<std::string>);

// creates python module that can be imported with "import py_stringtrie"
PYBIND11_MODULE(py_stringtrie, trie) {
  py::bind_vector<std::vector<std::string>>(trie, "StringVector");

  py::class_<StringTrie>(trie, "StringTrie")
     .def(py::init<>())
     .def("addWord", &StringTrie::addWord, "Add word to trie")
     .def("remove", &StringTrie::remove, "Remove word from trie")
     .def("contains", &StringTrie::contains, "Returns true if word is in trie")
     .def("removeAllWithPrefix", &StringTrie::removeAllWithPrefix, "Remove all words with prefix")
     .def("resetTrie", &StringTrie::resetTrie, "Remove all words from trie")
     .def("getNumberUniqueWords", &StringTrie::getNumberUniqueWords, "Get number of unique words")
     .def("getNumberTotalWords", &StringTrie::getNumberTotalWords, "Get number of total words")
     .def("printAll", &StringTrie::printAll, "Print all words")
     .def("printAllByOccurences", &StringTrie::printAllByOccurences, "Print all words ordered by occurence")
     .def("printAllByOccurences", &StringTrie::printOccurencesInRange, "Print all words ordered by occurence in a specified frequency range", py::arg("upper_limit") = INT32_MAX, py::arg("lower_limit") = 1)
     .def("printAllWithPrefix", &StringTrie::printAllWithPrefix, "Print all words with prefix");
}
