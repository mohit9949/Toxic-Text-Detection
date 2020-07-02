
# Toxic-Text-Detection
Toxic texts and Abuses can effect a person mentally. In order to tackle that I have developed this project.

This repository consist of a web application which can classify between toxic and non toxic texts. This uses a deep learning model to classify the text.

## Demo: [Click on the image]
<a href="http://www.youtube.com/watch?feature=player_embedded&v=Dnp49qO1PQk
" target="_blank"><img src="http://img.youtube.com/vi/Dnp49qO1PQk/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>


The dataset  was acquired from **Kaggle's Toxic Comment Classification Challenge**. <br>
**Link:** https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data


It uses deep learning LSTM model for classification of the text. For a functioning website with deep learning model, I have prefered to use Django Frame Work.

This LSTM model has a accuracy of **96%** on test data.

### Repository Details:
- The Machine Learning folder contains all the operations performed to build a model. They also contain the trained model saved in '.h5' format.
- The other folder contains Django Files including a fully functioning website in order to test the model.

### Potential:
- This can further developed into a API where every one can take advantage of it to avoid toxic texts. By doing this one can integrate into chatting applications, games, ...etc.
 #### [!] Note: API Service has been implemented and this can be used as a API with POST. This will return a Json format of the prediction of a given text.
### Backdrops:
- This deep learning model is actually a multilabel classification and has the potential to detect various other labels such as insult,obscene, threat, etc. But however during my testing and according to the data visualisation there is a slight bias towards certain labels. Thats why I prefered to keep it as a binary classifier.

**[!]Note:** I have generalized all the other labels as toxic and did not skip them. Skipping them would defeat the purpose of the model.
