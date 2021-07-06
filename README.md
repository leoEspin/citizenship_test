# Citizenship test simulator

The questions bank json file is a text dump from the [USCIS's Official list of civics questions and answers for the naturalization test](https://www.uscis.gov/sites/default/files/document/questions-and-answers/100q.pdf).

The simulator takes 10 random questions from the bank and compares the typed answers with the official answers. Currently the answers have to match the text exactly to be deemed correct (which is ok, because the correct answers will be displayed which is good for practicing anyway).

Run the test with `test_simulation.ipynb` (or check how to call the main routine from this file, if you want to use the command line instead)

The file `cleaning.py` takes a text dump from the original pdf and produces a structured json file. The notebook `data_structure.ipynb` was an initial exploration of appropriate data structures to store the questions/answers. 