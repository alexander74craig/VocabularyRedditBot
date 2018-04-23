#include <pybind11/pybind11.h>
#include <pybind11/stl_bind.h>

// stringtrie.h code can be found at https://github.com/lcsfrey/Data_Structures
#include "stringtrie.h"

namespace py = pybind11;

PYBIND11_MAKE_OPAQUE(std::vector<std::string>);

// creates python module that can be imported with "import py_stringtrie"

PYBIND11_MODULE(py_stringtrie, trie) {

  // creates a c++ std::vector<std::string> object called StringVector in python
  
  py::bind_vector<std::vector<std::string>>(trie, "StringVector");

  // StringTrie is a prefix tree that stores character of string as a trie node,
  // where each child character node represents the suffix of the previous 
  // character. Each unique prefix of a word is only stored once. For example, 
  // if "prepared", "prepaid", and "prep" are added to the trie, the characters 
  // "prep" are only stored once, the following "a" is stored once, and the only 
  // "id" and "red" are stored separately.
  
  py::class_<StringTrie>(trie, "StringTrie")
  
     // constructor
     
     .def(py::init<>())
     
     // insert functions
     
     .def("addWord", &StringTrie::addWord,  "Add word to trie")
     
     // removal functions
     
     .def("remove", &StringTrie::remove, "Remove word from trie")
     
     .def("removeAllWithPrefix", &StringTrie::removeAllWithPrefix, 
          "Remove all words with prefix")
          
     .def("resetTrie", &StringTrie::resetTrie, "Remove all words from trie")
     
     // containment functions
     
     .def("contains", &StringTrie::contains, "Returns true if word is in trie")
     
     // accessor functions
     
     .def("getNumberUniqueWords", &StringTrie::getNumberUniqueWords, 
          "Get number of unique words")
          
     .def("getNumberTotalWords", &StringTrie::getNumberTotalWords, 
          "Get number of total words")
          
     // print functions
     
     .def("printAll", &StringTrie::printAll, "Print all words")
     
     .def("printAllByOccurences", &StringTrie::printAllByOccurences, 
          "Print all words ordered by occurence")
          
     .def("printAllByOccurences", &StringTrie::printOccurencesInRange, 
          "Print all words ordered by occurence in a specified frequency range", 
          py::arg("upper_limit") = INT32_MAX, 
          py::arg("lower_limit") = 1)
          
     .def("printAllWithPrefix", &StringTrie::printAllWithPrefix, 
          "Print all words with prefix")
          
     // read & write functions
     
     .def("writeToFile", &StringTrie::writeToFile, 
          "Write all words and their occurences to file",
          py::arg("filename") = "comment_words.txt")
          
     .def("readFromFile", &StringTrie::readFromFile, 
          "Read all words and their occurences from file",
          py::arg("filename") = "comment_words.txt");
}
