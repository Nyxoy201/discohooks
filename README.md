<div align="center">

# DiscoHooks 
</div>

## Projet Description 
DiscoHooks is a simple python library to use discord webhooks.

## Lib Features 
- Send Message To Webhook
- Send File To Webhook
- Send Embed To Webhook
- Delete Webhook
- Customize Webhook
- Get Webhook Informations
- Use multiple webhooks

## Installing
The requests library is required.

```
# Install Requests Lib
pip install reqests

#Install Discohooks Lib
pip install discohooks
```

## How To Use
**To use the library without embed :**
First, import the library : 
```python
from discohooks import Webhook
```

1. **Send Message :**
```python
from discohooks import Webhook

hook = Webhook(["webhook_url_1", "webhook_url_2"])
# Even if you're using only one webhook, still use the [ ]

hook.send(content="Hello Word!")
```

2. **Delete Webhook :**
```python
from discohooks import Webhook

hook = Webhook(["webhook_url_1", "webhook_url_2"])
# Even if you're using only one webhook, still use the [ ]

hook.delete()
```

3. **Customize Webhook :**
```python
from discohooks import Webhook

hook = Webhook(["webhook_url_1", "webhook_url_2"])
# Even if you're using only one webhook, still use the [ ]

hook.customize(name="WEBHOOK_NAME", avatar="AVATAR_URL")
```

