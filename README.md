# Masked Hierarchical Transformer for Conversation Structure Modeling

This repo contains the scripts that crawl the reddit dataset used in paper [*Who Did They Respond to? Conversation Structure Modeling Using Masked Hierarchical Transformer*](https://arxiv.org/abs/1911.10666) by Henghui Zhu, Feng Nan, Zhiguo Wang, Ramesh Nallapati, and Bing Xiang in AAAI 2020.

In order to get the dataset, one needs to register an application in Reddit and get clinet ID and screte. The details can be found [here](https://praw.readthedocs.io/en/latest/getting_started/authentication.html#password-flow). 

Then clone the repo using the following command.
```bash
git clone https://github.com/henghuiz/MaskedHierarchicalTransformer.git
```

Next, run the following command for generating dataset in the paper.
```bash
cd MaskedHierarchicalTransformer
unzip raw_data.zip
pip install -r requirements.txt
python generate_dataset.py --client_id=YOUR_CLIENT_ID --client_secret=YOUR_CLIENT_SECRET
```
By default, the dataset will be obtained in the folder `raw_data_with_text`.

If you have used the datasets, please cite the following paper:

```
@article{zhu2019did,
  title={Who did They Respond to? Conversation Structure Modeling using Masked Hierarchical Transformer},
  author={Zhu, Henghui and Nan, Feng and Wang, Zhiguo and Nallapati, Ramesh and Xiang, Bing},
  journal={arXiv preprint arXiv:1911.10666},
  year={2019}
}
```