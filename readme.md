# Project Description
RoBERTa (Robustly Optimized BERT Approach) is a transformer-based language model introduced by Liu et al. in 2019. It is a variant of BERT (Bidirectional Encoder Representations from Transformers) that achieves state-of-the-art performance on various natural language processing (NLP) tasks. RoBERTa uses a larger training dataset and longer training duration compared to BERT, and removes the next sentence prediction (NSP) task from the pretraining process. These optimizations make RoBERTa more robust and effective for a variety of tasks such as sentence classification, named entity recognition, and question answering, etc.

This project implements similarity detection in the English language using RoBERTa, a transformer-based model. It evaluates whether two given text inputs are paraphrases of each other using Amaan39/Roberta-Webis-CPC, a fine-tuned RoBERTa model for paraphrase detection trained on Webis Crowd Paraphrase Corpus 2011 dataset.

The application is built using FastAPI, making it easy to deploy and test via API calls.

## Project Structure
```
Similarity-detection-using-RoBERTa/
│── data
│── notebook                # contains implementation notebook
│── app.py                  # FastAPI application
│── predict.py              # Model inference logic
│── requirements.txt        # Dependencies

```

## Usage