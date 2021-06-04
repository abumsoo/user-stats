# User stats

Web application that takes input through a file or through direct text, and generates data visualizations based on the data in the file or text. The app expects a JSON file in the format that is used in [https://randomuser.me/](https://randomuser.me/).

## Usage

Get JSON data from randomuser.me

```
curl https://randomuser.me/api/?results=1000 > user_data.json
```

Go to https://salty-island-70058.herokuapp.com/ and insert file that we just downloaded (user_data.json)

## API usage

```
curl -H "Accept: text/plain" -H "Content-Type: application/json" --request POST -d @user_data.json https://salty-island-70058.herokuapp.com/api/stat_api/
```

Change the accept header to receive data in the following forms: JSON, XML, or plain text.
