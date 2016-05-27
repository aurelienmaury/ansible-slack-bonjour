# Bonjour à Madame, Bonjour à Monsieur

The playbook you never asked for...

* Install Python dependencies:

```
pip install -r requirements.txt
```

* Fill a YAML file (let's say `bonjour-vars.yml` with these variables:

```
---
slack_webhook_token: "-- see https://slack.com/apps/manage/A0F7XDUAZ-incoming-webhooks for getting yours --"
slack_channel: "#random"
slack_bot_name: "AnsiBot"
```

* Enjoy:

```
ansible-playbook bonjour.yml -e@bonjour-vars.yml
```

I hope it will help you build a better DevOps culture... ;-)
