# IdentiFusion: A Multimodal Approach to Facial Attribute Recognition using FaceBERT and LightenedMOON

<p align="center">
  <img src="https://github.com/tarhanefe/bilkent-cs115-labs/assets/73281981/353e59fa-4cf5-4be5-b62f-afa383f3fdcd" alt="Bilkent University Logo" width = "300" />
</p>

## Authors
- Efe Tarhan, EEE B.Sc, Bilkent University
- Ege Yüceel, EEE B.Sc, Bilkent University
- M. Berk Alemdar, EEE B.Sc, Bilkent University

## Abstract
IdentiFusion presents a novel multimodal system that synergistically combines Natural Language Processing (NLP) and Computer Vision to match textual face descriptions with corresponding facial images. The system integrates FaceBERT, an NLP model fine-tuned for extracting facial features from text, and LightenedMOON, a Computer Vision model trained on the CelebA dataset for facial attribute recognition from images. This project demonstrates the effective integration of NLP and Computer Vision for applications in image retrieval, matching, and recommendation systems to aid in law enforcement and forensic investigations.

## Introduction
This project aims to bridge the gap between NLP and Computer Vision by developing a system capable of comparing textual descriptions and visual representations of human faces. The integration of these fields allows for the creation of systems that can understand and interpret both textual and visual data.

<p align="center">
  <img src="https://github.com/tarhanefe/bilkent-ee486/assets/73281981/62774892-9f39-4d61-952f-9f85e2e10e49" alt="Bilkent University Logo" width = "400" />
</p>

## Methodology
### Datasets
- **CelebA Dataset**: A large-scale face attributes dataset used for training the LightenedMOON model.
- **SynthFace-3K Dataset**: A synthetic dataset created using the GPT API for fine-tuning the FaceBERT model. It maps input sequences to 40 human facial attributes.

### Models
- **FaceBERT**: A fine-tuned BERT model for extracting facial features from text. It outputs a 40-dimensional vector representing facial attributes.
- **LightenedMOON**: A deep convolutional neural network (DCNN) trained on the CelebA dataset for facial attribute recognition from images. It also outputs a 40-dimensional vector.


<p align="center">
  <img src="https://github.com/tarhanefe/bilkent-ee486/assets/73281981/d8c7b82f-5ef4-4dce-a799-5e9a24a52fbb" alt="Bilkent University Logo" width = "400" />
</p>


### Comparator
A comparator is used to compare the outputs of the NLP and Computer Vision models to predict the face that aligns with the textual face description. This involves a weighted dot product method to enhance the accuracy of the predictions.

## Results
The performance of the system was evaluated using training and validation loss plots for FaceBERT, attribute recognition accuracy for LightenedMOON, and the overall accuracy of the multimodal system. The results demonstrate the effectiveness of the system in matching textual face descriptions with visual representations.


## Discussion & Conclusion
The integration of NLP and Computer Vision in IdentiFusion shows promising results, particularly in handling diverse sentence structures and facial attributes. Future work could focus on refining the model's accuracy for less frequent features and improving contextual relevance in image captioning tasks.

## How to Use
### Requirements
- Python 3.x
- PyTorch
- Transformers (Huggingface)
- OpenCV
- NLTK
- MXNet

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/tarhanefe/bilkent-ee486.git
   cd bilkent-ee486


- [Report](https://github.com/tarhanefe/bilkent-ee486/blob/main/report.pdf)
  
- [Code](https://github.com/tarhanefe/bilkent-ee486/blob/main/code.ipynb)

