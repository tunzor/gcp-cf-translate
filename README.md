# Cloud Function Translator

This is a simple translator service written in python leveraging the [Google Translate API](https://cloud.google.com/translate/docs/).
It's designed to run as a [cloud function](https://cloud.google.com/functions/) on the Google Cloud Platform and can be done so with the following `gcloud` commands.

#### Enables the translate API
`gcloud services enable translate.googleapis.com` 
#### Deploys the Cloud Function
**Note**: This must be run in the directory containing this repo's code
`gcloud functions deploy translator --runtime python37 --trigger-http --entry-point translate`


## Usage
The `gcloud functions deploy` command above will return the HTTP endpoint, among other things, and will look similar to:
`https://[REGION]-[YOUR_PROJECT_ID].cloudfunctions.net/translator`

Two parameters are required: `toLang` (the language to translate the text to) and `text` (the text to translate)
*A list of supported language codes is [here](https://cloud.google.com/translate/docs/languages)*

For example, this will translate `hello world` to Spanish:
`https://[REGION]-[YOUR_PROJECT_ID].cloudfunctions.net/translator?toLang=es&text=hello world`
