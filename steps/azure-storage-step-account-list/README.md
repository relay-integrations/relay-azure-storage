# azure-storage-step-account-list

This [Azure](https://azure.microsoft.com/en-us/services/storage/) step container lists the accounts
in an Azure subscription or resource group and sets an output, `storageAccounts`, to an array of storage account objects.

## Example

```yaml
steps:
# ...
- name: azure-storage-list-accounts
  image: relaysh/azure-storage-step-account-list
  spec:
    azure:
      connection: !Connection { type: azure, name: my-azure-account }
    resourceGroup: 'my_resource_group'
```

## Example output `storageAccounts`

```
[
   {
      "id":"/subscriptions/asdfwer2-c108-452b-8178-f548c95d18fe/resourceGroups/1234/providers/Microsoft.Storage/storageAccounts/1234testing",
      "name":"1234testing",
      "type":"Microsoft.Storage/storageAccounts",
      "tags":{

      },
      "location":"eastus",
      "sku":{
         "name":"Standard_LRS",
         "tier":"Standard"
      },
      "kind":"Storage",
      "provisioning_state":"Succeeded",
      "primary_endpoints":{
         "blob":"https://1234testing.blob.core.windows.net/",
         "queue":"https://1234testing.queue.core.windows.net/",
         "table":"https://1234testing.table.core.windows.net/",
         "file":"https://1234testing.file.core.windows.net/"
      },
      "primary_location":"eastus",
      "status_of_primary":"available",
      "creation_time":"2019-04-08T14:37:10.824178Z",
      "encryption":{
         "services":{
            "blob":{
               "enabled":True,
               "last_enabled_time":"2019-04-08T14:37:10.949187Z",
               "key_type":"Account"
            },
            "file":{
               "enabled":True,
               "last_enabled_time":"2019-04-08T14:37:10.949187Z",
               "key_type":"Account"
            }
         },
         "key_source":"Microsoft.Storage"
      },
      "enable_https_traffic_only":False,
      "network_rule_set":{
         "bypass":"AzureServices",
         "virtual_network_rules":[

         ],
         "ip_rules":[

         ],
         "default_action":"Allow"
      },
      "private_endpoint_connections":[

      ]
   }
]
```
