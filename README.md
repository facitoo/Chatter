# Chatter
Introduction
-------------

chatter is the implementation of chatbot using NMT - Neural Machine Translation (seq2seq). Includes BPE/WPM-like tokenizator (own implementation). Main purpose of that project is to make an NMT chatbot, but it's fully compatible with NMT and still can be used for sentence translations between two languages.

The code is built on top of NMT but because of lack of available interfaces, some things are "hacked", and parts of the code had to be copied into that project (and will have to be maintained to follow changes in NMT).

This project forks NMT. We had to make a change in our code allowing the use of a stable TensorFlow (1.4) version. Doing so allowed us also to fix some bug before official patch as well as do couple of necessary changes.
