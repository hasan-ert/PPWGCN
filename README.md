# PPWGCN

We provide tha data, source code, and results here. We consult the text_gcn code from https://github.com/yao8839836/text_gcn.

## Reproducing Results

1. Run `python create_my_data.py`(there are four data sets in our experiments)
2. Run `python remove_words.py gcc_my_method_0.5`
3. Run `python build_graph.py gcc_my_method_0.5`
4. Run `python train.py gcc_my_method_0.5`
5. Change `gcc_my_method_0.5` in above 3 command lines to `gcc_my_method_0.4/0.3/0.2/0.1`, `gcc_description_0.5`, `mozilla_my_method_/0.5/0.4/0.3/0.2/0.1` ,  `eclipse_my_method_/0.5/0.4/0.3/0.2/0.1`,  `netbeans_my_method_/0.5/0.4/0.3/0.2/0.1`, `eclipse_description_0.5`, `mozilla_description_0.5`, and `netbeans_description_0.5`,when producing results for other datasets.