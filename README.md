# Getting start Rasa

## Container docker with ubuntu to start
It is strongly recomended to share some folder to put your training files to doesn't lose if the container die
```
$ docker run -it -p 5055:5055 -p 5005:5005 -v /home/oriol.canalias/workspace/learning-rasa/examples:/opt/rasa --name local-ubuntu ubuntu bash
```

Installing python (3.7) and pip
```
/# apt-get update
/# apt-get install -y python3-dev python3-pip
/# apt-get install -y software-properties-common
/# add-apt-repository ppa:deadsnakes/ppa
/# apt-get update
/# apt-get -y install python3.7
/# python3.7 -m pip install rasa
```

## Getting start

Some files are important to do a simple bot.

### data/nlu.md

Is the file with the groups of words or sentences grouping for the same meaning and Rasa use to try predict the correct intent.  

```
## intent:greet
- hey
- ...

## intent:goodbye
- bye
- ...
```
Some examples on folder examples/rasa-assistant

### data/stories.md
Define matches between intents and reponses:
```
## greet
* greet
  - utter_greet

## thank
* thank
  - utter_noworries

## goodbye
* bye
  - utter_bye

## Some question from FAQ
* faq
  - respond_faq
```

### domain.yml
Define the behaivor of the bot over every intent.
```
intents:
  - greet
  - bye
  - thank
  - faq

responses:
  utter_noworries:
    - text: No worries!
  utter_greet:
    - text: Hi
  utter_bye:
    - text: Bye!

actions:
  - respond_faq
```

### data/responses.md
Contains a group of responses that we can use to agroup 
```
## ask channels
* faq/ask_channels
  - We have a comprehensive list of [supported connectors](https://rasa.com/docs/core/connectors/), but if
    you don't see the one you're looking for, you can always create a custom connector by following
    [this guide](https://rasa.com/docs/rasa/user-guide/connectors/custom-connectors/).

## ask languages
* faq/ask_languages
  - You can use Rasa to build assistants in any language you want!
  - You can use Rasa to build assistants in any language2 you want!

## ask rasa x
* faq/ask_rasax
 - Rasa X is a tool to learn from real conversations and improve your assistant. Read more [here](https://rasa.com/docs/rasa-x/)
 ```

## Starting

We can start a new sample with :
```
$ rasa init --no-prompt
```

To train an existing model, we can run:
```
$ rasa train
```
To play with the bot, we can use:
```
$ rasa shell
```

## Testing
```
rasa test --stories tests/conversation_tests.md
```

The test command will produce a directory named `results`. It should contain a file called `failed_stories.md`, where any test cases that failed will be printed. 
As part of a CI/CD pipeline, the test option --fail-on-prediction-errors can be used to throw an exception that stops the pipeline.

## Handling
A lot of conversational assistants have user goals that involve collecting a bunch of information from the user before being able to do something for them. This is called slot filling. 

## Pipelines
- Commom pipelines
-- CRFEntityExtrator - Extract de entities
-- RegexFeaturizer - Adding adicional features to CRFEntityExtractor

- Supervised Embedding
-- WhitespaceTokenizer - Is a Word tokenizer using white spaces
-- CountVectorFeaturizer - Counts the aparitions words to make the prediction
-- EmbeddingIntentClassifier - Make the preditcion using the result of countVectorFeaturizer

- Pretreined Embedding Spacy
-- SpacyNLP - Uses pretrained word embeddings, for spaCy language models
-- SpacyTokenizer - Is a Word tokenizer using the rules defined for the language
-- SpacyFeaturizer - - idem CountVectorFeaturizer
-- SklearnIntentClassifier - idem EmbeddingIntentCalssifier

Punctuation in training model not affect the intent classification.
By default, EntityRecognizor is case-sensitive, but countVector is not case sensitive

## Types of slots
- Text - where you only care whether or not they’ve been specified
- Boolean - Checks if slot is set and if True
- Categorical - Matters if exists and the contain. We can specify accepted values
```
slots:
  price_level:
    type: categorical
    values:
    - low
    - medium
    - high
```
- Float - Matters if exists and the contain. We can range the accepted values
```
slots:
  price_value:
    type: float
    min_value: 0.0
    max_value: 50.0
```
- list: When we want to store multiple values
- Unfeaturized: Doesn't afect to dialog make predictions
## Some commands

```
rasa train nlu
```
Only train the nlu model

```
rasa shell nlu
```
We can talk with the model and view the predictions


